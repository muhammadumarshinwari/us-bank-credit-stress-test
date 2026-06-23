"""Standalone coefficient chart for the README — bars + 95% CIs."""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from stresskit import SatelliteNPLModel
from stresskit.style import apply_style

apply_style()

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"

panel = pd.read_csv(DATA_DIR / "regression_panel.csv", parse_dates=["date"])
model = SatelliteNPLModel().fit(panel)

# pull macro coefficients only (ignore bank fixed-effect dummies)
keep = ["npl_lag1", "real_gdp_growth_lag2", "unemployment", "mortgage_rate_lag1"]
coefs   = model.result.params[keep]
ses     = model.result.bse[keep]
ci_low  = coefs - 1.96 * ses
ci_high = coefs + 1.96 * ses

labels = {
    "npl_lag1":              "NPL (lag 1)",
    "real_gdp_growth_lag2":  "Real GDP growth (lag 2)",
    "unemployment":          "Unemployment",
    "mortgage_rate_lag1":    "30Y mortgage rate (lag 1)",
}
y_labels = [labels[v] for v in keep]
y_pos    = np.arange(len(keep))

# Color by sign: positive = navy, negative = burgundy
colors = ["#1f3a5f" if c >= 0 else "#a3324d" for c in coefs.values]

fig, ax = plt.subplots(figsize=(10.5, 4.8))

# Horizontal bars
bars = ax.barh(
    y_pos, coefs.values,
    color=colors, alpha=0.85,
    edgecolor="white", linewidth=1.2,
    zorder=3,
)

# 95% confidence interval whiskers
for i, (lo, hi, c) in enumerate(zip(ci_low.values, ci_high.values, coefs.values)):
    ax.plot([lo, hi], [i, i], color="#333333", lw=1.4, zorder=4)
    ax.plot([lo, lo], [i - 0.12, i + 0.12], color="#333333", lw=1.4, zorder=4)
    ax.plot([hi, hi], [i - 0.12, i + 0.12], color="#333333", lw=1.4, zorder=4)
    # value label outside the bar
    offset = 0.02 if c >= 0 else -0.02
    ha = "left" if c >= 0 else "right"
    ax.text(c + offset, i, f"{c:+.3f}", va="center", ha=ha,
            fontsize=10, fontweight="bold", color="#222222")

ax.axvline(0, color="#444444", lw=1.0, zorder=2)
ax.set_yticks(y_pos)
ax.set_yticklabels(y_labels)
ax.invert_yaxis()
ax.set_xlabel("Coefficient (with 95% confidence interval)")
ax.set_title("Satellite Model — Estimated Coefficients", loc="left", pad=14)

# subtle x-axis grid only
ax.grid(True, axis="x", color="#e8e8e8", lw=0.7, zorder=1)
ax.grid(False, axis="y")

# expand x-limits a bit so labels never clip
xmin = min(ci_low.min(), 0) - 0.1
xmax = max(ci_high.max(), 0) + 0.15
ax.set_xlim(xmin, xmax)

# Legend chip below
fig.text(
    0.5, -0.02,
    f"N = {int(model.result.nobs):,} bank-quarters    |    "
    f"R-squared = {model.result.rsquared:.3f}    |    "
    f"Estimator: pooled OLS with bank fixed effects, HC1 robust SEs",
    ha="center", fontsize=9, color="#555555",
)

fig.tight_layout()
out = DOCS_DIR / "coefficient_estimates.png"
fig.savefig(out)
print(f"Saved: {out}")
