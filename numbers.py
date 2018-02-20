
import random


min = 0
max = 12
no_of_tries = 3
t = 1
secret = random.choice(range(min, max))

print("can you guess my number" + "\n")
while True:
	guess = input("try: ")
	
	try:
		guess = int(guess)
	except:
		print("try a number instead")
		break
		
	if guess == secret:
		print("score! you guessed my number.")
		print("tries:", t)
		break
	
	elif t == no_of_tries:
		print("run out of tries, did you")
		print("my number was", secret)
		break
	
	elif guess > secret:
		print("a little bit lower\n")
		t += 1
	
	elif guess < secret:
		print("a tad higher\n")
		t += 1
