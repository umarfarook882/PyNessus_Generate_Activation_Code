from bs4 import BeautifulSoup
import requests
import time
import re
from tempmail import TempMail
import os
import sys

def banner():
	print("==================================================================")
	print("            Generate Multiple Nessus Activation code                       ")
	print("   Don't misuse this script other then for Pentesting purpose              ")
	print("                      \033[1;31;10mBy:Fools of Security :)\033[1;31;0m     ")
	print("==================================================================")


def nessus_activation():
	tmp = TempMail()
	email = tmp.get_email_address()  
	print("Your Temp mail address is successfully created!")
	print ("Email Address: "+ email)
	# print tmp.get_mailbox(email)  
	#Nessus Registeration Form
	print ("\033[1;32;10mNessus Registeration Form \033[1;32;0m")
	ht=requests.get("https://www.tenable.com/products/nessus-home")
	bs=BeautifulSoup(ht.text,'html.parser')
	for link in bs.findAll("input",{"name":"token"}):
	 if 'name' in link.attrs:
	   tkn=link.attrs['value']
	 else:
	   print("not found")
	fname=raw_input("First Name:")
	lname=raw_input("Last Name:")
	# nes_email=raw_input("Email:")
	params={"first_name":fname,"last_name":lname,"email":email,"country":"IN","Accept":"Agree","robot":"human","type":"homefeed","token":tkn,"submit":"Register"}
	r = requests.post("https://www.tenable.com/products/nessus-home", data=params)
	if r.status_code == 200:
		bs=BeautifulSoup(r.text,'html.parser')
		keyword=bs.find("title").get_text()
		success=keyword.split('|')
		if str(success[0][:-1]) == 'Thank You for Registering for Nessus Home!':
			print('\033[1;32;10m'+str(success[0][:-1])+'\033[1;32;0m')
			while  True:
				if tmp.get_mailbox(email):
					for emails in tmp.get_mailbox(email):
						if emails['mail_subject'] == 'Tenable Nessus Home Activation Code':
							message=emails['mail_text']
							receive=raw_input("To check for Nessus Activation Code in Inbox, press enter")
							regex = r"\w{4}(?:-\w{4}){4}"
							activation_code=re.search(regex,message)
							print('\033[1;32;10mNessus Activation Code is:\033[1;32;0m'+activation_code.group())
							sys.exit()
				else:
					print ('There are no emails yet....')

		elif bs.find('span',{"style":"color:#FF0000;"}).get_text():
			os.system('clear')
			# print('\033[1;31;10m'+bs.find('span',{"style":"color:#FF0000;"}).get_text()+'\033[1;31;0m')
			print('\033[1;31;10m Sorry, This Email Address is already Registered for Nessus Activation Code\033[1;31;0m')
			print("Wait..Regenerating new Temp email address")
			nessus_activation()
	else:
		print("something went wrong with the request")
		sys.exit()


if __name__ == "__main__":
	banner()
	nessus_activation()

