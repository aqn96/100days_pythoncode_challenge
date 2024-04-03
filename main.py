#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")

total = input("What was the total bill $?")
tip_per = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_ppl = input("How many people to split the bill? ")

total_tip = float(total) * (float(tip_per)/100)
each_tip = total_tip / int(num_ppl)
each_pay = float(total) / int(num_ppl)
each_total = each_pay + each_tip
each_total = "{:.2f}".format(each_total)

print(f"Each person should pay: ${each_total}")

