import random 

toprange = input("Type a number: ")

if toprange.isdigit():
    toprange= int(toprange)

    if toprange <= 0:
        print("please type a number larger than 0")
        quit()
        
else: 
    print("please type a number")        
    quit()

random_number = (random.randint(0, toprange))
print(random_number)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)       
    else: 
        print("please type a number")        
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    else:
        print("Not this time!")    

print ("You got it in", guesses, "guesses ")        