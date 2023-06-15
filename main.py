##################### Extra Hard Starting Project ######################

# -------------------------------- IMPORTS ----------------------------- #
import datetime as dt
import smtplib
import random
import pandas

# -------------------------------- CONSTANTS ----------------------------- #
LIST_OF_LETTERS = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]


# 1. Update the birthdays.csv

# TODO 2. Check if today matches a birthday in the birthdays.csv
with open("birthdays.csv") as birthdays_file:
    birthdays_dataframe = pandas.read_csv(birthdays_file)
    birthday_list = birthdays_dataframe.to_list()
    print(birthdays_dataframe)

# TODO 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# TODO 4. Send the letter generated in step 3 to that person's email address.

# -------------------------------- CONSTANTS ----------------------------- #




