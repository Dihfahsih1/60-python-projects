from Questions import Questions

#a list of questions
questions_prompts =[
    "What colour are Apples?\n(a) Red/Green \n(b) Purple\n(c) Orange\n\n",
    
    "What colour are Bananas?\n(a) reen \n(b) Mangenta\n(c) Yellow\n\n",
    
    "What colour are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Questions(questions_prompts[0], 'a'),
    Questions(questions_prompts[1], 'c'),
    Questions(questions_prompts[2], 'b')
]

def run_tests(questions):
    score = 0
    for question in questions:
        answer = input(question.prompts)
        if answer == question.answers:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) +" corect")
    
run_tests(questions)