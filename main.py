
import datetime as dt
import random
import smtplib
import pandas as pd


EMAIL = "aigboje.python@gmail.com"
PASSWORD = "odjieouhexbefofu"

now = dt.datetime.now()
today_year = now.year
today_month = now.month
today_day = now.day

today_date = (today_month, today_day)

birthday_list = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthday_list.iterrows()}

if today_date in birthdays_dict:
    birthday_person = birthdays_dict[today_date]
    file_to_send = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_to_send) as birthday_msg:
        msg_contents = birthday_msg.read()
        meg_contents = msg_contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=birthday_person.email,
            msg=f"Subject: HAPPY BIRTHDAY\n\n {meg_contents}"
        )

