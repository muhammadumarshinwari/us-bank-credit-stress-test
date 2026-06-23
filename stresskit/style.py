"""
Shared matplotlib style for all charts. Import once at the top of any
plotting script:

    from stresskit.style import apply_style, BANK_COLORS
    apply_style()
"""

import matplotlib.pyplot as plt
import matplotlib as mpl


# A muted, professional palette (works on white and dark backgrounds)
PALETTE = [
    "#1f3a5f",  # deep navy
    "#c47b3b",  # warm copper
    "#5a8a72",  # sage green
    "#a3324d",  # muted burgundy
    "#7d6b9e",  # dusty purple
    "#3a6a8b",  # steel blue
    "#b39449",  # antique gold
    "#6a8caf",  # soft slate
    "#8a4f4f",  # brick
    "#4d7066",  # forest
]

# Bank-specific assignments (consistent colors across all charts)
BANK_COLORS = {
    "JPMorgan Chase Bank NA": "#1f3a5f",
    "Bank of America NA":     "#c47b3b",
    "Wells Fargo Bank NA":    "#5a8a72",
    "Citibank NA":            "#a3324d",
    "U.S. Bank NA":           "#7d6b9e",
    "PNC Bank NA":            "#3a6a8b",
    "Truist Bank":            "#b39449",
    "Fifth Third Bank NA":    "#6a8caf",
    "KeyBank NA":             "#8a4f4f",
    "Regions Bank":           "#4d7066",
}


def apply_style():
    """Apply the shared chart style globally."""
    mpl.rcParams.update({
        # Fonts
        "font.family":          "DejaVu Sans",
        "font.size":            10.5,
        "axes.titlesize":       12,
        "axes.titleweight":     "bold",
        "axes.labelsize":       10.5,
        "axes.labelweight":     "regular",
        "xtick.labelsize":      9.5,
        "ytick.labelsize":      9.5,
        "legend.fontsize":      9.5,
        "figure.titlesize":     13,
        "figure.titleweight":   "bold",

        # Figure
        "figure.facecolor":     "white",
        "axes.facecolor":       "white",
        "savefig.facecolor":    "white",
        "savefig.dpi":          150,
        "figure.dpi":           110,
        "savefig.bbox":         "tight",
        "savefig.pad_inches":   0.25,

        # Axes
        "axes.edgecolor":       "#cccccc",
        "axes.linewidth":       0.8,
        "axes.spines.top":      False,
        "axes.spines.right":    False,
        "axes.titlepad":        12,
        "axes.labelpad":        6,
        "axes.prop_cycle":      mpl.cycler(color=PALETTE),

        # Grid (subtle horizontal only)
        "axes.grid":            True,
        "axes.grid.axis":       "y",
        "grid.color":           "#e8e8e8",
        "grid.linestyle":       "-",
        "grid.linewidth":       0.7,
        "axes.axisbelow":       True,

        # Ticks
        "xtick.color":          "#444444",
        "ytick.color":          "#444444",
        "xtick.direction":      "out",
        "ytick.direction":      "out",
        "xtick.major.size":     3,
        "ytick.major.size":     3,

        # Lines
        "lines.linewidth":      1.8,
        "lines.markersize":     5,

        # Legend
        "legend.frameon":       False,
        "legend.loc":           "best",

        # Spacing
        "figure.autolayout":    False,
    })
