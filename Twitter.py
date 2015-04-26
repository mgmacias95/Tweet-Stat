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

    # Returns a list of the users who more mention to the specified user
    def mentioners(self):
        # Get the lastest mentions to the user
        mentions = self.api.mentions_timeline(self.user.id, count=75)

        # Save screen names of the people who mentioned
        people_who_mentioned = []

        for plp in mentions:
            people_who_mentioned.append(plp.user.screen_name)

        # Save a 2d array the screen name and the times the specified user has been mentioned by the user
        mentioned_stats = []
        for mention in people_who_mentioned:
            each_m = [mention, people_who_mentioned.count(mention)]
            if mentioned_stats.count(each_m) == 0:
                mentioned_stats.append(each_m)

        # Now we sort the list
        mentioned_stats.sort(key=itemgetter(1), reverse=True)

        # And print the results
        for result in mentioned_stats:
            print(result[0]+" mentions "+self.user.screen_name+" the "+str((result[1]/75)*100)+"% of the times")

    def __mentions_filtrer(self, list_timeline):
        my_mentioned_people = []
        for tweet in list_timeline:
            if len(tweet.entities['user_mentions']) > 0:
                for users in tweet.entities['user_mentions']:
                    my_mentioned_people.append(users['screen_name'])

        return my_mentioned_people

    # Returns a list with the users the specified user mentions more
    def more_mentioned (self):
        # Get the user time lime
        my_timeline = self.api.user_timeline(self.user.id, counter=200, include_rts=False)
        my_last_tweet = my_timeline[-1].id

        my_mentioned_people = []

        # Repeat the process until getting 1000 tweets
        for i in range(200,1000,200):
            # get the people who the specified user mentions
            aux = self.__mentions_filtrer(my_timeline)
            for sn in aux:
                my_mentioned_people.append(sn)

            my_timeline = []
            my_timeline = self.api.user_timeline(self.user.id, include_rts=False, counter=200, max_id=my_last_tweet)
            my_last_tweet = my_timeline[-1].id
            aux = []

        tam_list = len(my_mentioned_people)
        mentions_stats = []

        # save in a 2D array the screen name and the times the user mentioned this screen name.
        for mention in my_mentioned_people:
            each_mention = [mention, my_mentioned_people.count(mention)]
            if mentions_stats.count(each_mention) == 0:
                mentions_stats.append(each_mention)

        # sort the list by the number of mentions
        mentions_stats.sort(key=itemgetter(1), reverse=True)

        # print the results
        for result in mentions_stats:
            print(self.user.screen_name+" mentions "+result[0]+" the "
                +str((result[1]/tam_list)*100)+"% of the times")


    # Returns a list of the users who the user follows and dont have a follow back
    def not_follow_back(self, fol_sn):
        # Get users friends list (last 5000 friends)
        my_friends = self.api.friends_ids(self.user.id)

        fr_sn = self.__get_screen_names(my_friends) # a list to save friends screen name

        for friend in fr_sn:
            if fol_sn.count(friend) == 0:
                print(friend+" does not follow "+self.user.screen_name+" back")

    # Returns a list with screen_names from a id list given
    def get_screen_names(self, id_list):
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

            f = open(self.user.screen_name, "w")
            f.writelines("%s\n" % l for l in my_actuals)
            print(self.user.screen_name+"\'s followers file updated")

        except IOError as e:
            print("followers file does not exists for "+self.user.screen_name)
            # save the actual followers list
            print("Creating file...")
            my_fol_sn = self.get_screen_names(my_followers)
            f = open(self.user.screen_name, "w")
            f.writelines("%s\n" % l for l in my_fol_sn)
            # compare with the friends list
            print("Checking friends list...")
            self.not_follow_back(my_fol_sn)

    # Returns the relationship between the specified user and another one
    def relationship(self):
        user2 = input("Tell me an screen name: ")
        rel = self.api.show_friendship(source_screen_name=self.user.screen_name, target_screen_name=user2)
        
        print(self.user.screen_name+"\'s relationship with "+user2+":")
        if rel[0].notifications_enabled:
            print(self.user.screen_name+" has notifications enabled for "+user2)
        elif rel[0].notifications_enabled == False:
            print(self.user.screen_name+" has not notifications enabled for "+user2)

        if rel[0].blocked_by:
            print(self.user.screen_name+" is blocked by "+user2)
        elif rel[0].blocked_by == False:
            print(self.user.screen_name+" is not blocked by "+user2)

        if rel[0].blocking:
            print(user2+" is blocked by "+self.user.screen_name)
        elif rel[0].blocking == False:
            print(user2+" is not blocked by "+self.user.screen_name)

        if rel[0].following:
            print(self.user.screen_name+" follows "+user2)
        else:
            print(self.user.screen_name+" does not follow "+user2)

        if rel[0].followed_by:
            print(self.user.screen_name+" is followed by "+user2)
        else:
            print(self.user.screen_name+" is not followed by "+user2)

        if rel[0].marked_spam:
            print(user2+" has been marked as spam by"+self.user.screen_name)
        elif rel[0].marked_spam == False:
            print(user2+" has not been marked as spam by "+self.user.screen_name)

        if rel[0].muting:
            print(user2+" is muted by "+self.user.screen_name)
        elif rel[0].muting == False:
            print(user2+" is not muted by "+self.user.screen_name)

        if rel[0].want_retweets:
            print(self.user.screen_name+" wants to see "+user2+"\'s retweets")
        elif rel[0].want_retweets == False:
            print(self.user.screen_name+" does not want to see "+user2+"\'s retweets")

        if rel[0].can_dm:
            print(self.user.screen_name+" can send direct messages to "+user2)
        else:
            print(self.user.screen_name+" cannot send direct messages to "+user2)
