(() => {
  const node = document.getElementById("case-data");
  if (!node) return;

  let caseData;
  try {
    caseData = JSON.parse(node.textContent || "{}");
  } catch (error) {
    console.error("No se pudo parsear case-data", error);
    return;
  }

  const phases = buildPhases(caseData);
  if (!phases.length) return;

  renderAll(phases);

  const onResize = debounce(() => {
    safeRender("case-chart-phase-overview", () => renderPhaseOverview(phases));
    safeRender("case-chart-edi-evidence", () => renderEdiEvidence(phases));
  }, 180);

  window.addEventListener("resize", onResize);
})();

function renderAll(phases) {
  safeRender("case-chart-phase-overview", () => renderPhaseOverview(phases));
  safeRender("case-chart-edi-evidence", () => renderEdiEvidence(phases));
  safeRender("case-chart-gates", () => renderGates(phases));
  safeRender("case-chart-errors", () => renderErrors(phases));
  safeRender("case-chart-correlations", () => renderCorrelations(phases));
  safeRender("case-chart-calibration", () => renderCalibration(phases));
  safeRender("case-chart-details", () => renderDetails(phases));
  safeRender("case-chart-dynamics", () => renderDynamics(phases));
  safeRender("case-chart-checks", () => renderChecks(phases));
  safeRender("case-chart-table", () => renderFullTable(phases));
}

function safeRender(rootId, renderFn) {
  const root = document.getElementById(rootId);
  if (!root) return;
  try {
    renderFn();
  } catch (error) {
    console.error(`Error renderizando ${rootId}`, error);
    root.innerHTML = '<p class="mini-note" style="color:#8d2f26">No se pudo renderizar este bloque.</p>';
  }
}

function buildPhases(caseData) {
  const phaseMap = (caseData && caseData.phases) || {};
  const order = Array.isArray(caseData.phase_order) && caseData.phase_order.length
    ? caseData.phase_order
    : Object.keys(phaseMap);

  return order
    .map((key, idx) => {
      const phase = phaseMap[key];
      if (!phase || typeof phase !== "object") return null;
      return {
        ...phase,
        key,
        label: phaseLabel(key),
        color: phaseColor(key, idx),
      };
    })
    .filter(Boolean);
}

function phaseLabel(key) {
  if (key === "real") return "Fase Real";
  if (key === "synthetic") return "Fase Sintética";
  return `Fase ${String(key).replace(/_/g, " ")}`;
}

function phaseColor(key, idx) {
  if (key === "real") return "#2f7b73";
  if (key === "synthetic") return "#ca6d2f";
  const palette = ["#315a8f", "#8f4f7c", "#7c8a2f", "#8c3a3a", "#5b5b9f"];
  return palette[idx % palette.length];
}

function renderPhaseOverview(phases) {
  const root = document.getElementById("case-chart-phase-overview");
  if (!root) return;

  const metricDefs = [
    {
      label: "overall_pass",
      get: (p) => (typeof p.overall_pass === "boolean" ? (p.overall_pass ? 1 : 0) : null),
      text: (v) => (v === null ? "n/a" : v > 0 ? "SI" : "NO"),
      domain: [0, 1],
    },
    {
      label: "criterios pasados",
      get: (p) => toNumber(p.criteria_pass_ratio),
      text: (v) => (v === null ? "n/a" : fmtPercent(v)),
      domain: [0, 1],
    },
    {
      label: "EDI",
      get: (p) => toNumber(getPath(p, "edi.value")),
      text: (v) => fmt(v),
      domain: [-1, 1],
      signed: true,
    },
    {
      label: "p-perm",
      get: (p) => {
        const pv = toNumber(getPath(p, "edi.pvalue"));
        return pv === null ? null : 1 - pv;
      },
      text: (_, p) => {
        const pv = toNumber(getPath(p, "edi.pvalue"));
        return pv === null ? "n/a" : pv.toFixed(3);
      },
      domain: [0, 1],
    },
    {
      label: "CR symploke",
      get: (p) => toNumber(getPath(p, "symploke.cr")),
      text: (v) => fmt(v),
      domain: [0, 2],
    },
    {
      label: "corr ABM",
      get: (p) => toNumber(getPath(p, "correlations.abm_obs")),
      text: (v) => fmt(v),
      domain: [-1, 1],
      signed: true,
    },
    {
      label: "RMSE delta",
      get: (p) => toNumber(getPath(p, "errors.rmse_gain")),
      text: (v) => fmtSignedPercent(v),
      domain: [-1, 1],
      signed: true,
    },
    {
      label: "inf. efectiva",
      get: (p) => toNumber(getPath(p, "effective_information")),
      text: (v) => fmt(v),
      domain: [0, 1],
    },
  ];

  const cards = phases
    .map((phase) => {
      const rows = metricDefs
        .map((def) => {
          const value = def.get(phase);
          const bar = buildMiniBar(value, def.domain, def.signed, phase.color);
          const rendered = typeof def.text === "function" ? def.text(value, phase) : fmt(value);
          return `
            <div class="metric-mini-row">
              <span class="metric-mini-label">${escapeHtml(def.label)}</span>
              ${bar}
              <strong class="metric-mini-value">${escapeHtml(rendered)}</strong>
            </div>
          `;
        })
        .join("");

      const tag = typeof phase.overall_pass === "boolean" ? (phase.overall_pass ? "PASA" : "NO PASA") : "N/A";
      return `
        <article class="phase-overview-card">
          <h4 style="color:${phase.color}">${escapeHtml(phase.label)}</h4>
          <p class="phase-overview-kicker">${escapeHtml(tag)} · categoría ${escapeHtml(getPath(phase, "taxonomy.category") || "n/a")}</p>
          <div class="metric-mini-list">${rows}</div>
        </article>
      `;
    })
    .join("");

  root.innerHTML = `<div class="phase-overview-grid">${cards}</div>`;
}

function renderEdiEvidence(phases) {
  const root = document.getElementById("case-chart-edi-evidence");
  if (!root) return;

  const rows = phases
    .map((phase) => {
      const value = toNumber(getPath(phase, "edi.value"));
      const lo = toNumber(getPath(phase, "edi.ci_lo"));
      const hi = toNumber(getPath(phase, "edi.ci_hi"));
      const null95 = toNumber(getPath(phase, "edi.null_95"));
      const pvalue = toNumber(getPath(phase, "edi.pvalue"));
      const sig = getPath(phase, "edi.significant");
      if ([value, lo, hi, null95].every((x) => x === null)) {
        return null;
      }
      return { phase, value, lo, hi, null95, pvalue, sig };
    })
    .filter(Boolean);

  if (!rows.length) {
    root.innerHTML = '<p class="mini-note">Sin datos EDI/IC para este caso.</p>';
    return;
  }

  const extrema = [];
  rows.forEach((r) => {
    [r.value, r.lo, r.hi, r.null95].forEach((v) => {
      if (typeof v === "number" && Number.isFinite(v)) extrema.push(v);
    });
  });

  if (!extrema.length) {
    root.innerHTML = '<p class="mini-note">Sin valores numéricos EDI.</p>';
    return;
  }

  let xMin = Math.min(...extrema);
  let xMax = Math.max(...extrema);
  const padExt = Math.max(0.05, (xMax - xMin) * 0.12);
  xMin -= padExt;
  xMax += padExt;
  if (Math.abs(xMax - xMin) < 1e-6) {
    xMin -= 0.25;
    xMax += 0.25;
  }

  const width = Math.max(560, root.clientWidth || 560);
  const rowGap = 56;
  const height = 30 + rowGap * rows.length + 24;
  const pad = { l: 132, r: 90, t: 20, b: 30 };

  const scaleX = (x) => pad.l + ((x - xMin) / (xMax - xMin)) * (width - pad.l - pad.r);
  const tickValues = [xMin, (xMin + xMax) / 2, xMax];

  const content = rows
    .map((r, idx) => {
      const y = pad.t + idx * rowGap + 16;
      const axis = `<line x1="${pad.l}" y1="${y}" x2="${width - pad.r}" y2="${y}" stroke="#516366" stroke-width="1" />`;

      const ci =
        typeof r.lo === "number" && typeof r.hi === "number"
          ? `<line x1="${scaleX(r.lo).toFixed(2)}" y1="${y}" x2="${scaleX(r.hi).toFixed(2)}" y2="${y}" stroke="${r.phase.color}" stroke-width="7" stroke-linecap="round" opacity="0.35" />`
          : "";

      const nullLine =
        typeof r.null95 === "number"
          ? `<line x1="${scaleX(r.null95).toFixed(2)}" y1="${(y - 13).toFixed(2)}" x2="${scaleX(r.null95).toFixed(2)}" y2="${(y + 13).toFixed(2)}" stroke="#8f342a" stroke-width="2" stroke-dasharray="4 2" />`
          : "";

      const valuePoint =
        typeof r.value === "number"
          ? `<circle cx="${scaleX(r.value).toFixed(2)}" cy="${y}" r="5" fill="${r.phase.color}"><title>${escapeHtml(r.phase.label)} EDI=${fmt(r.value)}</title></circle>`
          : "";

      const sigText =
        typeof r.sig === "boolean" ? (r.sig ? "signif." : "no signif.") : "sig n/a";
      const pText = typeof r.pvalue === "number" ? `p=${r.pvalue.toFixed(3)}` : "p=n/a";

      return `
        <g>
          ${axis}
          ${ci}
          ${nullLine}
          ${valuePoint}
          <text x="${pad.l - 8}" y="${y + 4}" text-anchor="end" font-size="11" fill="#273a3d">${escapeHtml(r.phase.label)}</text>
          <text x="${width - pad.r + 8}" y="${y + 4}" text-anchor="start" font-size="10.5" fill="#31484c">${escapeHtml(pText)} · ${escapeHtml(sigText)}</text>
        </g>
      `;
    })
    .join("");

  const ticks = tickValues
    .map((tv) => {
      const x = scaleX(tv).toFixed(2);
      return `<g><line x1="${x}" y1="${height - pad.b}" x2="${x}" y2="${height - pad.b + 5}" stroke="#516366" /><text x="${x}" y="${height - pad.b + 17}" text-anchor="middle" font-size="10.5" fill="#3a5053">${fmt(tv)}</text></g>`;
    })
    .join("");

  root.innerHTML = `
    <p class="mini-note">Intervalo grueso: IC bootstrap (95%). Línea punteada: umbral nulo 95%. Punto: EDI observado.</p>
    <div class="case-svg-wrap">
      <svg width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" role="img" aria-label="Evidencia EDI por fase">
        <rect width="${width}" height="${height}" fill="#fffaf5" />
        <line x1="${pad.l}" y1="${height - pad.b}" x2="${width - pad.r}" y2="${height - pad.b}" stroke="#516366" />
        ${content}
        ${ticks}
      </svg>
    </div>
  `;
}

function renderGates(phases) {
  const root = document.getElementById("case-chart-gates");
  if (!root) return;

  const gatesSet = new Set();
  phases.forEach((phase) => {
    (phase.gates || []).forEach((gate) => {
      gatesSet.add(gate.key);
    });
  });

  const defaultOrder = [
    "c1_convergence",
    "c2_robustness",
    "c3_replication",
    "c4_validity",
    "c5_uncertainty",
    "symploke_pass",
    "non_locality_pass",
    "persistence_pass",
    "emergence_pass",
    "coupling_ok",
    "rmse_fraud_check",
  ];

  const ordered = defaultOrder.filter((k) => gatesSet.has(k)).concat(
    [...gatesSet].filter((k) => !defaultOrder.includes(k)).sort()
  );

  if (!ordered.length) {
    root.innerHTML = '<p class="mini-note">Sin compuertas registradas.</p>';
    return;
  }

  const summaries = phases
    .map((phase) => {
      const values = (phase.gates || []).map((g) => g.pass).filter((v) => typeof v === "boolean");
      const passed = values.filter(Boolean).length;
      const total = values.length;
      const ratio = total ? passed / total : null;
      const bar = buildMiniBar(ratio, [0, 1], false, phase.color);
      return `
        <article class="gate-summary-card">
          <h4 style="color:${phase.color}">${escapeHtml(phase.label)}</h4>
          <div class="metric-mini-row">
            <span class="metric-mini-label">gates pass</span>
            ${bar}
            <strong class="metric-mini-value">${total ? `${passed}/${total}` : "n/a"}</strong>
          </div>
          <p>overall_pass: ${phase.overall_pass === true ? "SI" : phase.overall_pass === false ? "NO" : "N/A"}</p>
        </article>
      `;
    })
    .join("");

  const labelByKey = new Map();
  phases.forEach((phase) => {
    (phase.gates || []).forEach((g) => {
      if (!labelByKey.has(g.key) && g.label) {
        labelByKey.set(g.key, g.label);
      }
    });
  });

  const rows = ordered
    .map((key) => {
      const cells = phases
        .map((phase) => {
          const gate = (phase.gates || []).find((g) => g.key === key);
          const val = gate ? gate.pass : null;
          const cls = val === true ? "bool-ok" : val === false ? "bool-bad" : "bool-na";
          const txt = val === true ? "✓" : val === false ? "✗" : "—";
          return `<td class="${cls}">${txt}</td>`;
        })
        .join("");
      return `<tr><th>${escapeHtml(labelByKey.get(key) || humanizeMetricKey(key))}</th>${cells}</tr>`;
    })
    .join("");

  root.innerHTML = `
    <div class="gate-summary-grid">${summaries}</div>
    <div class="numeric-table-wrap">
      <table class="heat-table">
        <thead>
          <tr>
            <th>Compuerta</th>
            ${phases.map((phase) => `<th>${escapeHtml(phase.label)}</th>`).join("")}
          </tr>
        </thead>
        <tbody>
          ${rows}
        </tbody>
      </table>
    </div>
  `;
}

function renderErrors(phases) {
  const root = document.getElementById("case-chart-errors");
  if (!root) return;

  const rows = [
    { label: "RMSE ABM", get: (p) => toNumber(getPath(p, "errors.rmse_abm")) },
    { label: "RMSE ABM sin ODE", get: (p) => toNumber(getPath(p, "errors.rmse_abm_no_ode")) },
    { label: "RMSE ODE", get: (p) => toNumber(getPath(p, "errors.rmse_ode")) },
    { label: "RMSE reducido", get: (p) => toNumber(getPath(p, "errors.rmse_reduced")) },
    { label: "Umbral RMSE", get: (p) => toNumber(getPath(p, "errors.threshold")) },
    {
      label: "RMSE delta (%)",
      get: (p) => toNumber(getPath(p, "errors.rmse_gain")),
      format: (v) => fmtSignedPercent(v),
      signed: true,
      domain: [-1, 1],
    },
  ];

  root.innerHTML = buildNumericTable(phases, rows, {
    showDelta: true,
    deltaLabel: deltaLabel(phases),
  });
}

function renderCorrelations(phases) {
  const root = document.getElementById("case-chart-correlations");
  if (!root) return;

  const rows = [
    { label: "Corr(ABM, obs)", get: (p) => toNumber(getPath(p, "correlations.abm_obs")), domain: [-1, 1], signed: true },
    { label: "Corr(ODE, obs)", get: (p) => toNumber(getPath(p, "correlations.ode_obs")), domain: [-1, 1], signed: true },
    { label: "Symploke CR", get: (p) => toNumber(getPath(p, "symploke.cr")), domain: [0, 2] },
    { label: "Symploke interno", get: (p) => toNumber(getPath(p, "symploke.internal")), domain: [0, 1] },
    { label: "Symploke externo", get: (p) => toNumber(getPath(p, "symploke.external")), domain: [0, 1] },
    { label: "Info efectiva", get: (p) => toNumber(getPath(p, "effective_information")), domain: [0, 1] },
    { label: "C1 corr ABM", get: (p) => toNumber(getPath(p, "details.c1.corr_abm")), domain: [-1, 1], signed: true },
    { label: "C1 corr ODE", get: (p) => toNumber(getPath(p, "details.c1.corr_ode")), domain: [-1, 1], signed: true },
  ];

  root.innerHTML = buildNumericTable(phases, rows, {
    showDelta: true,
    deltaLabel: deltaLabel(phases),
  });
}

function renderCalibration(phases) {
  const root = document.getElementById("case-chart-calibration");
  if (!root) return;

  const rows = [
    { label: "forcing_scale", get: (p) => toNumber(getPath(p, "calibration.forcing_scale")) },
    { label: "macro_coupling", get: (p) => toNumber(getPath(p, "calibration.macro_coupling")), domain: [0, 1] },
    { label: "ode_coupling_strength", get: (p) => toNumber(getPath(p, "calibration.ode_coupling_strength")), domain: [0, 1] },
    { label: "abm_feedback_gamma", get: (p) => toNumber(getPath(p, "calibration.abm_feedback_gamma")) },
    { label: "damping", get: (p) => toNumber(getPath(p, "calibration.damping")), domain: [0, 1.2] },
    { label: "ode_alpha", get: (p) => toNumber(getPath(p, "calibration.ode_alpha")) },
    { label: "ode_beta", get: (p) => toNumber(getPath(p, "calibration.ode_beta")) },
    { label: "assimilation_strength", get: (p) => toNumber(getPath(p, "calibration.assimilation_strength")), domain: [0, 1] },
    { label: "calibration_rmse", get: (p) => toNumber(getPath(p, "calibration.calibration_rmse")) },
    { label: "forcing mean", get: (p) => toNumber(getPath(p, "forcing.mean")) },
    { label: "forcing std", get: (p) => toNumber(getPath(p, "forcing.std")) },
    { label: "forcing min", get: (p) => toNumber(getPath(p, "forcing.min")) },
    { label: "forcing max", get: (p) => toNumber(getPath(p, "forcing.max")) },
    { label: "bias scale_factor", get: (p) => toNumber(getPath(p, "bias_correction.scale_factor")) },
    { label: "bias corr_train", get: (p) => toNumber(getPath(p, "bias_correction.ode_obs_corr_train")), domain: [-1, 1], signed: true },
  ];

  root.innerHTML = buildNumericTable(phases, rows, {
    showDelta: true,
    deltaLabel: deltaLabel(phases),
  });
}

function renderDetails(phases) {
  const root = document.getElementById("case-chart-details");
  if (!root) return;

  const rows = [
    { label: "C1 relative_improvement", get: (p) => toNumber(getPath(p, "details.c1.relative_improvement")), signed: true, domain: [-1, 1], format: (v) => fmtSignedPercent(v) },
    { label: "C1 rmse_abm", get: (p) => toNumber(getPath(p, "details.c1.rmse_abm")) },
    { label: "C1 rmse_ode", get: (p) => toNumber(getPath(p, "details.c1.rmse_ode")) },
    { label: "C1 rmse_reduced", get: (p) => toNumber(getPath(p, "details.c1.rmse_reduced")) },
    { label: "C1 threshold", get: (p) => toNumber(getPath(p, "details.c1.threshold")) },
    { label: "C2 mean_delta", get: (p) => toNumber(getPath(p, "details.c2.mean_delta")), signed: true },
    { label: "C2 var_delta", get: (p) => toNumber(getPath(p, "details.c2.var_delta")), signed: true },
    { label: "C2 relative_mean", get: (p) => toNumber(getPath(p, "details.c2.relative_mean")), signed: true, format: (v) => fmtSignedPercent(v) },
    { label: "C2 relative_var", get: (p) => toNumber(getPath(p, "details.c2.relative_var")), signed: true, format: (v) => fmtSignedPercent(v) },
    { label: "C3 persistence_1", get: (p) => toNumber(getPath(p, "details.c3.persistence_1")) },
    { label: "C3 persistence_2", get: (p) => toNumber(getPath(p, "details.c3.persistence_2")) },
    { label: "C4 diff", get: (p) => toNumber(getPath(p, "details.c4.diff")), signed: true },
    { label: "C5 sensitivity_min", get: (p) => toNumber(getPath(p, "details.c5.sensitivity_min")) },
    { label: "C5 sensitivity_max", get: (p) => toNumber(getPath(p, "details.c5.sensitivity_max")) },
    { label: "C5 range", get: (p) => toNumber(getPath(p, "details.c5.range")) },
    { label: "C5 relative_range", get: (p) => toNumber(getPath(p, "details.c5.relative_range")), format: (v) => fmtSignedPercent(v), signed: true },
  ];

  root.innerHTML = buildNumericTable(phases, rows, {
    showDelta: true,
    deltaLabel: deltaLabel(phases),
  });
}

function renderDynamics(phases) {
  const root = document.getElementById("case-chart-dynamics");
  if (!root) return;

  const rows = [
    { label: "non_locality dominance_share", get: (p) => toNumber(getPath(p, "non_locality.dominance_share")) },
    { label: "persistence std_ratio", get: (p) => toNumber(getPath(p, "persistence.std_ratio")) },
    { label: "persistence model_std", get: (p) => toNumber(getPath(p, "persistence.model_std")) },
    { label: "persistence obs_std", get: (p) => toNumber(getPath(p, "persistence.obs_std")) },
    { label: "noise cv", get: (p) => toNumber(getPath(p, "noise.cv")) },
    { label: "noise edi_std", get: (p) => toNumber(getPath(p, "noise.edi_std")) },
    { label: "noise edi_mean", get: (p) => toNumber(getPath(p, "noise.edi_mean")) },
    { label: "emergence err_abm", get: (p) => toNumber(getPath(p, "emergence.err_abm")) },
    { label: "emergence err_abm_no_ode", get: (p) => toNumber(getPath(p, "emergence.err_abm_no_ode")) },
    { label: "emergence err_reduced", get: (p) => toNumber(getPath(p, "emergence.err_reduced")) },
    { label: "emergence threshold", get: (p) => toNumber(getPath(p, "emergence.threshold")) },
    { label: "viscosity relaxation_time", get: (p) => toNumber(getPath(p, "viscosity.detail.relaxation_time")) },
    { label: "viscosity peak_impact", get: (p) => toNumber(getPath(p, "viscosity.detail.peak_impact")) },
    { label: "data coverage", get: (p) => toNumber(getPath(p, "data.coverage")), domain: [0, 1] },
    { label: "data steps", get: (p) => toNumber(getPath(p, "data.steps")) },
    { label: "data val_steps", get: (p) => toNumber(getPath(p, "data.val_steps")) },
  ];

  root.innerHTML = buildNumericTable(phases, rows, {
    showDelta: true,
    deltaLabel: deltaLabel(phases),
  });
}

function renderChecks(phases) {
  const root = document.getElementById("case-chart-checks");
  if (!root) return;

  const checkMaps = phases.map((phase) => collectChecks(phase));
  const allKeys = new Set();
  checkMaps.forEach((map) => {
    Object.keys(map).forEach((k) => allKeys.add(k));
  });

  if (!allKeys.size) {
    root.innerHTML = '<p class="mini-note">Sin checks booleanos registrados.</p>';
    return;
  }

  const preferred = [
    "overall_pass",
    "edi.significant",
    "edi.valid",
    "criteria.c1_convergence",
    "criteria.c2_robustness",
    "criteria.c3_replication",
    "criteria.c4_validity",
    "criteria.c5_uncertainty",
    "criteria.symploke_pass",
    "criteria.non_locality_pass",
    "criteria.persistence_pass",
    "criteria.emergence_pass",
    "criteria.coupling_ok",
    "criteria.rmse_fraud_check",
    "criteria.edi_valid",
    "criteria.cr_valid",
    "symploke.pass",
    "symploke.cr_valid",
    "non_locality.pass",
    "persistence.pass",
    "emergence.pass",
    "noise.stable",
    "coupling_check",
    "rmse_fraud_check",
    "gated_by_synthetic",
  ];

  const ordered = preferred.filter((k) => allKeys.has(k)).concat(
    [...allKeys].filter((k) => !preferred.includes(k)).sort()
  );

  const taxonomy = phases
    .map((phase) => {
      const cat = getPath(phase, "taxonomy.category") || "n/a";
      const level = getPath(phase, "taxonomy.nivel");
      const interp = getPath(phase, "taxonomy.interpretation") || "";
      return `
        <article class="taxonomy-card">
          <h4 style="color:${phase.color}">${escapeHtml(phase.label)}</h4>
          <p><strong>Categoría:</strong> ${escapeHtml(String(cat))}</p>
          <p><strong>Nivel:</strong> ${level === null || typeof level === "undefined" ? "n/a" : escapeHtml(String(level))}</p>
          <p>${escapeHtml(String(interp || "Sin interpretación textual"))}</p>
        </article>
      `;
    })
    .join("");

  const rows = ordered
    .map((key) => {
      const cells = checkMaps
        .map((map) => {
          const val = map[key];
          const cls = val === true ? "bool-ok" : val === false ? "bool-bad" : "bool-na";
          const txt = val === true ? "✓" : val === false ? "✗" : "—";
          return `<td class="${cls}">${txt}</td>`;
        })
        .join("");
      return `<tr><th>${escapeHtml(humanizeMetricKey(key))}</th>${cells}</tr>`;
    })
    .join("");

  root.innerHTML = `
    <div class="taxonomy-grid">${taxonomy}</div>
    <div class="numeric-table-wrap">
      <table class="heat-table">
        <thead>
          <tr>
            <th>Check</th>
            ${phases.map((phase) => `<th>${escapeHtml(phase.label)}</th>`).join("")}
          </tr>
        </thead>
        <tbody>${rows}</tbody>
      </table>
    </div>
  `;
}

function renderFullTable(phases) {
  const root = document.getElementById("case-chart-table");
  if (!root) return;

  const flatMaps = phases.map((phase) => flattenNumeric(phase));
  const keySet = new Set();
  flatMaps.forEach((map) => {
    Object.keys(map).forEach((k) => keySet.add(k));
  });

  const keys = [...keySet].sort();
  if (!keys.length) {
    root.innerHTML = '<p class="mini-note">No se detectaron métricas numéricas para tabular.</p>';
    return;
  }

  const rows = keys.map((key) => ({
    label: key,
    get: (_phase, idx) => {
      const map = flatMaps[idx] || {};
      return toNumber(map[key]);
    },
    format: (v) => fmtAuto(v),
    signed: key.includes("delta") || key.includes("diff"),
  }));

  root.innerHTML = `
    <p class="mini-note">Cobertura numérica: ${keys.length} métricas detectadas en las fases del caso.</p>
    ${buildNumericTable(phases, rows, {
      showDelta: true,
      deltaLabel: deltaLabel(phases),
      withBars: false,
      metricKeyFormatter: (k) => humanizeMetricKey(k),
    })}
  `;
}

function buildNumericTable(phases, rows, options) {
  const opts = options || {};
  const showDelta = opts.showDelta !== false && phases.length >= 2;
  const deltaLabelText = opts.deltaLabel || "Delta";
  const withBars = opts.withBars !== false;
  const keyFormatter = typeof opts.metricKeyFormatter === "function" ? opts.metricKeyFormatter : (x) => x;

  const preparedRows = rows
    .map((row) => {
      const values = phases.map((phase, idx) => {
        if (typeof row.get === "function") {
          return toNumber(row.get(phase, idx));
        }
        return null;
      });
      const valid = values.filter((v) => typeof v === "number" && Number.isFinite(v));
      if (!valid.length) return null;

      const signed = row.signed === true || valid.some((v) => v < 0);
      const domain = Array.isArray(row.domain) && row.domain.length === 2 ? row.domain : null;

      let min = 0;
      let max = 1;
      if (domain) {
        min = toNumber(domain[0]) ?? 0;
        max = toNumber(domain[1]) ?? 1;
      } else if (signed) {
        const absMax = Math.max(...valid.map((v) => Math.abs(v)), 1e-9);
        min = -absMax;
        max = absMax;
      } else {
        min = 0;
        max = Math.max(...valid, 1e-9);
      }

      return {
        ...row,
        values,
        min,
        max,
        signed,
      };
    })
    .filter(Boolean);

  if (!preparedRows.length) {
    return '<p class="mini-note">Sin métricas numéricas para este bloque.</p>';
  }

  const header = `
    <tr>
      <th class="metric-col">Métrica</th>
      ${phases.map((phase) => `<th>${escapeHtml(phase.label)}</th>`).join("")}
      ${showDelta ? `<th>${escapeHtml(deltaLabelText)}</th>` : ""}
    </tr>
  `;

  const body = preparedRows
    .map((row) => {
      const fmtFn = typeof row.format === "function" ? row.format : (v) => fmt(v);
      const cells = row.values
        .map((value, idx) => numericValueCell(value, {
          min: row.min,
          max: row.max,
          signed: row.signed,
          withBars,
          color: phases[idx].color,
          formatter: fmtFn,
        }))
        .join("");

      let deltaCell = "";
      if (showDelta) {
        const a = row.values[0];
        const b = row.values[1];
        if (typeof a === "number" && typeof b === "number") {
          const delta = a - b;
          const cls = delta > 0 ? "delta-pos" : delta < 0 ? "delta-neg" : "";
          const deltaFmt = typeof row.deltaFormat === "function" ? row.deltaFormat : fmtFn;
          deltaCell = `<td class="${cls}">${escapeHtml(deltaFmt(delta))}</td>`;
        } else {
          deltaCell = '<td class="delta-na">—</td>';
        }
      }

      const metricLabel = keyFormatter(row.label);
      return `<tr><th class="metric-col">${escapeHtml(metricLabel)}</th>${cells}${deltaCell}</tr>`;
    })
    .join("");

  return `
    <div class="numeric-table-wrap">
      <table class="numeric-table">
        <thead>${header}</thead>
        <tbody>${body}</tbody>
      </table>
    </div>
  `;
}

function numericValueCell(value, config) {
  const cfg = config || {};
  const withBars = cfg.withBars !== false;
  const formatter = typeof cfg.formatter === "function" ? cfg.formatter : (v) => fmt(v);

  if (typeof value !== "number" || !Number.isFinite(value)) {
    return `<td><span class="num-na">—</span></td>`;
  }

  const text = escapeHtml(formatter(value));
  if (!withBars) {
    return `<td><span class="num-text" style="position:static;transform:none;display:inline-block">${text}</span></td>`;
  }

  const min = typeof cfg.min === "number" ? cfg.min : 0;
  const max = typeof cfg.max === "number" ? cfg.max : 1;
  const signed = Boolean(cfg.signed);
  const color = cfg.color || "#2f7b73";

  if (signed) {
    const absMax = Math.max(Math.abs(min), Math.abs(max), 1e-9);
    const ratio = Math.min(1, Math.abs(value) / absMax);
    const widthPct = ratio * 50;
    const leftPct = value >= 0 ? 50 : 50 - widthPct;
    const negCls = value < 0 ? "neg" : "";
    return `
      <td>
        <div class="num-bar signed">
          <span class="num-fill ${negCls}" style="left:${leftPct.toFixed(2)}%;width:${widthPct.toFixed(2)}%;background:${value < 0 ? "#b45a4d" : color}"></span>
          <span class="num-text">${text}</span>
        </div>
      </td>
    `;
  }

  const denom = Math.max(1e-9, max - Math.min(0, min));
  const normalized = (value - Math.min(0, min)) / denom;
  const widthPct = Math.max(0, Math.min(100, normalized * 100));

  return `
    <td>
      <div class="num-bar">
        <span class="num-fill" style="left:0;width:${widthPct.toFixed(2)}%;background:${color}"></span>
        <span class="num-text">${text}</span>
      </div>
    </td>
  `;
}

function buildMiniBar(value, domain, signed, color) {
  if (typeof value !== "number" || !Number.isFinite(value)) {
    return '<div class="metric-mini-track is-na"></div>';
  }

  const d = Array.isArray(domain) && domain.length === 2 ? domain : [0, 1];
  const min = toNumber(d[0]) ?? 0;
  const max = toNumber(d[1]) ?? 1;

  if (signed || (min < 0 && max > 0)) {
    const absMax = Math.max(Math.abs(min), Math.abs(max), 1e-9);
    const ratio = Math.min(1, Math.abs(value) / absMax);
    const widthPct = ratio * 50;
    const leftPct = value >= 0 ? 50 : 50 - widthPct;
    const negCls = value < 0 ? "neg" : "";
    return `
      <div class="metric-mini-track signed">
        <span class="metric-mini-fill ${negCls}" style="left:${leftPct.toFixed(2)}%;width:${widthPct.toFixed(2)}%;background:${value < 0 ? "#b45a4d" : color}"></span>
      </div>
    `;
  }

  const denom = Math.max(1e-9, max - min);
  const pct = ((value - min) / denom) * 100;
  return `
    <div class="metric-mini-track">
      <span class="metric-mini-fill" style="left:0;width:${Math.max(0, Math.min(100, pct)).toFixed(2)}%;background:${color}"></span>
    </div>
  `;
}

function collectChecks(phase) {
  const out = {};

  const assign = (key, value) => {
    if (typeof value === "boolean") out[key] = value;
  };

  assign("overall_pass", phase.overall_pass);
  assign("edi.significant", getPath(phase, "edi.significant"));
  assign("edi.valid", getPath(phase, "edi.valid"));
  assign("symploke.pass", getPath(phase, "symploke.pass"));
  assign("symploke.cr_valid", getPath(phase, "symploke.cr_valid"));
  assign("non_locality.pass", getPath(phase, "non_locality.pass"));
  assign("persistence.pass", getPath(phase, "persistence.pass"));
  assign("emergence.pass", getPath(phase, "emergence.pass"));
  assign("noise.stable", getPath(phase, "noise.stable"));
  assign("coupling_check", phase.coupling_check);
  assign("rmse_fraud_check", phase.rmse_fraud_check);
  assign("gated_by_synthetic", phase.gated_by_synthetic);

  const criteriaFull = phase.criteria_full || {};
  Object.keys(criteriaFull).forEach((k) => {
    assign(`criteria.${k}`, criteriaFull[k]);
  });

  return out;
}

function flattenNumeric(obj, prefix, out) {
  const target = out || {};
  const base = prefix || "";
  if (!obj || typeof obj !== "object") return target;

  Object.entries(obj).forEach(([key, value]) => {
    const fullKey = base ? `${base}.${key}` : key;
    if (typeof value === "number" && Number.isFinite(value)) {
      target[fullKey] = value;
      return;
    }
    if (value && typeof value === "object" && !Array.isArray(value)) {
      flattenNumeric(value, fullKey, target);
    }
  });

  return target;
}

function deltaLabel(phases) {
  if (phases.length < 2) return "Delta";
  return `Δ ${phases[0].label} - ${phases[1].label}`;
}

function getPath(obj, path) {
  if (!obj || typeof obj !== "object" || !path) return null;
  return path.split(".").reduce((acc, key) => (acc && typeof acc === "object" ? acc[key] : null), obj);
}

function humanizeMetricKey(key) {
  const mapped = {
    "criteria.c1_convergence": "C1 convergencia",
    "criteria.c2_robustness": "C2 robustez",
    "criteria.c3_replication": "C3 replicación",
    "criteria.c4_validity": "C4 validez",
    "criteria.c5_uncertainty": "C5 incertidumbre",
    "criteria.symploke_pass": "Symploke pass",
    "criteria.non_locality_pass": "No localidad pass",
    "criteria.persistence_pass": "Persistencia pass",
    "criteria.emergence_pass": "Emergencia pass",
    "criteria.coupling_ok": "Acoplamiento OK",
    "criteria.rmse_fraud_check": "Check RMSE-fraud",
    "criteria.edi_valid": "EDI válido",
    "criteria.cr_valid": "CR válido",
  };
  if (mapped[key]) return mapped[key];
  return key
    .replace(/^details\./, "")
    .replace(/\./g, " · ")
    .replace(/_/g, " ");
}

function toNumber(value) {
  return typeof value === "number" && Number.isFinite(value) ? value : null;
}

function fmt(value) {
  if (typeof value !== "number" || !Number.isFinite(value)) return "n/a";
  return value.toFixed(3);
}

function fmtPercent(value) {
  if (typeof value !== "number" || !Number.isFinite(value)) return "n/a";
  return `${(value * 100).toFixed(1)}%`;
}

function fmtSignedPercent(value) {
  if (typeof value !== "number" || !Number.isFinite(value)) return "n/a";
  const pct = value * 100;
  const sign = pct > 0 ? "+" : "";
  return `${sign}${pct.toFixed(1)}%`;
}

function fmtAuto(value) {
  if (typeof value !== "number" || !Number.isFinite(value)) return "n/a";
  const abs = Math.abs(value);
  if (abs >= 1000) return value.toFixed(1);
  if (abs >= 100) return value.toFixed(2);
  if (abs >= 1) return value.toFixed(4);
  if (abs >= 0.01) return value.toFixed(5);
  return value.toExponential(2);
}

function escapeHtml(text) {
  return String(text)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function debounce(fn, wait) {
  let timeout;
  return (...args) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => fn(...args), wait);
  };
}
