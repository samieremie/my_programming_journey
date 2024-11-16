# This is my first very very simple game

questions = [

    {
        "question": "Which country has the highest life expectancy?",
        "options": ["A. Hong Kong", "B. Belgium", "C. Romania", "D. USA"],
        "answer": "A",
    },
    {
        "question": "How many minutes are in a full week?",
        "options": ["A. 4800", "B. 6200", "C. 7600", "D. 10,080"],
        "answer": "D",
    },
    {
        "question": "What is acrophobia a fear of?",
        "options": ["A. Depths", "B. Heights", "C. Spins", "D. Acrobranches"],
        "answer": "B",
    },
    {
        "question": "What phone company produced the 3310?",
        "options": ["A. Nokia", "B. Smart", "C. Samnsung", "D. Apple"],
        "answer": "A",
    },
]

def run_quizz(list_questions):

    total = 0 # Holds the total amount of questions
    final_score = 0 # Holds the score of the player
    print("Welcome to the quizz game of Samuel! \n")
    for question in list_questions:
        total += 1
        print(f"This is the question number: {total} \n")
        print(question["question"])
        for option in question["options"]:
            print(option)
        
        # Prompt the player for input. 
        prompt = "Choose an answer from A, B, C, D. \n"
        prompt += "If you want to quit press q\n"
        answer = input(prompt)

        # If the answer is correct add 1 to the final score.
        # make the comparison case insensitive
        if answer.lower() == 'q':
            print("Hope to see you back")
            return None
        elif answer.lower() == question["answer"].lower():
            final_score += 1
    
    result = final_score / total

    if result < 0.5:
        print("You don't have a lot of common knowledge, keep improving.")
        print(f"Your score was: {final_score} / {total}")
    else:
        print("Congratulations.")
        print(f"Your score was: {final_score} / {total}")


run_quizz(questions)

