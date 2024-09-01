print("\t\tWelcome to Quiz Game!!!\n")
# from quiz_DB import Question_Bank
# from quiz_DB import options

# All question created in dictionary (key:value pair) and added in a list. 
Question_Bank=[
    {"text":"The ability of one class to acquire methods and attributes from another class is called_______.\n","answer":"A"},
    {"text":"What does MRO stands for?","answer":"B"},
    {"text":"What is the depth of multi-level inheritance in python?\n","answer":"C"},
    {"text":"Diamond problem in python is addressed using which algorithm\n","answer":"A"},
    {"text":"Which of the following is a type of inheritance?\n","answer":"D"},
    {"text":"Who is the creator of python programming language?\n","answer":"B"}
]

options=[
    ["A. Inheritance,","B. Abstraction","C. Polymorphism","D. Objects\n"],
    ["A. Master Record Order","B. Method Resolution Order", "C. Method Recored Order", "D. Master Resolution Operation\n"],
    ["A. Two level","B. Three level", "C. Any level", "D. None of these\n"],
    ["A. C3 Linearization algorithm", "B. D3 Linearization Algorithm", "C. D3 Poly alogorithim", "D. E3 Linear method algorithm\n"],
    ["A. Single","B. Double","C. Multiple", "D. Both A & C\n"],
    ["A. Bjarne Stroustrup", "B. Guido Van Rossum","C. Dannis Ritchie","D. James Gosling\n"]
]
print("\t###### *** Quiz Begins *** ######\n")
score = 0
def check_ans (usr_guess, correct_ans):
    if usr_guess == correct_ans:
        return True
    else:
        return False


for ques in range(len(Question_Bank)):
    print(Question_Bank[ques]["text"])
    for i in options[ques]:
        print(i)

    guess = input("Enter your answer(A/B/C/D) : ").upper()
    is_correct = check_ans(guess,Question_Bank[ques]["answer"])
    if is_correct:
        print("Correct Answer")
        score += 1
    else:
        print("Incorrect Answer")
        print(f"The correct answer is {Question_Bank[ques]['answer']}")
    print(f"Your current score is {score}/{ques+1}")
    print("\n*************************")
print("Your final score is ",score)
print(f"Your winning percentage is {score/len(Question_Bank)*100} %")