from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


CSV_PATH = Path("/workspaces/GCAP3226_week2/week2.csv")
PLOTS_DIR = Path("/workspaces/GCAP3226_week2/plots")
OUTPUT_PATH = PLOTS_DIR / "government_consideration_bar_chart.png"


def main():
    df = pd.read_csv(CSV_PATH)

    if "government_consideration" not in df.columns:
        raise ValueError("Column 'government_consideration' not found in the dataset.")

    counts = df["government_consideration"].value_counts().sort_index()

    PLOTS_DIR.mkdir(exist_ok=True)

    scale_labels = {
        1: "1 = Not agree (disagree)",
        2: "2 = Slightly disagree",
        3: "3 = Neutral",
        4: "4 = Agree",
        5: "5 = Strongly agree",
    }

    plt.figure(figsize=(9, 5.5))
    bars = plt.bar(counts.index.astype(str), counts.values, color="steelblue")
    plt.title("Government Consideration")
    plt.xlabel("Scale")
    plt.ylabel("Number of Respondents")
    plt.xticks(
        ticks=sorted(counts.index),
        labels=[scale_labels.get(i, str(i)) for i in sorted(counts.index)],
        rotation=0,
    )

    for bar, value in zip(bars, counts.values):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            value + 0.5,
            str(value),
            ha="center",
            va="bottom",
        )

    plt.figtext(
        0.5,
        0.01,
        "Scale note: 1 = not agree/disagree, 5 = agree/strongly agree.",
        ha="center",
        fontsize=9,
    )

    plt.tight_layout(rect=(0, 0.05, 1, 1))
    plt.savefig(OUTPUT_PATH, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"Saved chart to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
