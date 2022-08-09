from datetime import datetime

import matplotlib.dates as mdates
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker


def getUserData(userName, groupedByUserName):
    userActivity = groupedByUserName.get_group(userName)
    timestamps = userActivity['ts'].sort_values().values
    timestamps = np.asarray(timestamps)
    x_array = [datetime.fromtimestamp(x / 1000.0) for x in timestamps]
    y_array = [userName] * len(x_array)
    return x_array, y_array


def getByDays(timestamps):
    days = {1: [], 2: [], 3: [], 31: []}
    for date in timestamps:
        days[date.day].append(date)
    return days


def plotUser(x_array, y_array, ax1):
    ax1.scatter(x_array, y_array, s=10)


def plotByDay(day, groupedByUserName, topUsers, top):
    fig, ax1 = getFigAndAx()
    tick_spacing = 0.5
    ax1.yaxis.set_minor_locator(ticker.MultipleLocator(tick_spacing))

    # fig = plt.figure()
    # ax1 = fig.add_subplot(111)

    for x in topUsers["original_username"][::-1]:
        userActivity = groupedByUserName.get_group(x)
        timestamps = userActivity['ts'].sort_values().values
        timestamps = np.asarray(timestamps)
        timestamps = [datetime.fromtimestamp(x / 1000.0) for x in timestamps]
        x_array = list(filter(lambda date: date.day == day, timestamps))
        y_array = [x] * len(x_array)
        plotUser(x_array, y_array, ax1)

    titleFont = {'family': 'serif', 'color': 'black', 'size': 20}
    labelsFont = {'family': 'serif', 'color': 'darkred', 'size': 15}
    plt.title("User activity  on day :" + str(day), fontdict=titleFont)
    plt.xlabel("Time", fontdict=labelsFont)
    plt.ylabel("User", fontdict=labelsFont)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    plt.gca().xaxis.set_major_locator(mdates.HourLocator())
    plt.gcf().autofmt_xdate()
    plt.savefig("user activity on day :" + str(day) + str(top) + ".png")


def analyzeUsers(top, groupedByUsr):
    topUsers = groupedByUsr.head(top).iloc[1:]
    print(f"Count rows for every user:\n{topUsers}")

    # userActivity = groupedByUserName.get_group("-NVLL-")
    # timestamps = userActivity['ts'].sort_values().values
    # timestamps = np.asarray(timestamps)
    # timestamps = [datetime.fromtimestamp(x / 1000.0) for x in timestamps]
    # byDays = getByDays(timestamps)

    fig, ax1 = getFigAndAx()
    tick_spacing = 0.5
    ax1.yaxis.set_minor_locator(ticker.MultipleLocator(tick_spacing))
    for x in topUsers["original_username"][::-1]:
        x_array, y_array = getUserData(x, groupedByUserNameData)
        plotUser(x_array, y_array, ax1)

    titleFont = {'family': 'serif', 'color': 'black', 'size': 20}
    labelsFont = {'family': 'serif', 'color': 'darkred', 'size': 15}
    plt.title("User activity", fontdict=titleFont)
    plt.xlabel("Time", fontdict=labelsFont)
    plt.ylabel("User", fontdict=labelsFont)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.gcf().autofmt_xdate()
    plt.savefig("user activity" + str(top) + ".png")

    plotByDay(1, groupedByUserNameData, topUsers, top)

    plotByDay(2, groupedByUserNameData, topUsers, top)

    plotByDay(3, groupedByUserNameData, topUsers, top)


def getFigAndAx():
    fig, ax1 = plt.subplots(1, 1, figsize=(100, 20))
    return fig, ax1


SEPARATOR_STYLE = f"\n{'=' * 30}\n"

path = "/Users/hhalevi/Downloads/data.csv"
df = pd.read_csv(path)

# matplotlib.use("TkAgg")

print(f"The Whole DataFrame:\n{df}{SEPARATOR_STYLE}")

total, _ = df.shape

df_unnamed = df[df.original_username.eq('###')]
print(f"df filtered on unnamed users:\n{df_unnamed}")

unnamed_size, _ = df_unnamed.shape
print(f"Total Rows: {total}")
print(f"Unnamed Rows: {unnamed_size}")
unnamed_percentage = unnamed_size / total
print(f"Percentage: {unnamed_percentage * 100}%{SEPARATOR_STYLE}")

groupedByUserNameData = df.groupby('original_username')
gUser = groupedByUserNameData["user"].count().sort_values(ascending=False).reset_index(name="count")
print(f"Count rows for every user:\n{gUser}")

analyzeUsers(1000, gUser)

analyzeUsers(10000, gUser)

# arr = list(range(0, topusers - 1))
# # gUser2["original_username"]
# plt.bar(arr, height=gUser2["count"])
# print("Show bar graph...")
# plt.show()

# # GETTING A DEEP DIVE PER DAY
# import matplotlib.dates as mdates

# fig = plt.figure()
# ax1 = fig.add_subplot(111)


# for x in gUser2["original_username"][::-1]:
#   userActivity = groupedByUserName.get_group(x)
#   timestamps =userActivity['ts'].sort_values().values
#   timestamps = np.asarray(timestamps)
#   timestamps = [datetime.fromtimestamp(x/1000.0) for x in timestamps]
#   x_array = list(filter(lambda date: date.day == 1, timestamps))
#   y_array = [x]*len(x_array)
#   plotUser(x_array,y_array,ax1)


# titleFont = {'family':'serif','color':'black','size':20}
# labelsFont = {'family':'serif','color':'darkred','size':15}
# plt.title("User activity on first day", fontdict = titleFont)
# plt.xlabel("Time", fontdict = labelsFont)
# plt.ylabel("User", fontdict = labelsFont)
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
# plt.gca().xaxis.set_major_locator(mdates.HourLocator())
# plt.gcf().autofmt_xdate()
# plt.savefig("user activity on first day" + str(topusers) + ".png")

#
# part_df = pd.read_csv(path, nrows=1000)
# plt.scatter(part_df["original_username"], part_df["ts"])
# print("Show Histogram...")
# plt.show()
#
# df = df_bonus
# sns.displot(df['original_username'], bins=20, color='red')
#
# df = df_bonus
# total = df.size
# print(total)
# df.head().style
#
# df_unnamed = df[df.original_username.eq('###')]
# unnamed_size = df_unnamed.size
# print(unnamed_size)
# df_unnamed.head().style
#
# unnamed_percentage = unnamed_size / total
# unnamed_percentage
#
# gUser = df.groupby('original_username')
#
# gUser.first()
#
# gUser.groups.keys()
#
# # number of users
# users = len(list(gUser.groups.keys()))
#
# gUserImpact = gUser.size().sort_values(ascending=False)
# gUserImpact.head()
#
# gUserImpact.get("###")
#
# df.hist(by=df['original_username'])
#
# df.count()['original_username'].hist(bins=100)
#
# df['original_username'].hist(by=df['original_username'])
#
# gUser.size().plot(kind="bar")
#
# df.head().hist(bins=1000)
#
# gUser.count().plot(kind='bar')
