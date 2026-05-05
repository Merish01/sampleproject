from data_loader import load_data
from data_processing import process_data
from visualization import (
    plot_scatter,
    plot_histogram,
    plot_bar,
    plot_pie,
    plot_subplot
)

df = load_data("StudentData.csv")

if df is not None:
    
    df, grouped = process_data(df)

    # Step 3: Visualize
    plot_scatter(df)
    plot_histogram(df)
    plot_bar(grouped)
    plot_pie(df)
    plot_subplot(df)