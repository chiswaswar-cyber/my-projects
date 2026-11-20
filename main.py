import os
import smtplib
import datetime as dt
import random
my_email = "chiswaswar@gmail.com"
receiver_email = "esthersitangaika@gmail.com"
my_password =os.environ.get("MY_PASSWORD")
now = dt.datetime.now()
weekday = now.weekday()
with open("quote.txt", encoding="cp1252") as quote_file:
    all_quotes = quote_file.readlines()
    quote=random.choice(all_quotes)
print(quote)

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=receiver_email,
        msg=f"From: {my_email}\nTo: {receiver_email}\nSubject:Be Motivated!\n\n{quote}".encode("utf-8")
                        )
print("Email sent!")
