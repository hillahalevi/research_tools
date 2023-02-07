# - [ ] Sort tweets ( with hashtags and no hashtags )
# - [ ] Train model tweets to hashtags
# - [ ] Run on all hashtags result : tweets to hashtags map
# - [ ] Get top hashtags (hashtags with a lot of tweets)

import json


def sortTweets(path):
    data = [json.loads(line) for line in open(path, 'r')]
    data_with_hashtagss = []
    data_with_no_hashtagss = []

    for i in data:
        if 'entities' in i and 'hashtags' in i['entities'] and i['entities']['hashtags']:
            print(i['entities']['hashtags'])
            data_with_hashtagss.append(i)
        else:
            data_with_no_hashtagss.append(i)

    return data_with_hashtagss, data_with_no_hashtagss



if __name__ == '__main__':
    paths = ["/Users/hhalevi/PycharmProjects/help/hashtagsReco/trending_topics_hebrew/Hebrew_tweets.json.2022-10-19",
             "/Users/hhalevi/PycharmProjects/help/hashtagsReco/trending_topics_hebrew/Hebrew_tweets.json.2022-10-20",
             "/Users/hhalevi/PycharmProjects/help/hashtagsReco/trending_topics_hebrew/Hebrew_tweets.json.2022-10-21",
             "/Users/hhalevi/PycharmProjects/help/hashtagsReco/trending_topics_hebrew/Hebrew_tweets.json.2022-10-22"]
    data_with_hashtags = []
    data_with_no_hashtags = []

    for path in paths:
        data_with_hashtags1, data_with_no_hashtags1 = sortTweets(path)
        data_with_no_hashtags = data_with_no_hashtags + data_with_hashtags1
        data_with_hashtags = data_with_hashtags + data_with_hashtags1

        print(data_with_hashtags1)

        print("done " + path)

    with open("hashtagsData.json", "w") as outfile:
        json.dump(data_with_hashtags, outfile)

    with open("no_hashtagsData.json", "w") as outfile:
        json.dump(data_with_no_hashtags, outfile)
    print("done all paths ")


