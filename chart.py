import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style and context for professional visuals
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic data for product performance
np.random.seed(42)
products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
sales = np.random.randint(80, 200, size=len(products))
profit_margin = np.random.uniform(0.1, 0.4, size=len(products))

# Create DataFrame
data = pd.DataFrame({
    "Product": products,
    "Sales": sales,
    "Profit Margin": profit_margin
})

# Create barplot
plt.figure(figsize=(8, 8))  # 8x8 inches → 512x512 px at 64 dpi
barplot = sns.barplot(
    data=data,
    x="Product",
    y="Sales",
    palette="viridis"
)

# Add title and labels
plt.title("Product Sales Performance", fontsize=18, weight="bold")
plt.xlabel("Product", fontsize=14)
plt.ylabel("Sales (Units)", fontsize=14)

# Annotate bars with sales values
for p in barplot.patches:
    barplot.annotate(
        format(p.get_height(), '.0f'),
        (p.get_x() + p.get_width() / 2., p.get_height()),
        ha='center', va='center',
        xytext=(0, 8),
        textcoords='offset points',
        fontsize=12, weight="bold"
    )

# Save chart as PNG (512x512 px)
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
