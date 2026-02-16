# 2. Stability Bubble Plot (Improved)
plt.figure(figsize=(10, 8))

# Create stability groups
df['stability'] = pd.cut(df['sigma'],
                        bins=[0, 0.1, 0.3, 1],
                        labels=['High Stability', 'Moderate Stability', 'Low Stability'])

# Color map for stability groups
stability_colors = {'High Stability': '#4daf4a', 
                    'Moderate Stability': '#ff7f00', 
                    'Low Stability': '#e41a1c'}

scatter = plt.scatter(
    df["median"],
    df["sigma"],
    s=np.log(df["total"]) * 45,
    c=df['stability'].map(stability_colors),
    alpha=0.8,
    edgecolor="k",
    linewidth=0.5
)

# Add manual legend for stability
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', label='High Stability (σ < 0.1)',
               markerfacecolor='#4daf4a', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='Moderate Stability (0.1 ≤ σ ≤ 0.3)',
               markerfacecolor='#ff7f00', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='Low Stability (σ > 0.3)',
               markerfacecolor='#e41a1c', markersize=10)
]

# Annotate points with offset
for i, row in df.iterrows():
    plt.annotate(
        row["Id"].split("_")[0],
        (row["median"], row["sigma"]),
        xytext=(10, 5),  # Increased x-offset
        textcoords="offset points",
        fontsize=9,
        alpha=0.9,
        arrowprops=dict(arrowstyle="-", alpha=0.3)
    )

# Formatting
plt.xlabel("Median TCWV (cm)", fontsize=12)
plt.ylabel("Sigma (Variability)", fontsize=12)
plt.title("Lithology Stability Classification", fontsize=14)
plt.grid(alpha=0.2)
plt.legend(handles=legend_elements, title="Stability Groups")
plt.tight_layout()
plt.savefig("lithology_stability_v2.png", dpi=300)
