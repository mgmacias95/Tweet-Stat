#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import keys
import menu
from menu import Menu 
from Twitter import Twitter

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    api = tweepy.API(auth)

    menu = Menu()

    menu.blue_world()

    usuario = menu.log_menu()

    while not usuario:
        print("Check that you put a screen name")
        usuario = menu.log_menu()

    user = api.get_user(usuario)
    tw = Twitter(user, api)

    menu.welcome_message()
    menu.print_main_menu()

    menu.set_main_menu_opt()

    while menu.option != -1:
        if menu.option == 0:
            num_opt = 3
            menu.print_user_menu()
            menu.set_submenu_opt(num_opt-1)

            while menu.suboption_menu != -1:
                if menu.suboption_menu == 0:
                    print("More mentioned users by "+user.screen_name)
                    tw.more_mentioned()
                    menu.continue_()
                    menu.print_user_menu()
                    menu.set_submenu_opt(num_opt-1)
                elif menu.suboption_menu == 1:
                    print("Users who more mention "+user.screen_name)
                    tw.mentioners()
                    menu.continue_()
                    menu.print_user_menu()
                    menu.set_submenu_opt(num_opt-1)
                elif menu.suboption_menu == 2:
                    tw.relationship()
                    menu.continue_()
                    menu.print_user_menu()
                    menu.set_submenu_opt(num_opt-1)

            menu.print_main_menu()
            menu.set_main_menu_opt()

        elif menu.option == 1:
            num_opt = 4
            menu.print_rt_menu()
            menu.set_submenu_opt(num_opt-1)
            while menu.suboption_menu != -1:
                if menu.suboption_menu == 0:
                    print("Users more retweeted by "+user.screen_name)
                    tw.most_rtd_users()
                    menu.continue_()
                    menu.print_rt_menu()
                    menu.set_submenu_opt(num_opt-1)

                elif menu.suboption_menu == 1:
                    print("Calling user that make mor rt\'s (Comming soon...)")
                    menu.continue_()
                    menu.print_rt_menu()
                    menu.set_submenu_opt(num_opt-1)

                elif menu.suboption_menu == 2:
                    print("Top 10 rted\'s tweets (Comming soon...)")
                    menu.continue_()
                    menu.print_rt_menu()
                    menu.set_submenu_opt(num_opt-1)

                elif menu.suboption_menu == 3:
                    print("Average rt per day (Comming soon...)")
                    menu.continue_()
                    menu.print_rt_menu()
                    menu.set_submenu_opt(num_opt-1)

            menu.print_main_menu()
            menu.set_main_menu_opt()

        elif menu.option == 2:
            num_opt = 4
            menu.print_fav_menu()
            menu.set_submenu_opt(num_opt-1)
            
            while menu.suboption_menu != -1:
                if menu.suboption_menu == 0:
                    print("Users more favorited by "+user.screen_name)
                    tw.most_faved_users()
                    menu.continue_()
                    menu.print_fav_menu()
                    menu.set_submenu_opt(num_opt-1)

                elif menu.suboption_menu == 1:
                    print("User that make favorite you more (Comming soon...)")
                    menu.continue_()
                    menu.print_fav_menu()
                    menu.set_submenu_opt(num_opt-1)

                elif menu.suboption_menu == 2:
                    print("Most faved tweets by "+user.screen_name)
                    tw.most_faved_tweets()
                    menu.continue_()
                    menu.print_fav_menu()
                    menu.set_submenu_opt(num_opt-1)

                elif menu.suboption_menu == 3:
                    print("Average fav per day (Comming soon...)")
                    menu.continue_()
                    menu.print_fav_menu()
                    menu.set_submenu_opt(num_opt-1)

            menu.print_main_menu()
            menu.set_main_menu_opt()

        elif menu.option == 3:
            num_opt = 3
            menu.print_follower_menu()
            menu.set_submenu_opt(num_opt-1)
            
            while menu.suboption_menu != -1:
                if menu.suboption_menu == 0:
                    print("Users who does not follow back "+user.screen_name)
                    my_followers = self.api.followers_ids(user.id)
                    my_fol_sn = tw.get_screen_names(my_followers)
                    tw.not_follow_back(my_fol_sn)
                    menu.continue_()
                    menu.print_follower_menu()
                    menu.set_submenu_opt(num_opt-1)

                elif menu.suboption_menu == 1:
                    print("New follower\'s (Comming soon...)")
                    menu.continue_()
                    menu.print_follower_menu()
                    menu.set_submenu_opt(num_opt-1)

                elif menu.suboption_menu == 2:
                    print("Last unfollows of "+user.screen_name)
                    tw.who_unfollowed()
                    menu.continue_()
                    menu.print_follower_menu()
                    menu.set_submenu_opt(num_opt-1)

            menu.print_main_menu()
            menu.set_main_menu_opt()

        elif menu.option == 4:
            num_opt = 1
            menu.extra()
            menu.set_submenu_opt(num_opt-1)
            while menu.suboption_menu != -1:
                menu.set_submenu_opt(num_opt-1)

            menu.print_main_menu()
            menu.set_main_menu_opt()

    if menu.option == -1:
        menu.print_exit_log()

    menu.normal_world()
