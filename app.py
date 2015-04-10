#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import keys
from operator import itemgetter

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)

usuario = input("Tell me an user\'s screen name: ")
user = api.get_user(usuario)

def rt_filtrer (list_timeline):
    # Returns a list which contains only tweets started by RT
    rts = []
    for tweet in list_timeline:
        if tweet.text[:4] == "RT @":
            rts.append(tweet)

    return rts

def remove_all_values (value, list_a):
    while value in list_a:
        list_a.remove(value)

def retweets_of():
    #Get user time line
    my_timeline = api.user_timeline(user.id, exclude_replies=True, counter=200)
    #Filtrer retweets made by this user
    my_rts = rt_filtrer(my_timeline)
    my_last_tweet = my_timeline[-1].id
    rted_people = []

    #repeat process until getting 1000 tweets
    for i in range(200,1000,200):
        # get the author of each retweet
        for rt in my_rts:
            rted_people.append(rt.retweeted_status.user.screen_name)

        my_timeline = []
        my_rts = []
        my_timeline = api.user_timeline(user.id, exclude_replies=True, counter=200, max_id=my_last_tweet)
        my_last_tweet = my_timeline[-1].id
        my_rts = rt_filtrer(my_timeline)
    
    tam_list = len(rted_people)
    rts_stats = []

    # we save in a 2d array the screen_name and the times the user made a rt from this account
    # example: user @user1 made 4 RT of @user2, and 1 RT of @user3. The list would look like this
    # rts_stats = [[user2, 4], [user3, 1]]
    for rt in rted_people:
        each_rted = [rt, rted_people.count(rt)]
        rts_stats.append(each_rted)
        remove_all_values(rt, rted_people)

    # We sort the list by the number of RTs:
    sorted(rts_stats, key=itemgetter(1))

    # And now, print the results
    for result in rts_stats:
        print(result[0]+" is the "+str((result[1]/tam_list)*100)
            +"% of"+usuario+"\'s RTs")

if __name__ == '__main__':
    retweets_of()
