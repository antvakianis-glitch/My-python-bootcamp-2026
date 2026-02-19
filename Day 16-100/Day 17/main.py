from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question = Question(question["text"], question["answer"])
    question_bank.append(question)


quiz = QuizBrain(question_bank)
quiz.next_question()
while quiz.still_has_question():
    quiz.next_question()
print("You have completed the Quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")




#for question in question_bank:
#    print(question.text)
#    my_answer = input("Enter your answer: 'True' or 'False'")
#    if my_answer.lower() == question.answer.lower():
#        score += 1
#        print(f"Correct the answer is:{question.answer}. Your current score: {score}")
#    else:
#        print(f"Wrong answer! The answer is:{question.answer}. Your current score: {score}")
#
#print(f"\n Quiz Complete! Final Score: {score}/{len(question_bank)}")


