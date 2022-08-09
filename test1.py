if __name__ == '__main__':
    import pandas as pd
    # import matplotlib.pyplot as plt
    import matplotlib

    matplotlib.use("TkAgg")
    from matplotlib import pyplot as plt

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
    # print(f"Count rows for every user:\n{gUser}")

    topusers = 100000
    gUser1 = gUser.head(topusers)
    gUser2 = gUser1.iloc[1:]
    print(f"Count rows for every user:\n{gUser2}")

    arr = list(range(0, topusers - 1))
    # gUser2["original_username"]
    plt.bar(arr, height=gUser2["count"])
    print("Show bar graph...")
    # plt.show()
    plt.savefig("topusers" + str(topusers) + ".png")
