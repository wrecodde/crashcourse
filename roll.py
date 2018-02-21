# lets roll a die

import random


def roll(sides=6, dice=1):
	results = []
	for i in range(dice):
		tab = random.choice(range(1, sides+1))
		results.append(tab)
	print("\tcast:", results)

print("roll a die (sim)")
print("""usage
	t: terminate
	r: roll your everyday die
	c: customize your die""")

while True:
	task = input("\ntask: ")
	if task == "t":
		print("say nada")
		break
	
	elif task == "r":
		print("rolling a single 6-sided die")
		roll()
	
	elif task == "c":
		print("going custom")
		try:
			sides = int(input("sides: "))
			dice = int(input("die count: "))
			roll(sides, dice)
		except:
			raise
			# print("input numbers!")
			continue
	
	else:
		print("couldnt parse that")