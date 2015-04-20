#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
from operator import itemgetter

class Twitter:
    """Clase donde se encapsularán todos los métodos para trabajar con Twitter"""
    def __init__(self, user, api):
        self.user = user
        self.api = api

    # Returns a list which contains only tweets started by RT
    def __rt_filtrer (self, list_timeline):
        rts = []
        for tweet in list_timeline:
            if tweet.text[:4] == "RT @":
                rts.append(tweet)

        return rts

    # Returns some stats of the most rted users by the specified user
    def most_rtd_users(self):
        #Get user time line
        my_timeline = self.api.user_timeline(self.user.id, exclude_replies=True, counter=200)
        #Filtrer retweets made by this user
        my_rts = self.__rt_filtrer(my_timeline)
        my_last_tweet = my_timeline[-1].id
        rted_people = []

        #repeat process until getting 1000 tweets
        for i in range(200,1000,200):
            # get the author of each retweet
            for rt in my_rts:
                rted_people.append(rt.retweeted_status.user.screen_name)

            my_timeline = []
            my_rts = []
            my_timeline = self.api.user_timeline(self.user.id, exclude_replies=True, counter=200, max_id=my_last_tweet)
            my_last_tweet = my_timeline[-1].id
            my_rts = self.__rt_filtrer(my_timeline)
        
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
                +"% of "+self.user.screen_name+"\'s latest RTs")


    # Returns some stats of the most faved users by the specified user
    def most_faved_users(self):
        # Get the user fav list
        my_favs = self.api.favorites(self.user.screen_name, count=20)

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
                +"% of "+self.user.screen_name+"\'s latest FAVs")

    # Returns a list of the users who the user follows and dont have a follow back
    def not_follow_back(self, fol_sn):
        # Get users friends list (last 5000 friends)
        my_friends = self.api.friends_ids(self.user.id)

        fr_sn = self.__get_screen_names(my_friends) # a list to save friends screen name

        for friend in fr_sn:
            if fol_sn.count(friend) == 0:
                print(friend+" does not follow "+self.user.screen_name+" back")

    # Returns a list with screen_names from a id list given
    def __get_screen_names(self, id_list):
        l = []

        for x in range(0,len(id_list),100):
            li = self.api.lookup_users(user_ids=id_list[x:(x+100)])
            for usr in li:
                l.append(usr.screen_name)

        return l

    # Returns a list of the people who unfollowed the specified user
    # it works this way: 
    #   if there's a file called self.user.screen_name it compares
    #   the content of this file with the actual list of followers
    #   if there's no file, it downloads the actual list of followers, writes it
    #   on a file called self.user.screen_name and compares the list with
    #   the list of friends.
    def who_unfollowed(self):
        #download actual followers list:
        my_followers = self.api.followers_ids(self.user.id)

        # try to open the file:
        try:
            f = open(self.user.screen_name)
            my_actuals = self.__get_screen_names(my_followers)
            anyone_unfollowed = False
            for line in f:
                if my_actuals.count(line[:len(line)-1]) == 0:
                    anyone_unfollowed = True
                    print(line[:len(line)-1]+" recently unfollowed "+self.user.screen_name)

            if not anyone_unfollowed: 
                print("No one unfollowed "+self.user.screen_name)
            else:
                f = open(self.user.screen_name, "w")
                f.writelines("%s\n" % l for l in my_actuals)
                print(self.user.screen_name+"\'s followers file updated")

        except IOError as e:
            print("followers file does not exists for "+self.user.screen_name)
            # save the actual followers list
            print("Creating file...")
            my_fol_sn = self.__get_screen_names(my_followers)
            f = open(self.user.screen_name, "w")
            f.writelines("%s\n" % l for l in my_fol_sn)
            # compare with the friends list
            print("Checking friends list...")
            self.not_follow_back(my_fol_sn)
