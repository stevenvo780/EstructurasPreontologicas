(() => {
  const dataNode = document.getElementById("summary-data");
  if (!dataNode) {
    return;
  }

  let summary;
  try {
    summary = JSON.parse(dataNode.textContent);
  } catch (err) {
    console.error("No se pudo parsear summary-data", err);
    return;
  }

  safeRender("chart-levels", () => renderLevelBars(summary.levels || []));
  safeRender("chart-categories", () => renderCategoryBars(summary.categories || []));
  safeRender("chart-edi-hist", () => renderHistogram(summary.edi_bins || [], "chart-edi-hist"));
  safeRender("chart-cr-hist", () => renderHistogram(summary.cr_bins || [], "chart-cr-hist"));
  safeRender("chart-rmse-hist", () => renderHistogram(summary.rmse_bins || [], "chart-rmse-hist"));
  safeRender("chart-pass-pie", () => renderPassPie(summary.stats || {}));
  safeRender("chart-criteria-rates", () => renderCriteriaRates(summary.criteria_pass_rates || []));
  safeRender("chart-scatter", () => renderScatter(summary.cases || []));
  safeRender("chart-timeline", () => renderTimeline(summary.timeline || []));
  safeRender("chart-heatmap", () => renderCriteriaHeatmap(summary.criteria_order || [], summary.cases || []));
  safeRender("chart-graph", () => renderCategoryGraph(summary.categories || [], summary.cases || []));

  window.addEventListener("resize", () => {
    safeRender("chart-scatter", () => renderScatter(summary.cases || []));
    safeRender("chart-timeline", () => renderTimeline(summary.timeline || []));
    safeRender("chart-graph", () => renderCategoryGraph(summary.categories || [], summary.cases || []));
  });
})();

function safeRender(rootId, fn) {
  try {
    fn();
  } catch (err) {
    console.error(`Error renderizando ${rootId}`, err);
    const root = document.getElementById(rootId);
    if (root) {
      root.innerHTML = '<p style="margin:0;color:#8d2f26;font-size:0.85rem;">No se pudo renderizar este gráfico.</p>';
    }
  }
}

function renderLevelBars(levels) {
  const root = document.getElementById("chart-levels");
  if (!root) return;
  if (!levels.length) {
    root.textContent = "Sin datos";
    return;
  }

  const max = Math.max(...levels.map((x) => x.count || 0), 1);
  root.innerHTML = `<div class="bar-list">${levels
    .map((row) => {
      const pct = ((row.count || 0) / max) * 100;
      return `
        <div class="bar-row">
          <span>${escapeHtml(row.label)}</span>
          <div class="bar-track"><div class="bar-fill" style="width:${pct.toFixed(1)}%"></div></div>
          <strong>${row.count || 0}</strong>
        </div>
      `;
    })
    .join("")}</div>`;
}

function renderCategoryBars(categories) {
  const root = document.getElementById("chart-categories");
  if (!root) return;
  if (!categories.length) {
    root.textContent = "Sin datos";
    return;
  }

  const max = Math.max(...categories.map((x) => x.count || 0), 1);
  root.innerHTML = `<div class="bar-list">${categories
    .map((row) => {
      const pct = ((row.count || 0) / max) * 100;
      return `
        <div class="bar-row">
          <span>${escapeHtml(row.category)}</span>
          <div class="bar-track"><div class="bar-fill" style="width:${pct.toFixed(1)}%"></div></div>
          <strong>${row.count || 0}</strong>
        </div>
      `;
    })
    .join("")}</div>`;
}

function renderHistogram(bins, targetId) {
  const root = document.getElementById(targetId);
  if (!root) return;
  if (!bins.length) {
    root.textContent = "Sin datos";
    return;
  }

  const max = Math.max(...bins.map((x) => x.count || 0), 1);
  root.innerHTML = `<div class="bar-list">${bins
    .map((row) => {
      const pct = ((row.count || 0) / max) * 100;
      return `
        <div class="bar-row">
          <span>${escapeHtml(row.label)}</span>
          <div class="bar-track"><div class="bar-fill" style="width:${pct.toFixed(1)}%"></div></div>
          <strong>${row.count || 0}</strong>
        </div>
      `;
    })
    .join("")}</div>`;
}

function renderPassPie(stats) {
  const root = document.getElementById("chart-pass-pie");
  if (!root) return;
  const pass = stats.overall_pass || 0;
  const total = stats.total_cases || 1;
  const fail = total - pass;
  const pctPass = (pass / total) * 100;
  const pctFail = (fail / total) * 100;
  
  root.innerHTML = `
    <div class="bar-list" style="margin-top: 1rem;">
      <div class="bar-row">
        <span>Aprobados (Pass)</span>
        <div class="bar-track"><div class="bar-fill" style="width:${pctPass.toFixed(1)}%; background: #2a8f67;"></div></div>
        <strong>${pass}</strong>
      </div>
      <div class="bar-row">
        <span>Fallidos (Fail)</span>
        <div class="bar-track"><div class="bar-fill" style="width:${pctFail.toFixed(1)}%; background: #b3473b;"></div></div>
        <strong>${fail}</strong>
      </div>
    </div>
  `;
}

function renderCriteriaRates(rates) {
  const root = document.getElementById("chart-criteria-rates");
  if (!root) return;
  if (!rates.length) {
    root.textContent = "Sin datos";
    return;
  }

  root.innerHTML = `<div class="bar-list">${rates
    .map((row) => {
      const rate = typeof row.rate === "number" ? row.rate : 0;
      const pct = rate * 100;
      return `
        <div class="bar-row">
          <span>${escapeHtml(row.label)}</span>
          <div class="bar-track"><div class="bar-fill" style="width:${pct.toFixed(1)}%"></div></div>
          <strong>${pct.toFixed(0)}%</strong>
        </div>
      `;
    })
    .join("")}</div>`;
}

function renderScatter(cases) {
  const root = document.getElementById("chart-scatter");
  if (!root) return;

  const points = cases.filter(
    (c) => typeof c.edi === "number" && Number.isFinite(c.edi) && typeof c.cr === "number" && Number.isFinite(c.cr)
  );
  if (!points.length) {
    root.textContent = "Sin puntos válidos para graficar";
    return;
  }

  const width = Math.max(520, root.clientWidth || 520);
  const height = 320;
  const pad = { l: 54, r: 16, t: 16, b: 42 };

  const xMinRaw = Math.min(...points.map((p) => p.edi));
  const xMaxRaw = Math.max(...points.map((p) => p.edi));
  const yMinRaw = Math.min(...points.map((p) => p.cr));
  const yMaxRaw = Math.max(...points.map((p) => p.cr));

  const xMin = Math.min(-1, xMinRaw - 0.05);
  const xMax = Math.max(1, xMaxRaw + 0.05);
  const yMin = Math.max(0, yMinRaw - 0.05);
  const yMax = yMaxRaw + 0.08;

  const xScale = (x) => pad.l + ((x - xMin) / (xMax - xMin)) * (width - pad.l - pad.r);
  const yScale = (y) => height - pad.b - ((y - yMin) / (yMax - yMin)) * (height - pad.t - pad.b);

  const circles = points
    .map((p) => {
      const color = p.overall_pass ? "#2a8f67" : "#b3473b";
      const cx = xScale(p.edi).toFixed(2);
      const cy = yScale(p.cr).toFixed(2);
      const label = `${p.case_name} | EDI=${fmt(p.edi)} | CR=${fmt(p.cr)}`;
      return `<circle cx="${cx}" cy="${cy}" r="4.3" fill="${color}" fill-opacity="0.88"><title>${escapeHtml(label)}</title></circle>`;
    })
    .join("");

  const xTicks = [-1, -0.5, 0, 0.5, 1]
    .map(
      (v) =>
        `<g><line x1="${xScale(v)}" y1="${height - pad.b}" x2="${xScale(v)}" y2="${height - pad.b + 5}" stroke="#49585c"/>` +
        `<text x="${xScale(v)}" y="${height - pad.b + 18}" text-anchor="middle" font-size="11" fill="#425356">${v.toFixed(
          1
        )}</text></g>`
    )
    .join("");

  const yTicks = [0, 0.5, 1, 1.5, 2]
    .map((v) => {
      const y = yScale(v);
      return `<g><line x1="${pad.l - 5}" y1="${y}" x2="${pad.l}" y2="${y}" stroke="#49585c"/>` +
        `<text x="${pad.l - 9}" y="${y + 4}" text-anchor="end" font-size="11" fill="#425356">${v.toFixed(1)}</text></g>`;
    })
    .join("");

  root.innerHTML = `
    <div class="scatter-wrap">
      <svg width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" role="img" aria-label="Dispersión EDI vs CR">
        <rect x="0" y="0" width="${width}" height="${height}" fill="#fffaf5" />
        <line x1="${pad.l}" y1="${height - pad.b}" x2="${width - pad.r}" y2="${height - pad.b}" stroke="#49585c" stroke-width="1" />
        <line x1="${pad.l}" y1="${pad.t}" x2="${pad.l}" y2="${height - pad.b}" stroke="#49585c" stroke-width="1" />
        ${xTicks}
        ${yTicks}
        <line x1="${xScale(0)}" y1="${pad.t}" x2="${xScale(0)}" y2="${height - pad.b}" stroke="#d6c4b2" stroke-dasharray="4 3" />
        ${circles}
        <text x="${(width + pad.l) / 2}" y="${height - 6}" text-anchor="middle" font-size="12" fill="#24373c">EDI</text>
        <text x="16" y="${height / 2}" transform="rotate(-90, 16, ${height / 2})" text-anchor="middle" font-size="12" fill="#24373c">CR</text>
      </svg>
    </div>
  `;
}

function renderTimeline(series) {
  const root = document.getElementById("chart-timeline");
  if (!root) return;

  const points = [...series]
    .filter((x) => typeof x.case_num === "number")
    .sort((a, b) => a.case_num - b.case_num);

  const validEdi = points.filter((x) => typeof x.edi === "number" && Number.isFinite(x.edi));
  if (!validEdi.length) {
    root.textContent = "Sin datos";
    return;
  }

  const width = Math.max(760, root.clientWidth || 760);
  const height = 290;
  const pad = { l: 50, r: 16, t: 16, b: 42 };

  const xMin = Math.min(...points.map((p) => p.case_num));
  const xMax = Math.max(...points.map((p) => p.case_num));
  const yMin = Math.min(-1, Math.min(...validEdi.map((p) => p.edi)) - 0.05);
  const yMax = Math.max(1, Math.max(...validEdi.map((p) => p.edi)) + 0.05);

  const xScale = (x) => pad.l + ((x - xMin) / Math.max(1, xMax - xMin)) * (width - pad.l - pad.r);
  const yScale = (y) => height - pad.b - ((y - yMin) / Math.max(0.0001, yMax - yMin)) * (height - pad.t - pad.b);

  const ediPath = validEdi
    .map((p, idx) => `${idx === 0 ? "M" : "L"} ${xScale(p.case_num).toFixed(2)} ${yScale(p.edi).toFixed(2)}`)
    .join(" ");

  const ediDots = validEdi
    .map((p) => {
      const cx = xScale(p.case_num).toFixed(2);
      const cy = yScale(p.edi).toFixed(2);
      const label = `${p.case_name} | EDI=${fmt(p.edi)} | RMSEΔ=${typeof p.rmse_reduction === "number" ? (p.rmse_reduction * 100).toFixed(1) + "%" : "n/a"}`;
      return `<circle cx="${cx}" cy="${cy}" r="3.8" fill="#2f7b73"><title>${escapeHtml(label)}</title></circle>`;
    })
    .join("");

  const rmseValues = points.filter((x) => typeof x.rmse_reduction === "number" && Number.isFinite(x.rmse_reduction));
  const rmseDots = rmseValues
    .map((p) => {
      const x = xScale(p.case_num);
      const y = (height - pad.b) - (Math.max(0, p.rmse_reduction) * (height - pad.t - pad.b));
      return `<rect x="${(x - 2.4).toFixed(2)}" y="${y.toFixed(2)}" width="4.8" height="4.8" fill="#ca6d2f"><title>RMSEΔ ${p.case_name}: ${(p.rmse_reduction * 100).toFixed(1)}%</title></rect>`;
    })
    .join("");

  const xTicks = points
    .filter((p) => p.case_num % 2 === 1)
    .map((p) => {
      const x = xScale(p.case_num);
      return `<g><line x1="${x}" y1="${height - pad.b}" x2="${x}" y2="${height - pad.b + 4}" stroke="#49585c"/>` +
        `<text x="${x}" y="${height - pad.b + 16}" text-anchor="middle" font-size="10" fill="#425356">${String(p.case_num).padStart(2, "0")}</text></g>`;
    })
    .join("");

  root.innerHTML = `
    <div class="scatter-wrap">
      <svg width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" role="img" aria-label="Serie EDI por caso">
        <rect x="0" y="0" width="${width}" height="${height}" fill="#fffaf5" />
        <line x1="${pad.l}" y1="${height - pad.b}" x2="${width - pad.r}" y2="${height - pad.b}" stroke="#49585c" />
        <line x1="${pad.l}" y1="${pad.t}" x2="${pad.l}" y2="${height - pad.b}" stroke="#49585c" />
        <line x1="${pad.l}" y1="${yScale(0)}" x2="${width - pad.r}" y2="${yScale(0)}" stroke="#dacbb8" stroke-dasharray="4 3" />
        ${xTicks}
        <path d="${ediPath}" fill="none" stroke="#2f7b73" stroke-width="2" />
        ${ediDots}
        ${rmseDots}
        <text x="${(width + pad.l) / 2}" y="${height - 6}" text-anchor="middle" font-size="12" fill="#24373c">Número de caso</text>
        <text x="14" y="${height / 2}" transform="rotate(-90, 14, ${height / 2})" text-anchor="middle" font-size="12" fill="#24373c">EDI</text>
        <text x="${width - 180}" y="18" font-size="11" fill="#2f7b73">● EDI</text>
        <text x="${width - 120}" y="18" font-size="11" fill="#ca6d2f">■ RMSEΔ</text>
      </svg>
    </div>
  `;
}

function renderCriteriaHeatmap(order, cases) {
  const root = document.getElementById("chart-heatmap");
  if (!root) return;
  if (!order.length || !cases.length) {
    root.textContent = "Sin datos";
    return;
  }

  const labels = {
    c1: "C1",
    c2: "C2",
    c3: "C3",
    c4: "C4",
    c5: "C5",
    sym: "Sym",
    non_local: "NoLocal",
    persist: "Persist",
    coupling: "Coupling",
  };

  const rows = [...cases]
    .sort((a, b) => (a.case_num || 0) - (b.case_num || 0))
    .map((c) => {
      const cells = order
        .map((k) => {
          const value = c.criteria?.[k];
          const cls = value === true ? "cell-ok" : value === false ? "cell-bad" : "cell-na";
          const char = value === true ? "✓" : value === false ? "✗" : "—";
          return `<td class="${cls}">${char}</td>`;
        })
        .join("");
      return `<tr><th>${escapeHtml(c.case_name)}</th>${cells}</tr>`;
    })
    .join("");

  root.innerHTML = `
    <table class="heat-table">
      <thead>
        <tr>
          <th>Caso</th>
          ${order.map((k) => `<th>${labels[k] || k}</th>`).join("")}
        </tr>
      </thead>
      <tbody>
        ${rows}
      </tbody>
    </table>
  `;
}

function renderCategoryGraph(categories, cases) {
  const root = document.getElementById("chart-graph");
  if (!root) return;

  const categoryList = (categories || []).map((c) => c.category).filter(Boolean);
  if (!categoryList.length || !cases.length) {
    root.textContent = "Sin datos";
    return;
  }

  const width = Math.max(780, root.clientWidth || 780);
  const leftX = 180;
  const rightX = width - 220;
  const topPad = 26;
  const rowGap = 24;

  const sortedCases = [...cases].sort((a, b) => (a.case_num || 0) - (b.case_num || 0));
  const height = Math.max(280, topPad * 2 + Math.max(categoryList.length, sortedCases.length) * rowGap + 20);

  const categoryY = new Map();
  categoryList.forEach((cat, i) => categoryY.set(cat, topPad + i * rowGap));

  const caseY = new Map();
  sortedCases.forEach((c, i) => caseY.set(c.case_name, topPad + i * rowGap));

  const palette = ["#2f7b73", "#ca6d2f", "#315a8f", "#8f4f7c", "#7c8a2f", "#8c3a3a", "#5b5b9f"];
  const colorByCat = new Map(categoryList.map((c, i) => [c, palette[i % palette.length]]));

  const lines = sortedCases
    .map((c) => {
      const cat = c.category || "unknown";
      const y1 = categoryY.get(cat);
      const y2 = caseY.get(c.case_name);
      if (typeof y1 !== "number" || typeof y2 !== "number") return "";
      const color = colorByCat.get(cat) || "#888";
      return `<path d="M ${leftX + 8} ${y1} C ${(leftX + rightX) / 2} ${y1}, ${(leftX + rightX) / 2} ${y2}, ${rightX - 8} ${y2}" stroke="${color}" stroke-opacity="0.35" fill="none" />`;
    })
    .join("");

  const categoryNodes = categoryList
    .map((cat) => {
      const y = categoryY.get(cat);
      const color = colorByCat.get(cat) || "#666";
      return `
        <circle cx="${leftX}" cy="${y}" r="6" fill="${color}" />
        <text x="${leftX - 12}" y="${y + 4}" text-anchor="end" font-size="11" fill="#24373c">${escapeHtml(cat)}</text>
      `;
    })
    .join("");

  const caseNodes = sortedCases
    .map((c) => {
      const y = caseY.get(c.case_name);
      const color = c.overall_pass ? "#2a8f67" : "#b3473b";
      const shortName = `${String(c.case_num).padStart(2, "0")}`;
      return `
        <circle cx="${rightX}" cy="${y}" r="4.5" fill="${color}"><title>${escapeHtml(c.case_name)}</title></circle>
        <text x="${rightX + 10}" y="${y + 4}" text-anchor="start" font-size="10.5" fill="#24373c">${shortName}</text>
      `;
    })
    .join("");

  root.innerHTML = `
    <div class="graph-wrap">
      <svg width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" role="img" aria-label="Grafo caso-categoría">
        <rect width="${width}" height="${height}" fill="#fffaf5" />
        ${lines}
        ${categoryNodes}
        ${caseNodes}
      </svg>
    </div>
  `;
}

function fmt(v) {
  return typeof v === "number" ? v.toFixed(3) : "n/a";
}

function escapeHtml(text) {
  return String(text)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/\"/g, "&quot;")
    .replace(/'/g, "&#039;");
}
