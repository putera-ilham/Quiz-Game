from question_model import Qn
from data import question_data
from quiz_brain import QzBr


qn_bank = []

for q in question_data:
    quest_text = q["question"]
    quest_ans = q["correct_answer"]
    new_q = Qn(quest_text, quest_ans) # OBJ WITH
    # QUESTIONS AND ANSWERS (ATTRIBUTES) ASSIGNED TO THE OBJ.
    qn_bank.append(new_q)


qz = QzBr(qn_bank)

while qz.cont_qn(): # till there are no more questions
    qz.next_qn()


print("You've completed the quiz")
print(f"Your final score was: {qz.score}/{qz.quest_num}")