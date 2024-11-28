print("hello world")

name = "youmad?"
input_name = input("Whats your name bruh?\nYour name: ")
print(f"Hello {input_name}.")
age_input = int(input("how old are you? "))

if(age_input > 18):
   print(f"hello {input_name}.\nyou are now {age_input}. You old ass MF.")
else:
   print(f"hello Little {input_name}.")

print(type(age_input), type(input_name))

lunch_money = float(input("How much dollar you bring 2Day?\nhow much? : "))

if(lunch_money > 100):
   print(f"You {name} rich Crazy MF! ...srr...")
elif(lunch_money > 50 and lunch_money < 100):
   print(f"You're brave to bring {lunch_money}$ to school homie {name}")
else:
   print("Poor soul, heres 20$. enjoy your afternoon buddy")
