import smtplib

my_Email = "utkarshmajumdar2607@gmail.com"
password =""
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_Email,password=password)
connection.sendmail(from_addr=my_Email, to_addrs="majumdar_utkarsh@srmap.edu.in", msg="Hello")
