#!/usr/bin/python3
print("==================================================================")
print("            Welcome !  to  ! Temp Mail ! Service ! ")
print("   Don't misuse this script other then for pentesting purpose  ")
print("            This script written  on Python 3 modules                  ")
print("                      Author:anonmech                             ")
print("==================================================================")
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
session = requests.Session()
ht=session.get("https://temp-mail.org/en/option/change")
bs=BeautifulSoup(ht.text,'html.parser')
#print("Cookie is set to:")
#print(ht.cookies.get_dict())
for  link in bs.findAll("input",{"name":"csrf"}):
  if 'name' in link.attrs:
   token=link.attrs['value']
   print("Csrf token is ",token)
  else:
   print("somethings went wrong")
mail_id=input("Choose Your Mail ID:")
print("@polyfaust.com\n@cartelera.org")
domain_name=input("Choose Your Mail Domain:")
params={"csrf":token,"mail":mail_id,"domain":domain_name}
r=session.post("https://temp-mail.org/en/option/change",params)
bs=BeautifulSoup(r.text,'html.parser')
for link in bs.findAll("button",{"data-dismiss":"alert"}):
  if 'data-dismiss' in link.attrs:
     print("The mail address is successfully created!")
     print("your mail id is" +mail_id+domain_name)
  else:
     print("somethings went wrong")
receive=input("if you read to recieve mail then press enter")
ht=session.get("https://temp-mail.org/en/")
bs=BeautifulSoup(ht.text,'html.parser')
for link in bs.findAll("a",{"title":"Tenable Nessus Home Activation Code"}):
  if 'title' in link.attrs:
     url=link.attrs['href']
     print(url)
  else:
      print("somethings went wrong")
url1=str(url)
ht=session.get(url1)
bs=BeautifulSoup(ht.text,'html.parser')
message=bs.findAll("div",{"data-x-div-type":"body"})
for msg in message:
     print(msg.get_text())

