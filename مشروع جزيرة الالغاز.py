#ترحيب بالمستخد
print("""
──▄────▄▄▄▄▄▄▄────▄───
─▀▀▄─▄█████████▄─▄▀▀──
─────██─▀███▀─██──────
───▄─▀████▀████▀─▄────
─▀█────██▀█▀██────█▀──

""")
print("Welcome to my island!")
print("There are two doors in front of you. 🚪 a red door 🚪 a blue door")
choice=input("Wich door do you want to open? ").lower()


#التحقق من اختيار المستخدم
if choice=="blue":
  print("Oops! You chose the crocodile door.")
  print("Game over! 🐊 🐊 🐊")
elif choice=="red":
  print("Great! now you entered a room.")
  print("You found three boxes: 🎁 white, 🎁 black, 🎁green")

  #التحقق المرة الثانية من اختيار المستخدم
  choice_box=input("Wich box do you open? ").lower()
  if choice_box=="white":
    print("Oops! You opened a box filled with snakes 🐍🐍🐍")
  elif choice_box=="black":
    print("Oops! you opened a box filled with spiders🕷️🕷️🕷️")
  elif choice_box=="green":
    print("Congratulations! You found the treasure! 💰💰💰")
  else:
    print("Invalid choice! 🤷‍♂️♂️ 🤷‍♂️♂️ 🤷‍♂️♂️")

else:
  print("Invalid choice! 🤷‍♂️♂️ 🤷‍♂️♂️ 🤷‍♂️♂️")

