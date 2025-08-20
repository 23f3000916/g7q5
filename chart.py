import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def generate_chart():
    """
    Generates and saves a professional Seaborn barplot visualizing
    customer satisfaction scores across different product categories.
    """
    # 1. Generate realistic synthetic data
    # Create a dictionary with product categories and their average satisfaction scores.
    # Scores are generated randomly to simulate real-world variance.
    data = {
        'Product Category': ['Electronics', 'Apparel', 'Home & Garden', 'Books & Media', 'Sporting Goods', 'Health & Beauty'],
        'Average Satisfaction Score': [4.2 + np.random.randn()*0.1 for _ in range(6)],
    }
    # Add some variance to the scores
    data['Average Satisfaction Score'][1] -= 0.5 # Lower score for Apparel
    data['Average Satisfaction Score'][3] += 0.3 # Higher score for Books & Media

    # Convert the dictionary to a pandas DataFrame, which is the standard
    # format for working with data in Seaborn.
    df = pd.DataFrame(data)
    df = df.sort_values('Average Satisfaction Score', ascending=False)

    # 2. Apply professional styling
    # Set the overall style of the plot for a clean, professional look.
    sns.set_style("whitegrid")
    # Set the context to 'talk' to make fonts and lines thicker, suitable for presentations.
    sns.set_context("talk")

    # 3. Create the barplot
    # Set the figure size. An 8x8 inch figure with a DPI of 64 will result in a 512x512 pixel image.
    plt.figure(figsize=(8, 8))

    # Create the barplot using a professional and accessible color palette ('viridis').
    barplot = sns.barplot(
        x='Average Satisfaction Score',
        y='Product Category',
        data=df,
        palette='viridis'
    )

    # 4. Customize the chart with titles and labels
    plt.title('Average Customer Satisfaction by Product Category', fontsize=18, weight='bold', pad=20)
    plt.xlabel('Average Satisfaction Score (out of 5)', fontsize=14)
    plt.ylabel('Product Category', fontsize=14)

    # Set x-axis limits to provide better context for the scores (e.g., from 0 to 5).
    plt.xlim(0, 5)
    
    # Add data labels to each bar for precise readings
    for p in barplot.patches:
        width = p.get_width()
        plt.text(width + 0.05, p.get_y() + p.get_height() / 2.,
                 f'{width:.2f}',
                 va='center')


    # 5. Export the chart
    # Use plt.tight_layout() to ensure all elements fit within the figure without overlapping.
    plt.tight_layout()
    # Save the figure to a PNG file with the specified dimensions and resolution.
    # bbox_inches='tight' trims any extra whitespace around the chart.
    plt.savefig('chart.png', dpi=64, bbox_inches='tight')

    print("Chart 'chart.png' (512x512) has been successfully generated.")

if __name__ == '__main__':
    generate_chart()
