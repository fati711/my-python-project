#ادخال البيانات
length=float(input("Please type the length: \n"))
width=float(input("Please type the width: \n"))
price=float(input("How much for 1 meter: \n"))

#حساب المساحة
area=length*width

#حساب السعر
total_price=price*area

print(f"The total area is: {area}.0")
print(f"The total price is: {total_price}.0$")