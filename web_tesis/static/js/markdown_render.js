(() => {
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initMarkdownEnhancements, { once: true });
  } else {
    initMarkdownEnhancements();
  }
})();

function initMarkdownEnhancements() {
  renderMermaidBlocks();
  renderMathBlocks();
  initHashNavigation();
}

function renderMermaidBlocks() {
  const codeBlocks = document.querySelectorAll("pre > code.language-mermaid");
  if (!codeBlocks.length) return;

  codeBlocks.forEach((code) => {
    const source = (code.textContent || "").trim();
    if (!source) return;

    const wrapper = document.createElement("div");
    wrapper.className = "mermaid-wrap";

    const graph = document.createElement("div");
    graph.className = "mermaid";
    graph.textContent = source;
    wrapper.appendChild(graph);

    const pre = code.parentElement;
    if (pre && pre.parentElement) {
      pre.parentElement.replaceChild(wrapper, pre);
    }
  });

  if (typeof window.mermaid === "undefined") {
    return;
  }

  try {
    window.mermaid.initialize({
      startOnLoad: false,
      securityLevel: "loose",
      theme: "default",
    });
    window.mermaid.run({ nodes: document.querySelectorAll(".mermaid") });
  } catch (error) {
    console.error("Error renderizando Mermaid", error);
  }
}

function renderMathBlocks() {
  if (typeof window.renderMathInElement === "undefined") {
    return;
  }

  const targets = document.querySelectorAll(".markdown-body");
  targets.forEach((target) => {
    try {
      window.renderMathInElement(target, {
        delimiters: [
          { left: "$$", right: "$$", display: true },
          { left: "\\[", right: "\\]", display: true },
          { left: "\\(", right: "\\)", display: false },
          { left: "$", right: "$", display: false },
        ],
        throwOnError: false,
      });
    } catch (error) {
      console.error("Error renderizando fórmulas", error);
    }
  });
}

function initHashNavigation() {
  const links = document.querySelectorAll('a[href^="#"]');
  links.forEach((link) => {
    link.addEventListener("click", (event) => {
      const href = link.getAttribute("href") || "";
      if (!href.startsWith("#")) return;
      event.preventDefault();
      scrollToHash(href, true);
    });
  });

  window.addEventListener("hashchange", () => scrollToHash(window.location.hash, false));

  if (window.location.hash) {
    // Espera a que Mermaid/KaTeX terminen de transformar el DOM.
    setTimeout(() => scrollToHash(window.location.hash, false), 120);
  }
}

function normalizeAscii(value) {
  try {
    return value.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  } catch (_) {
    return value;
  }
}

function normalizeAnchorKey(value) {
  return normalizeAscii(String(value || ""))
    .toLowerCase()
    .replace(/[_\s]+/g, "-")
    .replace(/[^\w-]+/g, "-")
    .replace(/-+/g, "-")
    .replace(/^-|-$/g, "");
}

function scrollToHash(rawHash, pushState) {
  const hash = (rawHash || "").replace(/^#/, "");
  if (!hash) return;

  const decoded = decodeURIComponent(hash);
  const candidates = [decoded];
  const ascii = normalizeAscii(decoded);
  if (ascii && !candidates.includes(ascii)) {
    candidates.push(ascii);
  }
  const underscoreSwap = decoded.replace(/_/g, "-");
  if (underscoreSwap && !candidates.includes(underscoreSwap)) {
    candidates.push(underscoreSwap);
  }

  let target = null;
  for (const id of candidates) {
    target = document.getElementById(id);
    if (target) break;
  }
  if (!target) {
    const keySet = new Set(candidates.map((x) => normalizeAnchorKey(x)));
    const allWithId = document.querySelectorAll("[id]");
    for (const el of allWithId) {
      const id = el.getAttribute("id");
      if (!id) continue;
      if (keySet.has(normalizeAnchorKey(id))) {
        target = el;
        break;
      }
    }
  }
  if (!target) {
    const desired = normalizeAnchorKey(decoded);
    const desiredTokens = desired.split("-").filter((t) => t && !/^\d+$/.test(t) && t.length > 2);
    if (desiredTokens.length) {
      const allWithId = document.querySelectorAll("[id]");
      let best = null;
      let bestScore = 0;
      for (const el of allWithId) {
        const id = el.getAttribute("id");
        if (!id) continue;
        const idKey = normalizeAnchorKey(id);
        const score = desiredTokens.reduce((acc, tk) => acc + (idKey.includes(tk) ? 1 : 0), 0);
        if (score > bestScore) {
          bestScore = score;
          best = el;
        }
      }
      if (best && bestScore >= 1) {
        target = best;
      }
    }
  }
  if (!target) return;

  target.scrollIntoView({ behavior: "smooth", block: "start" });

  if (pushState) {
    const safeHash = `#${encodeURIComponent(decoded)}`;
    if (window.location.hash !== safeHash) {
      history.pushState(null, "", safeHash);
    }
  }
}
