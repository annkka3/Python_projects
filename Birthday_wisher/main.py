import smtplib
import datetime as dt
import random as rd
import pandas as pd

my_email = "annagromyko88@gmail.com"
password = '***********'


with open(f'letter_templates/letter_{rd.randint(1,3)}.txt') as letter:
    wish = letter.readlines()


def send_email():
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email_to_send,
                            msg=f'Subject:HAPPY BIRTHDAY! \n\n {"".join(wish).replace("[NAME]", name)}')

now = dt.datetime.now()
month = now.month
day = now.day

birthdays = pd.read_csv("birthdays.csv")

for i in range(len(birthdays)):
    if birthdays["month"][i] == month and birthdays["day"][i] == day:
        email_to_send = birthdays["email"][i]
        name = birthdays["name"][i]
        send_email()
