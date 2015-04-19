class Menu:
	"""docstring for Menu"""
	def __init__(self):
		self.option = 0
		self.suboption_menu = 0

	def welcome_message(self):
		print("""


        ---------------------------------------------------------
                            WELCOME TO TWEETSTAT           
        ---------------------------------------------------------
               
                      Get Twitter user\'s profile info

           Remember: with great power comes great responsibility

		""")

	def print_main_menu(self):
		print("""

        ---------------------------------------------------------
                           TweetStat Main Menu
        ---------------------------------------------------------

        0 --> User stat\'s                 1 --> RT\'s zone
        2 --> Fav\'s zone                  3 --> Follower\'s zone
                            -1 --> Exit
		""")

	def print_user_menu(self):
		print("""
			User stat\'s zone menu

			0 --> ??
			1 --> ?? 

			More comming soon

			""")

	def print_rt_menu(self):
		print("""
        ---------------------------------------------------------
                           RT\'s zone menu
        ---------------------------------------------------------

               0 --> More rted users.
               1 --> User that make more rt\'s. (Comming soon)
               2 --> Top 10 rted\'s tweets. (Comming soon)
               3 --> Average rt per day. (Comming soon)

			""")

	def print_fav_menu(self):
		print("""
        ---------------------------------------------------------
                           Fav\'s zone menu
        ---------------------------------------------------------
               0 --> More fav users.
               1 --> User that make favorite you more. (Comming soon)
               2 --> Top 10 fav\'s tweets. (Comming soon)
               3 --> Average fav per day. (Comming soon)

			""")		

	def print_follower_menu(self):

		print("""
        ---------------------------------------------------------
                           Follower\'s zone menu
        ---------------------------------------------------------
               0 --> Not follow back.
               1 --> New follower\'s. (Comming soon)
               2 --> Last unfollows. (Comming soon)
               -1 --> Back
			""")

	def print_exit_log(self):

		print("""			


        ---------------------------------------------------------
                            Exiting of TweetStat           
        ---------------------------------------------------------
               
                      Thank you for using TweetStat

               Remember what uncle Ben said once before die:

                With great power comes great responsibility


			""")

	def set_main_menu_opt(self):
		self.option = int(input("Choose a valid option: "))

		if self.option < -1 or self.option > 3:
			print("Oups! Something is wrong with your choice")

			while self.option < -1 or self.option > 3:
				self.option = int(input("Try to choose a valid option: "))

	def set_submenu_opt(self):
		self.suboption_menu = int(input("Choose a valid option: "))

		if self.suboption_menu < -1 or self.suboption_menu > 3:
			print("Oups! Something is wrong with your choice")

			while self.suboption_menu < -1 or self.suboption_menu > 3:
				self.option = int(input("Try to choose a valid option: "))

if __name__ == '__main__':
    menu = Menu()
    menu.welcome_message()
    menu.print_main_menu()

    menu.set_main_menu_opt()

    while menu.option != -1:
    	if menu.option == 0:
    		menu.print_user_menu()
    		menu.suboption_menu = int(input("Choose a valid submenu option: "))

    	elif menu.option == 1:
    		menu.print_rt_menu()
    		menu.suboption_menu = int(input("Choose a valid submenu option: "))

    	elif menu.option == 2:
    		menu.print_fav_menu()
    		menu.suboption_menu = int(input("Choose a valid submenu option: "))

    	elif menu.option == 3:
    		menu.print_follower_menu()
    		menu.suboption_menu = int(input("Choose a valid submenu option: "))


    if menu.option == -1:
    	menu.print_exit_log()
