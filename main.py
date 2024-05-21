print("welcome to bill calculator")
total = float(input("what was the total bill? $"))
per = int(input("what percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("how many people to split the bill?"))
add = (total * per) / 100
totalbill = (total + add) / people
totalbill = round(totalbill, 2)
totalbill = "{:.2f}".format(totalbill)
print(f"each person should pay: ${totalbill}")
