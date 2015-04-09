#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import keys

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)

usuario = input("Introduce el usuario: ")
user = api.get_user(usuario)

def rt_filtrer (list_timeline):
    # Returns a list which contains only tweets started by RT
    rts = []
    for tweet in list_timeline:
        if tweet.text[:4] == "RT @":
            rts.append(tweet)

    return rts

def retweets_of():
    #Get user time line
    my_timeline = api.user_timeline(user.id, exclude_replies=True, counter=200)
    my_rts = rt_filtrer(my_timeline)
    rted_people = []

    # get the author of each retweet
    for rt in my_rts:
        rted_people.append(rt.retweeted_status.user.screen_name)


if __name__ == '__main__':
    retweets_of()
