my_number = 3
number_guessed = 0

while number_guessed != my_number:
    number_guessed = raw_input("Guess my number (between 1 and 5):")
    number_guessed = int(number_guessed)

print "You are right! My number was " + str(my_number) + "!"
