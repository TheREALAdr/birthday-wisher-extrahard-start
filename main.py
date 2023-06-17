##################### Extra Hard Starting Project ######################

# ------------ IMPORTS -------------- #
import pandas
import random
import datetime as dt
import smtplib

gmail_testing_acc = "obviouslyafakeemailbroski@gmail.com"
gmail_app_password = "vqtlvqzpnjhufmto"

yahoo_testing_acc = "testing_468@yahoo.com"

birthday_person = ""
list_of_letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
# 1. Update the birthdays.csv
with open("birthdays.csv") as birthdays_file:
    birthdays_dataframe = pandas.read_csv(birthdays_file)

birthday_names_list = birthdays_dataframe.name.to_list()

birthday_month_list = birthdays_dataframe.month.to_list()

birthday_day_list = birthdays_dataframe.day.to_list()

birthday_month_dictionary = {day: month for day, month in zip(birthday_names_list, birthday_month_list)}

birthday_day_dictionary = {name: day for name, day in zip(birthday_names_list, birthday_day_list)}

current_month = dt.datetime.now().month
current_day = dt.datetime.now().day

print(current_month, current_day)

def is_birthday():
    global birthday_person
    for name in birthday_names_list:
        if birthday_month_dictionary[name] == current_month:
            if birthday_day_dictionary[name] == current_day:
                birthday_person = name
                return True


# 2. Check if today matches a birthday in the birthdays.csv (Try Catch needed?)


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if is_birthday():
    random_letter = random.choice(list_of_letters)
    with open(f"letter_templates/{random_letter}") as letter_file:
        chosen_letter = letter_file.read()
    edited_chosen_letter = chosen_letter.replace("[NAME]", birthday_person)
    print(edited_chosen_letter)

# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=gmail_testing_acc, password=gmail_app_password)
        connection.sendmail(from_addr=gmail_testing_acc,
                            to_addrs=yahoo_testing_acc,
                            msg=f"Subject:Birthday Message!\n\n{edited_chosen_letter}")




