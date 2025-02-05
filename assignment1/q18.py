"""A library charges a fine for every book returned late. For first5 days, the fine is 50 paise,
for 6-10 days fine is one rupee and above 10 days fine is 5 rupees. If you return the book
after 30days your membership will be cancelled. Write a program to accept the number
of days the member is late to return the book and display the fine or the appropriate
message."""


days = int(input("Enter the Number of Days :"))
if (days>0 and days<= 5):
	amount = 0.50 * days
	print("Fine Amount Rs :", amount)
 
elif(days >= 6 and days <= 10):
	amount = 1 * days
	print("Fine Amount Rs :", amount)
 
elif (days > 10):
	amount = 5 * days
	print("Fine Amount Rs :", amount)
	if (days > 30):
		print("Your membership is Cancelled..")
else:
	print("Invalid")