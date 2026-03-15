from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface
from settings import QuizSettings

settings = QuizSettings()
parameters = settings.get_parameters()


response = requests.get("https://opentdb.com/api.php",parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)

