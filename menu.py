import os

class Menu:
    """docstring for Menu"""
    def __init__(self):
        self.option = 0
        self.suboption_menu = 0

    def clean_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def welcome_message(self):

        self.clean_screen()

        print("""


        ---------------------------------------------------------
                            WELCOME TO TWEETSTAT           
        ---------------------------------------------------------
               
                      Get Twitter user\'s profile info

           Remember: with great power comes great responsibility

        """)

    def print_main_menu(self):
        self.clean_screen()

        print("""

        ---------------------------------------------------------
                           TweetStat Main Menu
        ---------------------------------------------------------

        0 --> User stat\'s                 1 --> RT\'s zone
        2 --> Fav\'s zone                  3 --> Follower\'s zone
                   -1 --> Exit          4 --> Extra
        """)

    def print_user_menu(self):

        self.clean_screen()
        print("""
      ---------------------------------------------------------
                       User stat\'s zone menu
      ---------------------------------------------------------

              0 --> More mentioned users.
              1 --> Users who mentioned you more.
               -1 --> Back

            More comming soon

            """)

    def print_rt_menu(self):
        self.clean_screen()

        print("""
        ---------------------------------------------------------
                           RT\'s zone menu
        ---------------------------------------------------------

                0 --> More rted users.
                1 --> User that make more rt\'s. (Comming soon)
                2 --> Top 10 rted\'s tweets. (Comming soon)
                3 --> Average rt per day. (Comming soon)
               -1 --> Back

            """)

    def print_fav_menu(self):
        self.clean_screen()

        print("""
        ---------------------------------------------------------
                           Fav\'s zone menu
        ---------------------------------------------------------
                0 --> More fav users.
                1 --> User that make favorite you more. (Comming soon)
                2 --> Top 10 fav\'s tweets. (Comming soon)
                3 --> Average fav per day. (Comming soon)
               -1 --> Back

            """)

    def log_menu(self):
        self.clean_screen()

        print("""
        ---------------------------------------------------------
                              Log Screen
        ---------------------------------------------------------

            To get acces to TWEETSTAT, please introduce an

                     user screen name without @

            """)
        
        usuario = input('Tell me an user\'s screen name')

        if usuario[0] == '@':
            usuario = usuario[1:]


        print("""

            """)

        return usuario
            


    def print_follower_menu(self):
        self.clean_screen()

        print("""
        ---------------------------------------------------------
                           Follower\'s zone menu
        ---------------------------------------------------------
                0 --> Not follow back.
                1 --> New follower\'s. (Comming soon)
                2 --> Last unfollows. (Comming soon)
               -1 --> Back
            """)

    def continue_(self):
        input("Press any key to continue...")

    def print_exit_log(self):
        self.clean_screen()

        print("""           


        ---------------------------------------------------------
                            Exiting of TweetStat           
        ---------------------------------------------------------
               
                      Thank you for using TweetStat.

              Remember what uncle Ben said once before he died:

                \"With great power comes great responsibility\"


            """)

    def extra(self):
        self.clean_screen()

        print("""
        ---------------------------------------------------------
                              TWEETSTAT
        ---------------------------------------------------------

        TweetStat is an oupen source code with GNU-3 License

        The authors of this dangerous work are:

           Marta Gómez     --> https://github.com/mgmacias95
           Braulio Vargas  --> https://github.com/BraulioV


        Press -1 to go back
        
            """)        

    def set_main_menu_opt(self):

        num_opts = 4

        self.option = int(input("Choose a valid option: "))

        if self.option < -1 or self.option > num_opts:
            print("Oups! Something is wrong with your choice")

            while self.option < -1 or self.option > num_opts:
                self.option = int(input("Try to choose a valid option: "))

    def set_submenu_opt(self, num_opts):
        self.suboption_menu = int(input("Choose a valid option: "))

        if self.suboption_menu < -1 or self.suboption_menu > num_opts:
            print("Oups! Something is wrong with your choice.")

            while self.suboption_menu < -1 or self.suboption_menu > num_opts:
                self.suboption_menu = int(input("Try to choose a valid option: "))
