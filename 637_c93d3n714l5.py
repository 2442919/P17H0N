#!/usr/bin/python3
#RescrieFila
import os
os.system('clear')
FirstName = input("Enter First Name:\n\n")
File = (FirstName)
with open(File, 'w') as first_name:
    first_name.write(FirstName + "\n")
os.system('clear')
LastName = input("Enter Last Name:\n\n")
with open(File, 'a+') as last_name:
    last_name.write(LastName + "\n")
os.system('clear')
DateOfBirth = input("Enter Date of Birth:\n\n")
with open(File, 'a+') as date_of_birth:
    date_of_birth.write(DateOfBirth + "\n")
os.system('clear')
PhoneNumber = input("Enter Phone Number:\n\n")
with open(File, 'a+') as phone_number:
    phone_number.write(PhoneNumber + "\n")
os.system('clear')
Email = input("Enter E-mail address:\n\n")
with open(File, 'a+') as email:
    email.write(Email + "\n")
os.system('clear')


   
