# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    # import seaborn as sns

    SEPARATOR_STYLE = f"\n{'=' * 30}\n"

    path = "/Users/hhalevi/Downloads/data.csv"
    # TODO: change to original path
    df = pd.read_csv(path)

    print(f"The Whole DataFrame:\n{df}{SEPARATOR_STYLE}")

    total, _ = df.shape

    df_unnamed = df[df.original_username.eq('###')]
    print(f"df filtered on unnamed users:\n{df_unnamed}")
    unnamed_size, _ = df_unnamed.shape

    print(f"Total Rows: {total}")
    print(f"Unnamed Rows: {unnamed_size}")

    unnamed_percentage = unnamed_size / total

    print(f"Percentage: {unnamed_percentage * 100}%{SEPARATOR_STYLE}")

    gUser = df.groupby('original_username')["user"].count().sort_values(ascending=False).reset_index(name="count")
    print(f"Count rows for every user:\n{gUser}")

    plt.hist(gUser["original_username"], weights=gUser["count"], bins=30)
    print("Show Histogram...")
    plt.show()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
