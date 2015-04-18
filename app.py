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
print("-----------------------------------------------------------")

# Returns a list which contains only tweets started by RT
def rt_filtrer (list_timeline):
    rts = []
    for tweet in list_timeline:
        if tweet.text[:4] == "RT @":
            rts.append(tweet)

    return rts

# Returns some stats of the most rted users by the specified user
def most_rtd_users():
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
        if rts_stats.count(each_rted) == 0:
            rts_stats.append(each_rted)

    # We sort the list by the number of RTs:
    rts_stats.sort(key=itemgetter(1), reverse=True)

    # And now, print the results
    for result in rts_stats:
        print(result[0]+" has the "+str((result[1]/tam_list)*100)
            +"% of "+usuario+"\'s latest RTs")

# Returns some stats of the most faved users by the specified user
def most_faved_users():
    # Get the user fav list
    my_favs = api.favorites(user.screen_name, count=20)

    # Save screen names of the faved people
    faved_people = []

    for fav in my_favs:
        faved_people.append(fav.user.screen_name)

    # Save a 2d array the screen name and the times the user has faved this screen name
    fav_stats = []
    for fav in faved_people:
        each_faved = [fav, faved_people.count(fav)]
        if fav_stats.count(each_faved) == 0:
            fav_stats.append(each_faved)

    # Now we sort the list
    fav_stats.sort(key=itemgetter(1), reverse=True)

    # And print the results
    for result in fav_stats:
        print(result[0]+" has the "+str((result[1]/20)*100)
            +"% of "+usuario+"\'s latest FAVs")

# Returns a list of the users who the user follows and dont have a follow back
def not_follow_back():
    # Get users friends list (last 5000 friends)
    my_friends = api.friends_ids(user.id)
    # Get users followers list (last 5000 friends)
    my_followers = api.followers_ids(user.id)

    fol_sn = [] # a list to save followers screen name
    fr_sn = [] # a list to save friends screen name

    # Get users screen name
    for x in range(0,user.followers_count,100):
        fol = api.lookup_users(user_ids=my_followers[x:(x+100)])
        for usr in fol:
            fol_sn.append(usr.screen_name)

    for x in range(0,user.friends_count,100):
        fr = api.lookup_users(user_ids=my_friends[x:(x+100)])
        for usr in fr:
            fr_sn.append(usr.screen_name)

    for friend in fr_sn:
        if fol_sn.count(friend) == 0:
            print(friend+" does not follow you back")


if __name__ == '__main__':
    not_follow_back()
