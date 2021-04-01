#Ali Rajgarah 1586471

soccer_dict = {}
soccer_list_keys = []

def sortDictKeys():

    soccer_list_keys = sorted(soccer_dict.keys())

    return soccer_list_keys


def rosterOutput():

    soccer_list_keys = sortDictKeys()

    print("ROSTER")

    for i in soccer_list_keys:


        print("Jersey number: " + str(i)

              + ", Rating: " + str(soccer_dict[i]))


def newPlayer():

    print("Enter a new player's jersey number:")

    jersey_num = int(input())

    while ((jersey_num < 0) or (jersey_num > 99)):
        print("Invalid Jersey Number! Please " +

              "enter again!")

        print("Enter a new player's jersey number:")

        jersey_num = int(input())


    print("Enter the player's rating:")

    player_rating = int(input())

    while ((player_rating < 1) or (player_rating > 9)):
        print("Invalid Rating! Please enter again!")

        print("Enter the player's rating:")

        player_rating = int(input())

    soccer_dict.update({jersey_num: player_rating})


def removePlayer():


    print("Enter a jersey number:")

    jersey_num = int(input())

    while ((jersey_num < 0) or (jersey_num > 99)):
        print("Invalid Jersey Number! Please " +

              "enter again!")

        print("Enter a jersey number:")

        jersey_num = int(input())

    if jersey_num in soccer_dict.keys():
        del soccer_dict[jersey_num]


def updateplayerRating():

    print("Enter a jersey number:")

    jersey_num = int(input())

    while ((jersey_num < 0) or (jersey_num > 99)):
        print("Invalid Jersey Number! Please " +

              "enter again!")

        print("Enter a jersey number:")

        jersey_num = int(input())


    print("Enter a new rating for player:")

    player_rating = int(input())


    while ((player_rating < 1) or (player_rating > 9)):
        print("Invalid Rating! Please enter again!")

        print("Enter a new rating for player:")

        player_rating = int(input())


    soccer_dict[jersey_num] = player_rating


def outputaboveRating():

    print("Enter a rating:")

    rating = int(input())

    while ((player_rating < 1) or (player_rating > 9)):
        print("Invalid Rating! Please enter again!")

        print("Enter a rating:")

        rating = int(input())

    print("ABOVE 5")

    soccer_list_keys = sortDictKeys()


    for i in soccer_list_keys:

        if (soccer_dict[i] > rating):

            print("Jersey number: " + str(i)

                  + ", Rating: " + str(soccer_dict[i]))


for i in range(1, 6):


    print("Enter player " + str(i) + "'s jersey number:")

    jersey_num = int(input())

    while ((jersey_num < 0) or (jersey_num > 99)):
        print("Invalid Jersey Number! Please " +

              "enter again!")

        print("Enter player " + str(i)

              + "'s jersey number:")

        jersey_num = int(input())

    print("Enter player " + str(i) + "'s rating:")

    player_rating = int(input())

    while ((player_rating < 1) or (player_rating > 9)):
        print("Invalid Rating! Please enter again!")

        print("Enter player " + str(i) + "'s rating:")

        player_rating = int(input())

    print()

    soccer_dict[jersey_num] = player_rating

rosterOutput()

print()

while (True):

    print("MENU")

    print("a - Add player")

    print("d - Remove player")

    print("u - Update player rating")

    print("r - Output players above a rating")

    print("o - Output roster")

    print("q - Quit")

    print()

    print("Choose an option:")

    user_choice = input()



    if (user_choice == 'a'):

        newPlayer()

    elif (user_choice == 'd'):

        removePlayer()

    elif (user_choice == 'u'):

        updateplayerRating()

    elif (user_choice == 'r'):

        outputaboveRating()

    elif (user_choice == 'o'):

        rosterOutput()

    elif (user_choice == 'q'):

        break

    print()