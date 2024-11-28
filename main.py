import math
#print("hello world")

#name = "youmad?"
#input_name = input("Whats your name bruh?\nYour name: ")
#print(f"Hello {input_name}.")
#age_input = int(input("how old are you? "))

#if(age_input > 18):
   #print(f"hello {input_name}.\nyou are now {age_input}. You old ass MF.")
#else:
   #print(f"hello Little {input_name}.")

#print(type(age_input), type(input_name))

#lunch_money = float(input("How much dollar you bring 2Day?\nhow much? : "))

#if(lunch_money > 100):
   #print(f"You {input_name} rich Crazy MF! ...srr...")
#elif(lunch_money > 50 and lunch_money < 100):
   #print(f"You're brave to bring {lunch_money}$ to school homie {input_name}")
#else:
   #print("Poor soul, heres 20$. enjoy your afternoon buddy")

##arithmatics Trying

#friends = 50

#print(friends)
#friends += 1

#friends *= 99
#print(friends)
#friends /= 34
#friends **= 3
#friends %= 7
#print(friends)


x = 4.14159264395151
y = 4.5
z = -5

#result = round(x)
#result = abs(z)
#result = pow(y, x)
#result = max(x, y, z)
#result = min(x,y,z)
#print(result)

##From math.py

x = 4.14159264395151
y = 4.5
z = -5

#print(math.pi)
#print(math.e)
#result = math.sqrt(x)
#result = math.ceil(x)
#result = min(math.ceil(x), y, z)
#result = math.floor(y) 

#crl = float(input("what da radious of ya circle?\nRadious: "))

#print( f" Your Ciecle area are: {pow(crl, 2)* math.pi}" )
#print( f" Your Ciecle Circom are: {(math.pi*2) * crl}" )

pita = float(input("Pls twell mwe what is side A (Shortest): "))
pitb = float(input("Pls twell mwe what is side B (Second - shortest): "))

print(f"Your loggest side are: {math.sqrt(pow(pita, 2) + pow(pitb, 2))}")