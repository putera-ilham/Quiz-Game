class QzBr:

    def __init__(self, q_list):
        self.quest_num = 0
        self.score = 0
        self.quest_list = q_list

    ### METHOD 1 ###
    def next_qn(self):
        curr_quest = self.quest_list[self.quest_num]
        self.quest_num += 1
        user_ans = (
            input(f"Q.{self.quest_num}: {curr_quest.text} (True/False)"))
        self.check_qn(user_ans, curr_quest.answer)

    ### METHOD 2 ###
    def cont_qn(self):
        return self.quest_num < len(self.quest_list) # will return either True or False
        # thus only this statement is needed

    ### METHOD 3 ###
    def check_qn(self, user_ans, corr_ans):
        if user_ans.lower() == corr_ans.lower():
            self.score += 1
            print("You got it!")
        else:
            print("You're wrong")
        print(f"The correct answer was {corr_ans}.")
        print(f"Your current score is: {self.score}/{self.quest_num}")
        print("\n")


