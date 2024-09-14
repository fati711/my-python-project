#اختيار المستخدم احد الطرقتين 
import random
print("Welcome to the Coin Guessing Game!")
print("Chose a method to toss the coin:")
print("1.Using random.random()")
print("2.Using random.randint()")
choice=input("Enter your choice (1 or 2): ")
if choice =="1":
  random_computer=random.random()
  if random_computer>0.5:
    computer="head"
  else:
    computer="tails"
  
elif choice=="2":
  randint_computer=random.randint(0,1)
  if randint_computer==1:
    computer="head"
  else:
    computer="tails"
  
else:
  print("Invalid choice. Please select either 1 or 2.")

# اختيار المستخدم والمقارنة
user=input("Enter your Guess (Head or Tails): ").lower()
if user=="tails" and computer=="head":
  print("Sorry, you lost!")
else:
  print("Congratulations! You won!")
print(f"The computer's coin toss result was: {computer}")
  