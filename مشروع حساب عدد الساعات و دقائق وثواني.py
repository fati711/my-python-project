#ادخال عدد الثواني
seconds=int(input("Enter the number of seconds: "))


#حساب عدد الساعات ودقائق والثواني
hours=seconds//3600
minutes=(seconds%3600)//60
second=seconds%60

#عرض عدد الساعات ودقائ و الثواني
print(f"The time is: {hours} hours, {minutes} minutes and {second} seconds along")