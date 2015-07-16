import os
import colors
from colors import bcolors

class Menu:
    """docstring for Menu"""
    def __init__(self):
        self.option = 0
        self.suboption_menu = 0

    def clean_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def blue_world(self):
        print(bcolors.bblue)

    def normal_world(self):
        print(bcolors.ENDC)

    def welcome_message(self):

        self.clean_screen()

        print(bcolors.BOLD+"""


        ---------------------------------------------------------
                            WELCOME TO TWEETSTAT           
        ---------------------------------------------------------
               
                      Get Twitter user\'s profile info

           Remember: \"with great power comes great responsibility\"

        """+bcolors.ENDC)
        self.blue_world()

    def print_main_menu(self):
        self.clean_screen()

        print(bcolors.BOLD+"""

        ---------------------------------------------------------
                           TweetStat Main Menu
        ---------------------------------------------------------

        0 --> User stat\'s                 1 --> RT\'s zone
        2 --> Fav\'s zone                  3 --> Follower\'s zone
                   -1 --> Exit          4 --> Extra
        """+bcolors.ENDC)
        self.blue_world()

    def print_user_menu(self):

        self.clean_screen()
        print(bcolors.BOLD+"""
      ---------------------------------------------------------
                       User stat\'s zone menu
      ---------------------------------------------------------

              0 --> More mentioned users.
              1 --> Users who mentioned you more.
              2 --> Relations between you and other user.
             -1 --> Back

            More comming soon

            """+bcolors.ENDC)
        self.blue_world()

    def print_rt_menu(self):
        self.clean_screen()

        print(bcolors.BOLD+"""
        ---------------------------------------------------------
                           RT\'s zone menu
        ---------------------------------------------------------

                0 --> More rted users.
                1 --> User that make more rt\'s.
                2 --> Most retweeted tweets.
               -1 --> Back

            """+bcolors.ENDC)
        self.blue_world()

    def print_fav_menu(self):
        self.clean_screen()

        print(bcolors.BOLD+"""
        ---------------------------------------------------------
                           Fav\'s zone menu
        ---------------------------------------------------------
                0 --> More fav users.
                1 --> Most faved tweets.
               -1 --> Back

            """+bcolors.ENDC)
        self.blue_world()

    def log_menu(self):
        self.clean_screen()

        print(bcolors.BOLD+"""
        ---------------------------------------------------------
                              Log Screen
        ---------------------------------------------------------

            To get access to TWEETSTAT, please introduce an

                     user screen name without @

            """+bcolors.ENDC)
        self.blue_world()
        
        usuario = input(bcolors.BOLD+'Tell me an user\'s screen name: '+bcolors.ENDC+bcolors.bblue)

        if usuario[0] == '@':
            usuario = usuario[1:]


        print("""

            """)

        return usuario
            


    def print_follower_menu(self):
        self.clean_screen()

        print(bcolors.BOLD+"""
        ---------------------------------------------------------
                           Follower\'s zone menu
        ---------------------------------------------------------
                0 --> Not follow back.
                1 --> New followers.
                2 --> Last unfollows.
               -1 --> Back
            """+bcolors.ENDC)

    def continue_(self):

        wait = input(bcolors.BOLD+"""





Press any key to continue..."""+bcolors.ENDC)
        self.blue_world()

    def print_exit_log(self):
        self.clean_screen()

        print(bcolors.BOLD+"""           


        ---------------------------------------------------------
                            Exiting of TweetStat           
        ---------------------------------------------------------
               
                      Thank you for using TweetStat.

             Remember what uncle Ben said once before he died:

              \"With great power comes great responsibility\"


            """+bcolors.ENDC)
        self.blue_world()

    def extra(self):
        self.clean_screen()

        print(bcolors.BOLD+"""
        ---------------------------------------------------------
                              TWEETSTAT
        ---------------------------------------------------------

           TweetStat is an oupen source code with GNU-3 License

           The authors of this dangerous work are:

             Marta Gomez     --> https://github.com/mgmacias95
             Braulio Vargas  --> https://github.com/BraulioV


                        



                        Press -1 to go back
        
            """+bcolors.ENDC)
        self.blue_world()        

    def set_main_menu_opt(self):

        num_opts = 4

        self.option = int(input(bcolors.BOLD+"Choose a valid option: "+bcolors.ENDC+bcolors.bblue))

        if self.option < -1 or self.option > num_opts:
            print(bcolors.BOLD+bcolors.FAIL+"Oups! Something is wrong with your choice D:"+bcolors.ENDC+bcolors.bblue)

            while self.option < -1 or self.option > num_opts:
                self.option = int(input(bcolors.BOLD+"Try to choose a valid option: "+bcolors.ENDC+bcolors.bblue))

    def set_submenu_opt(self, num_opts):
        self.suboption_menu = int(input(bcolors.BOLD+"Choose a valid option: "+bcolors.ENDC+bcolors.bblue))

        if self.suboption_menu < -1 or self.suboption_menu > num_opts:
            print(bcolors.BOLD+bcolors.FAIL+"Oups! Something is wrong with your choice."+bcolors.ENDC+bcolors.bblue)

            while self.suboption_menu < -1 or self.suboption_menu > num_opts:
                self.suboption_menu = int(input(bcolors.BOLD+"Try to choose a valid option: "+bcolors.ENDC+bcolors.bblue))
