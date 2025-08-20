import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set professional style and context
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate realistic synthetic data for customer spending behavior
# Your email: 24f1001831@ds.study.iitm.ac.in
np.random.seed(42)
segments = ["Segment A", "Segment B", "Segment C", "Segment D"]
data = []
for segment in segments:
    for _ in range(200):
        if segment == "Segment A":
            purchase = np.random.normal(50, 15)
        elif segment == "Segment B":
            purchase = np.random.normal(80, 20)
        elif segment == "Segment C":
            purchase = np.random.normal(60, 10)
        else:
            purchase = np.random.normal(120, 25)
        data.append({"Segment": segment, "Purchase_Amount": max(0, purchase)})

df = pd.DataFrame(data)

# Create the boxplot
plt.figure(figsize=(8, 8))
sns.boxplot(x="Segment", y="Purchase_Amount", data=df, palette="viridis")

# Add titles and labels
plt.title("Purchase Amount Distribution by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Purchase Amount ($)")

# Save the chart as a PNG file with exact 512x512 pixel dimensions
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
