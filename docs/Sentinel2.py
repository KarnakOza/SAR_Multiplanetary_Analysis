TCWV data analysis


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Your data
data = [
    ["opaque_clouds", 13.2563, 15.3527, 13.1711, 13.0849, 13.2664, 13.3095, 0.4073, 320453],
    ["partially_corrected_crosstalk_B11", 14.1169, 14.5698, 14.14, 13.544, 14.4846, 14.5257, 0.2846, 12829],
    ["scl_cloud_high_proba", 14.7573, 15.7119, 15.0179, 13.0632, 15.6377, 15.6616, 0.858, 65774],
    ["scl_cloud_medium_proba", 14.1156, 15.6981, 14.3136, 13.061, 15.0468, 15.2472, 0.8135, 622544],
    ["scl_cloud_shadow", 13.124, 13.7471, 13.0808, 13.0794, 13.0895, 13.7438, 0.1631, 186],
    ["scl_nodata", 15.7058, 16.351, 15.7137, 15.0094, 16.0693, 16.1524, 0.2746, 598059],
    ["scl_not_vegetated", 13.7316, 15.6527, 13.5361, 13.0524, 14.6308, 14.8778, 0.5777, 21944401],
    ["scl_topographic_and_casted_shadows", 14.1539, 14.98, 14.2629, 13.6345, 14.4849, 14.5266, 0.3001, 15354],
    ["scl_unclassified", 14.2962, 15.5851, 14.0141, 13.0635, 15.5372, 15.5523, 0.9852, 6690],
    ["scl_vegetation", 13.4488, 14.9465, 13.2265, 13.1089, 13.9211, 14.1582, 0.3951, 599873],
    ["scl_water", 13.7273, 15.3355, 13.6438, 13.0556, 14.4486, 14.6948, 0.5131, 4885952],
    ["snow_and_ice_areas", 14.0421, 15.4378, 14.1479, 13.0882, 15.0266, 15.1088, 0.7823, 949214]
]

df = pd.DataFrame(data, columns=[
    "Id", "average", "maximum", "median", "minimum", 
    "p90_threshold", "p95_threshold", "sigma", "total"
])

# Sort by median TCWV
df = df.sort_values("median", ascending=False)

# 1. Range Plot for Distribution Analysis
plt.figure(figsize=(14, 10))
y_pos = np.arange(len(df))

# Full range (min to max)
plt.hlines(y_pos, df["minimum"], df["maximum"], 
           color="lightgray", linewidth=4, alpha=0.7, label="Full Range")

# Critical threshold range (p90 to p95)
plt.hlines(y_pos, df["p90_threshold"], df["p95_threshold"], 
           color="gold", linewidth=8, label="p90-p95 Range")

# Median markers
plt.scatter(df["median"], y_pos, s=120, color="red", zorder=5, label="Median")

# Critical thresholds
plt.axvline(x=14.0, color="blue", linestyle="--", alpha=0.7, label="14.0 cm Threshold")
plt.axvline(x=15.5, color="purple", linestyle="--", alpha=0.7, label="15.5 cm Threshold")

# Formatting
plt.yticks(y_pos, df["Id"], fontsize=9)
plt.xlabel("TCWV (cm)", fontsize=12)
plt.title("TCWV Distribution Across Atmospheric and Surface Classes", fontsize=14)
plt.grid(axis="x", linestyle="--", alpha=0.3)
plt.legend(loc="lower right")
plt.xlim(12.5, 16.5)
plt.tight_layout()
plt.savefig("tcwv_distribution.png", dpi=300)

# 2. Sigma vs. Median Bubble Plot
plt.figure(figsize=(12, 8))
scatter = plt.scatter(
    df["median"],
    df["sigma"],
    s=np.log(df["total"])*50,  # Scale by log(total)
    c=df["median"],
    cmap="coolwarm",
    alpha=0.7
)

# Annotations
for i, row in df.iterrows():
    plt.annotate(
        row["Id"], 
        (row["median"], row["sigma"]),
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=8
    )

# Formatting
plt.colorbar(scatter, label="Median TCWV (cm)")
plt.xlabel("Median TCWV (cm)", fontsize=12)
plt.ylabel("Sigma (Variability)", fontsize=12)
plt.title("TCWV Stability Analysis: Variability vs Central Tendency", fontsize=14)
plt.grid(alpha=0.2)
plt.tight_layout()
plt.savefig("tcwv_variability.png", dpi=300)
