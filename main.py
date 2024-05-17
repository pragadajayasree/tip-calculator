#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("welcome to bill calculator")
total=float(input("what was the total bill? $"))
per=int(input("what percentage tip would you like to give? 10, 12, or 15?"))
people=int(input("how many people to split the bill?"))
add=(total*per)/100;
totalbill=(total+add)/people
totalbill=round(totalbill,2)
totalbill="{:.2f}".format(totalbill)
print(f"each person should pay: ${totalbill}")
