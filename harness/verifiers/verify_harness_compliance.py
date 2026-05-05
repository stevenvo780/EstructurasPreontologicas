"""Verificador formal: el propio harness cumple las convenciones de Claude Code.

Audita frontmatters de:
  - .claude/agents/*.md (campos obligatorios, modelo alias, tools como list)
  - .claude/commands/*.md (description + allowed-tools como list)
  - .claude/skills/*/SKILL.md (name + description mínimos)

Detecta drift cuando alguien edite un archivo y rompa el schema.

Re-validación de la regla recursiva: el harness está sujeto a sus propias reglas.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import yaml

from harness.lib.tesis_paths import repo_root


VALID_MODELS = {"sonnet", "opus", "haiku", "inherit", None}
KNOWN_TOOLS = {
    "Read", "Write", "Edit", "MultiEdit", "Bash", "Grep", "Glob",
    "WebSearch", "WebFetch", "Task", "TodoWrite", "NotebookEdit",
    "ListMcpResourcesTool", "ReadMcpResourceTool",
}


def parse_frontmatter(text: str) -> dict | None:
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        return yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None


def audit_agents() -> list[dict]:
    issues = []
    agents_dir = repo_root() / ".claude" / "agents"
    if not agents_dir.exists():
        return [{"file": str(agents_dir), "severity": "high", "issue": "directory missing"}]
    for f in sorted(agents_dir.glob("*.md")):
        if f.name == "README.md":
            continue
        rel = str(f.relative_to(repo_root()))
        text = f.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            issues.append({"file": rel, "severity": "critical", "issue": "no frontmatter or invalid YAML"})
            continue
        if not fm.get("name"):
            issues.append({"file": rel, "severity": "critical", "issue": "missing 'name'"})
        elif fm["name"] != f.stem:
            issues.append({"file": rel, "severity": "high",
                           "issue": f"name '{fm['name']}' != filename stem '{f.stem}'"})
        if not fm.get("description"):
            issues.append({"file": rel, "severity": "critical", "issue": "missing 'description'"})
        else:
            desc = fm["description"]
            if len(desc) < 50:
                issues.append({"file": rel, "severity": "medium",
                               "issue": f"description too short ({len(desc)} chars; recommend >50)"})
            triggers = ("use proactively", "use when", "must be used", "use this")
            if not any(t in desc.lower() for t in triggers):
                issues.append({"file": rel, "severity": "medium",
                               "issue": "description lacks delegation trigger ('Use proactively when...', 'MUST BE USED whenever...', etc.)"})
        tools = fm.get("tools")
        if tools is None:
            issues.append({"file": rel, "severity": "low",
                           "issue": "no 'tools' field — agent inherits ALL tools (consider whitelisting)"})
        elif not isinstance(tools, list):
            issues.append({"file": rel, "severity": "high",
                           "issue": f"'tools' must be YAML list, got {type(tools).__name__}"})
        else:
            unknown = [t for t in tools if t not in KNOWN_TOOLS and not t.startswith("mcp__")]
            if unknown:
                issues.append({"file": rel, "severity": "medium",
                               "issue": f"unknown tools: {unknown} (typo? check Claude Code docs)"})
        model = fm.get("model")
        if model not in VALID_MODELS:
            issues.append({"file": rel, "severity": "medium",
                           "issue": f"model '{model}' is not an alias (sonnet/opus/haiku/inherit). Versioned IDs break across releases."})
        body = parts_body(text)
        if len(body.strip()) < 200:
            issues.append({"file": rel, "severity": "medium",
                           "issue": f"body very short ({len(body)} chars; agent likely under-specified)"})
    return issues


def audit_commands() -> list[dict]:
    issues = []
    cmd_dir = repo_root() / ".claude" / "commands"
    if not cmd_dir.exists():
        return [{"file": str(cmd_dir), "severity": "high", "issue": "directory missing"}]
    for f in sorted(cmd_dir.glob("*.md")):
        if f.name == "README.md":
            continue
        rel = str(f.relative_to(repo_root()))
        text = f.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            issues.append({"file": rel, "severity": "critical", "issue": "no frontmatter or invalid YAML"})
            continue
        if not fm.get("description"):
            issues.append({"file": rel, "severity": "critical", "issue": "missing 'description'"})
        at = fm.get("allowed-tools")
        if at is not None and not isinstance(at, list):
            issues.append({"file": rel, "severity": "high",
                           "issue": f"'allowed-tools' must be YAML list, got {type(at).__name__}"})
    return issues


def audit_skills() -> list[dict]:
    issues = []
    skills_dir = repo_root() / ".claude" / "skills"
    if not skills_dir.exists():
        return []
    for sk in sorted(skills_dir.iterdir()):
        if not sk.is_dir():
            continue
        skill_md = sk / "SKILL.md"
        if not skill_md.exists():
            issues.append({"file": str(sk.relative_to(repo_root())),
                           "severity": "critical", "issue": "missing SKILL.md"})
            continue
        rel = str(skill_md.relative_to(repo_root()))
        text = skill_md.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            issues.append({"file": rel, "severity": "critical", "issue": "no frontmatter"})
            continue
        for required in ("name", "description"):
            if not fm.get(required):
                issues.append({"file": rel, "severity": "critical",
                               "issue": f"missing '{required}'"})
    return issues


def audit_settings() -> list[dict]:
    issues = []
    settings = repo_root() / ".claude" / "settings.json"
    if not settings.exists():
        return [{"file": ".claude/settings.json", "severity": "high", "issue": "missing"}]
    try:
        data = json.loads(settings.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [{"file": ".claude/settings.json", "severity": "critical",
                 "issue": f"invalid JSON: {e}"}]
    hooks = data.get("hooks", {})
    for ev in ("PreToolUse", "PostToolUse", "Stop", "SessionStart", "UserPromptSubmit"):
        for entry in hooks.get(ev, []):
            for h in entry.get("hooks", []):
                cmd = h.get("command", "")
                if cmd and not cmd.startswith("/"):
                    script = repo_root() / cmd
                    if not script.exists():
                        issues.append({"file": ".claude/settings.json",
                                       "severity": "high",
                                       "issue": f"hook '{ev}' references missing script: {cmd}"})
    return issues


def audit_mcp() -> list[dict]:
    issues = []
    mcp = repo_root() / ".mcp.json"
    if not mcp.exists():
        return []
    try:
        data = json.loads(mcp.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [{"file": ".mcp.json", "severity": "critical",
                 "issue": f"invalid JSON: {e}"}]
    if "mcpServers" not in data:
        issues.append({"file": ".mcp.json", "severity": "high",
                       "issue": "missing 'mcpServers' key"})
    return issues


def parts_body(text: str) -> str:
    parts = text.split("---", 2)
    return parts[2] if len(parts) >= 3 else text


def main() -> dict:
    all_issues = (audit_agents() + audit_commands() + audit_skills()
                  + audit_settings() + audit_mcp())
    by_sev = {"critical": [], "high": [], "medium": [], "low": []}
    for i in all_issues:
        by_sev[i["severity"]].append(i)

    if by_sev["critical"]:
        status = "fail"
    elif by_sev["high"]:
        status = "fail"
    elif by_sev["medium"]:
        status = "warn"
    else:
        status = "pass"

    return {
        "verifier": "harness_compliance",
        "status": status,
        "agents_audited": len(list((repo_root() / ".claude/agents").glob("*.md"))) - 1,
        "commands_audited": len(list((repo_root() / ".claude/commands").glob("*.md"))) - 1,
        "skills_audited": len(list((repo_root() / ".claude/skills").iterdir()))
                          if (repo_root() / ".claude/skills").exists() else 0,
        "issues_count": len(all_issues),
        "issues_by_severity": {k: len(v) for k, v in by_sev.items()},
        "issues_critical": by_sev["critical"],
        "issues_high": by_sev["high"],
        "issues_medium": by_sev["medium"][:10],
        "issues_low": by_sev["low"][:5],
        "interpretation": (
            "Re-valida que el propio harness cumple la documentación oficial Claude Code: "
            "frontmatter de sub-agentes, slash commands, skills, hooks y MCPs. "
            "Critical/high bloquean carga; medium/low son advisory."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, ensure_ascii=False))
