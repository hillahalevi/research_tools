from datetime import datetime

import matplotlib.dates as mdates
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import praw
import pandas as pd

# # Replace <client_id> and <client_secret> with your own credentials
# reddit = praw.Reddit(client_id='<client_id>', client_secret='<client_secret>',
#                      user_agent='<client_id>:<client_secret> (by /u/<reddit_username>)',
#                      access_token='<access_token>')

reddit = praw.Reddit(client_id='FnSwswueosOi_g',
                     client_secret='kcUc1ZMxUDLHgO4gzdFCdca79xk',
                     password='gefenp4',
                     user_agent='Avrahami_crawling_data',
                     username='avrahami_isr')

SEPARATOR_STYLE = f"\n{'=' * 30}\n"

path = "/Users/hhalevi/Downloads/data.csv"
df = pd.read_csv(path)
df = df[df.original_username != '###']

# group the data frame by the original_username column
grouped = df.groupby('original_username')

# count the number of rows for each group
result = grouped.size().reset_index(name='counts')

# sort the result by the counts column in descending order
result = result.sort_values(by='counts', ascending=False)

# get a list of original_username sorted by the number of rows they had
usernames = list(result['original_username'])

# print the result
print(usernames)

# Initialize a list to store the extracted information for each user
user_data_list = []

# Iterate over the list of usernames
for username in usernames:
    try:
        # Retrieve information about the Reddit user
        user = reddit.redditor(username)
        # Extract the required information
        num_posts = user.link_karma + user.comment_karma
        likes = user.link_karma
        comments = user.comment_karma
        communities = len(user.subreddits)

        # Store the extracted information in a dictionary
        user_info = {
            'username': username,
            'num_posts': num_posts,
            'likes': likes,
            'comments': comments,
            # 'communities': communities
        }

        # Append the dictionary to the list of user information
        user_data_list.append(user_info)
    except:
        # Print an error message if the Reddit user was not found
        print(f'User {username} not found')

# Create a pandas DataFrame from the list of user information
users_df = pd.DataFrame(user_data_list)
users_df.to_csv("users_data.csv", index=False)
