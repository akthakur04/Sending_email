'''import smtplib
mail=smtplib.SMTP("smtp.gmail.com",587)
mail.starttls()
mail.login("akshay11042000@gmail.com","agentat12_12")
subject="sending mail through python"
body="hey this mail is send through python \ndont reply to tis msg "
message="Subject : {}\n\n{}".format(subject,body)

listofaddress=["akshay.181004@gmail.com","thakurakshay10thb@gmail.com","pooja.181047@gmail.com","kundan.181033@gmail.com"]
mail.sendmail("akshay11042000",listofaddress,message)
mail.quit()
print("mailed successful")
'''
import pandas as pd
import smtplib
#connect gmail
mail=smtplib.SMTP("smtp.gmail.com",587)
mail.starttls()
mail.login("akshay11042000@gmail.com","agentat12_12")

#write msg
subject="sending mail through python"
body="hey this mail is send through python \ndont reply to tis msg "
message="Subject : {}\n\n{}".format(subject,body)

#add recipents
df=pd.read_csv("mail.csv")
emails=df['mails']


#send mails
for i in range(len(emails)):
    mail.sendmail("akshay11042000",emails[i],message)
#quit server
mail.quit()

#print on console
print("mailed successful")

