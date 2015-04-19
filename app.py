#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import keys
from Twitter import Twitter

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)

usuario = input("Tell me an user\'s screen name: ")
user = api.get_user(usuario)
print("-----------------------------------------------------------")

if __name__ == '__main__':
    tw = Twitter(user, api)
    tw.who_unfollowed()
