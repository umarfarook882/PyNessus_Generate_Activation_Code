#!/usr/bin/python3
print("==================================================================")
print("  Welcome !  to  ! Nessus Home  activation code Generation ! Service ! ")
print("       Don't misuse this script other then for pentesting purpose      ")
print("                This script written  on Python 3 modules                  ")
print("                          Author:anonmech                                   ")
print("==================================================================")


from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
ht=urlopen("https://www.tenable.com/products/nessus-home")
bs=BeautifulSoup(ht,'html.parser')
for link in bs.findAll("input",{"name":"token"}):
 if 'name' in link.attrs:
   tkn=link.attrs['value']
 else:
   print("not found")
fname=input("First Name:")
lname=input("Last Name:")
email=input("Email:")
params={"first_name":fname,"last_name":lname,"email":email,"country":"IN","Accept":"Agree","robot":"human","type":"homefeed","token":tkn,"submit":"Register"}
r = requests.post("https://www.tenable.com/products/nessus-home", data=params)
bs=BeautifulSoup(r.text,'html.parser')
for link in bs.findAll("meta",{"content":"Thank you for registering for Nessus Home. An email containing your activation code has been sent to you at the email address you provided."}):
 if 'content' in link.attrs:
    print(link.attrs['content'])
 else:
    print("something went wrong")


