import random
sub = random.randint(0,50)
inp = random.randint(0,100) + sub
end = random.randint(0,20)
print("Guess a number in my mind")
print("if you are smart or smarter than me(computer)")
name = input("your name: ")
count = 0
while True:
	inpu = int(input("guess = "))
	count += 1
	if inpu == ' ':
			print("dummy,input a numeric value")
	elif inpu != inp:
		print("Wrong!,",name,"you are not even smart!")
		if count == 2:
			print(name,"try harder")
		if count == 6:
			print(name,"i taught you are a smart person")
		if count == 10:
			print(name,"are you sure you can do better!? ")
		if inpu > inp:
			print(" HINT : The number is smaller ... ")
			print(" HINT : The number was sumed with ", sub)
		if count > 15:
			print(name,"You are even worst and poor intellectually, you have attempted it with HINT for",count,'times')
			print("and still not gotten it right")
			print(name,"I know you will fail Succesfuly?")

		if count == end:
			print("Time UP!!!")
			print(name,"You Succesfuly Failed the test!")
			print("It shows you are not smarter and intelligent than me!")
			print("well the number i was intelligently thinking of was",inp)
			print("only God knows if you will win in your next play")
			print("try again for loosing!? else, you are a looser")
			quit()
	else:
		print("correct!, you guessed it right")
		print("try again to prove how dynamic you can analyse")
		quit()
