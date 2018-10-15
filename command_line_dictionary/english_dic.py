import json
from difflib import get_close_matches

#loading the data from the json file
with open("076 data.json") as data_file:
    data = json.load(data_file)


def definitions(the_word):
    the_definitions = "\n"
    #unpacking the definitions from the list and arranging them in order
    for count, definition in enumerate(data[the_word], 1):
        the_definitions += "Definition {}: {}\n".format(count, definition)
    return the_definitions


def find_word():
    #keep on looping if the right input is not entered
    while True:
        the_word = input("Please enter a word to find: ").lower()
        #if the input is a valid string
        if the_word.isalpha():
            if the_word in data.keys():
                return definitions(the_word)
            #if not found in the data and found close matches using len()
            elif len(get_close_matches(the_word, data.keys())) > 0:
                #keep on looping if the right input is not entered
                while True:
                    #yes or not
                    input_1 = input("\nDid you mean {} instead?\nEnter Yes or No [Y/N]: ".format(
                        get_close_matches(the_word, data.keys())[
                            0])).lower()

                    if input_1[0] == "y":
                        return definitions(get_close_matches(the_word, data.keys())[0])

                    elif input_1[0] == "n":
                        input_2 = input("\nDid you mean {} instead?\nEnter Yes or No [Y/N]: ".format(
                            get_close_matches(the_word, data.keys())[
                                1])).lower()

                        if input_2[0] == "y":
                            return definitions(get_close_matches(the_word, data.keys())[1])

                        elif input_2[0] == "n":
                            return "\n{} not found in the dictionary".format(the_word)
                        #if it is not the string inputed does not start with y or n
                        else:
                            print("\nPlease again by entering yes/no or Y/N")
                    #if it is not the string inputed does not start with y or n
                    else:
                        print("\nPlease again by entering yes/no or Y/N")
            else:
                return "\n{} not found in the dictionary".format(the_word)

        elif the_word == "":
            print("\nThere is no word that was entered, please try again\n")
        else:
            print("\nPlease enter an word instead of a number, please try again\n")


print(find_word())

