from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


CSV_PATH = Path("/workspaces/GCAP3226_week2/week2.csv")
PLOTS_DIR = Path("/workspaces/GCAP3226_week2/plots")
OUTPUT_PATH = PLOTS_DIR / "government_consideration_scatter.png"


def main():
    df = pd.read_csv(CSV_PATH)

    if "government_consideration" not in df.columns:
        raise ValueError("Column 'government_consideration' not found in the dataset.")

    x = range(len(df))
    y = df["government_consideration"]

    PLOTS_DIR.mkdir(exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color="darkorange", alpha=0.8, s=40)
    plt.title("Scatter Plot of Government Consideration")
    plt.xlabel("Respondent Index")
    plt.ylabel("Government Consideration")
    plt.xticks([])
    plt.yticks(range(1, 6), ["1", "2", "3", "4", "5"])
    plt.ylim(0.5, 5.5)

    plt.figtext(
        0.5,
        0.01,
        "Scale note: 1 = not agree / disagree, 5 = agree / strongly agree.",
        ha="center",
        fontsize=9,
    )

    plt.tight_layout(rect=(0, 0.05, 1, 1))
    plt.savefig(OUTPUT_PATH, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"Saved scatter plot to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
