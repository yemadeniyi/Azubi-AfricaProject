print("Welcome to Ecobank!!!")

first_name = input("Please, enter your first name? ")

print("Hello" + " " + first_name + ", Welcome.")

second_name = input("Please, enter your last name? ")

print("Thank you," + " " + first_name + " " + second_name  + " ")

account_no = int(input("Please enter your account no? "))
str_account = str(account_no)
print( first_name + ", " + "your account number is " + str_account + " .")

if len(str(account_no)) == 8 :
    print ("Account number is good")
else:
    print ("Account number is wrong")

y = int(str(str_account)[:2])

if y == 11:
       print ("Your account is a Savings Account")
       print ("Your account balance is ------, thank you.")

elif y == 22:
       print ("Your account is a Current Account")
       print ("Your account balance is ------, thank you")

else: 
      print ("I cant help you")   

#elif account_no = (11**):
    #print ("Your account is a Current Account")
    #print ("Your account balance is ------, thank you")

#
    
