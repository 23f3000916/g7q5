import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def generate_chart():
    """
    Generates and saves a professional Seaborn barplot visualizing
    customer satisfaction scores across different product categories,
    adhering to specific export dimensions and styling.
    """
    # 1. Generate realistic synthetic data for product performance insights
    # A dictionary is created to hold the data, which is then loaded into a pandas DataFrame.
    data = {
        'Product Category': ['Electronics', 'Apparel', 'Home & Garden', 'Books & Media', 'Sporting Goods', 'Health & Beauty'],
        'Average Satisfaction Score': [4.3, 3.6, 4.1, 4.6, 4.0, 4.4],
    }
    df = pd.DataFrame(data)
    # Sorting the data makes the chart easier to interpret.
    df = df.sort_values('Average Satisfaction Score', ascending=False)

    # 2. Apply professional styling using Seaborn best practices
    # 'whitegrid' provides a clean, professional background.
    sns.set_style("whitegrid")
    # 'talk' context increases font sizes for better readability in presentations.
    sns.set_context("talk")

    # 3. Create the barplot
    # Set the figure size. An 8x8 inch figure with a DPI of 64 results in a 512x512 pixel image.
    plt.figure(figsize=(8, 8))

    # Create the barplot using sns.barplot() as specified.
    # The 'viridis' palette is colorblind-friendly and professional.
    barplot = sns.barplot(
        x='Average Satisfaction Score',
        y='Product Category',
        data=df,
        palette='viridis'
    )

    # 4. Style the chart with appropriate titles, labels, and colors
    plt.title('Average Customer Satisfaction by Product Category', fontsize=18, weight='bold', pad=20)
    plt.xlabel('Average Satisfaction Score (out of 5)', fontsize=14)
    plt.ylabel('Product Category', fontsize=14)

    # Set x-axis limits for better context (scores are out of 5).
    plt.xlim(0, 5)

    # Add data labels to each bar for clarity.
    for p in barplot.patches:
        width = p.get_width()
        plt.text(width + 0.05, p.get_y() + p.get_height() / 2.,
                 f'{width:.1f}',
                 va='center')

    # 5. Export the chart to the specified dimensions
    # Ensure all elements fit neatly within the saved figure.
    plt.tight_layout()
    # Save the figure. dpi=64 on an 8x8 figure creates a 512x512 pixel image.
    # bbox_inches='tight' removes any excess whitespace.
    plt.savefig('chart.png', dpi=64, bbox_inches='tight')

    print("Chart 'chart.png' (512x512) has been successfully generated.")

if __name__ == '__main__':
    generate_chart()
