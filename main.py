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
            num_opt = 2
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

            menu.print_main_menu()
            menu.set_main_menu_opt()

        elif menu.option == 1:
            num_opt = 4
            menu.print_rt_menu()
            menu.set_submenu_opt(num_opt-1)
            while menu.suboption_menu != -1:
                if menu.suboption_menu == 0:
                    print("Calling more rted users...")
                    menu.continue_()
                    menu.print_rt_menu()
                    menu.set_submenu_opt(num_opt-1)

                elif menu.suboption_menu == 1:
                    print("Calling user that make mor rt\'s")
                    menu.continue_()
                    menu.print_rt_menu()
                    menu.set_submenu_opt(num_opt-1)

                elif menu.suboption_menu == 2:
                    print("Top 10 rted\'s tweets")
                    menu.continue_()
                    menu.print_rt_menu()
                    menu.set_submenu_opt(num_opt-1)

                elif menu.suboption_menu == 3:
                    print("Average rt per day")
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
                    print("More fav users...")
                    menu.continue_()
                    menu.print_fav_menu()
                    menu.set_submenu_opt(num_opt-1)

                elif menu.suboption_menu == 1:
                    print("User that make favorite you more")
                    menu.continue_()
                    menu.print_fav_menu()
                    menu.set_submenu_opt(num_opt-1)

                elif menu.suboption_menu == 2:
                    print("Top 10 fav\'s tweets")
                    menu.continue_()
                    menu.print_fav_menu()
                    menu.set_submenu_opt(num_opt-1)

                elif menu.suboption_menu == 3:
                    print("Average fav per day")
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
                    print("Not follow back")
                    menu.continue_()
                    menu.print_follower_menu()
                    menu.set_submenu_opt(num_opt-1)

                elif menu.suboption_menu == 1:
                    print("New follower\'s")
                    menu.continue_()
                    menu.print_follower_menu()
                    menu.set_submenu_opt(num_opt-1)

                elif menu.suboption_menu == 2:
                    print("Last unfollows")
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
