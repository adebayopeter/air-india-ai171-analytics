from data_loader import load_common_data
from visualizations import save_charts
df = load_common_data()

if __name__ == "__main__":
    save_charts(df)
