import random #imports random
#Random Word Generator. Spits out 2 words
adjectives = ["parched", "bright", "clumsy", "lucky", "absurd", "materialistic", "instinctive", "amusing", "narrow", "thoughtful", "vengeful", "huge"] #list for adjectives
nouns = ["Backpack", "Brush", "Bulb", "Childhood", "Execution", "Festival", "Owl", "Shampoo", "Suet", "Widget", "Author", "Tanker"]#list for nounts

print("This Generator will give you two random words, one adjective and one noun to hopefully give you inspiration to write something")#Prints options for user

uOption = input("Please press 'x' to continue with this process or press 'n' to cancel this process.")#asks user for input

if uOption == 'x': #an if statement for if user wants to proceed
    a = (random.choice(adjectives))
    n = (random.choice(nouns)) #takes a random word from the respective list
    print(a, " ",n)#prints a random adjective and noun
else: #if uOption != 'x' then will move to an else statement
    print("Goodbye")#prints goodbye

