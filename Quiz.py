quizList = {
    "1" : ['\nWhat is your name?', 'where do you live?', 'How old are you?'],
    "2" : ['Name a fruit that starts with the letter A', 'Name one yellow fruit']
}

correct = "Yeay, You answer is Correct. Goodjob!"
wrong = "Sorry, Your answer is wrong. Try again later!"

print("==========")
print("Select your quiz: ")
print("1. Personal Quiz")
print("2. Fruit Quiz")
print("==========")

selects = input('Choose ur number: ')

if selects == '1':
    print(quizList['1'][0])
    a = input('Enter your Answer: ')
    print("Helo " + a + "Nice to meet you!" + "\n")
    print(quizList['1'][1])
    b = input('Enter your Answer: ')
    print("Your live in " + b + "\n")
    print(quizList['1'][2])
    c = input('Enter your Answer: ')
    print("Your age is " + c + " Years old")

elif selects == '2':
    print(quizList['2'][0])
    a = input('Enter your answer here: ')
    if a == 'Apple':
        print(correct + "\n")
    elif a == 'Avocado':
        print(correct + "\n")
    else:
        print(wrong + "\n")
    print(quizList['2'][1])
    b = input('Enter your answer here: ')
    if b == 'Banana':
        print(correct)
    else:
        print(wrong)
else:
    print('\nWe do not have more questions')