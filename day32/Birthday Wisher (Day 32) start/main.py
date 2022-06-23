# import smtplib

# my_email = "myemail@gmail.com"
# password = "12345asdf12345"


# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls() # makes connection secure
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="example@gmail.com", 
#         msg="Subject:Hello\n\nThis is the body of the email."
#     )



import datetime as dt

now = dt.datetime.now()
year = now.year
if year == 2020:
    print("wear a mask")
day_of_the_week = now.weekday()
print(day_of_the_week)

date_of_birth = dt.datetime(year=1997, month=11, day=8, hour=4)
print(date_of_birth)