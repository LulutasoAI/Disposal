import random
class Persona_Generator():
    "I thought This was a good idea but this is useless as something I can not even remember for once in my life"
    def __init__(self):
        self.name = self.pickone_from_list(["Aren", "Naron","Sharon"])
        self.age = random.randint(15, 100)
        self.sex = self.pickone_from_list(["male", "female", "else"])
        self.place = random.randint(1,47)
        self.job = self.pickone_from_list(["Academia", "IT", "Sales", "Physical", "Office","CEO", "Executive"])
        self.income = random.randint(1000000, 20000000) #We have to Choose statistically
        self.family_members_num = random.randint(1,5)
        self.personality = self.pickone_from_list(["Consumer", "Creative", "Educated", "Not Educated"])
        self.goals = self.pickone_from_list(["Family", "Money", "Productivity", "Serve", "FIRE"])
        self.lifeStyles = self.pickone_from_list(["Student", "Labour"])
        self.value = self.pickone_from_list(["Money", "Family", "Win", "Helping others", "selfish"])
        self.Hobbies = self.pickone_from_list(["Sport", "Indoor", "Outdoor", "pets"])
        self.Consume_tendency = self.pickone_from_list(["paycheck to paycheck", "saves money" ])
        self.information_gathering = self.pickone_from_list(["SNS", "Internet surfing", "PC", "Mobile", "Social", "Realworld"])

        itnorm_capital, itnorm_norm, itobject, itown, itown_capital = self.how2call_gen(self.sex)

        print("{} name is {}.".format(itown_capital,self.name))
        print("{} age is {}.".format(itown_capital,int(self.age)))
        print("{} lives in {}".format(itnorm_capital,self.place))
        print("{} job is {}".format(itown_capital,self.job))
    def pickone_from_list(self,alist):
        outcome = alist[random.randint(0,len(alist)-1)]
        return outcome

    def how2call_gen(self,sex):
        if sex == "male":
            itnorm_capital = "He"
            itnorm_norm = "he"
            itobject = "him"
            itown = "his"
            itown_capital = "His"
        elif sex == "female":
            itnorm_capital = "She"
            itnorm_norm = "she"
            itobject = "her"
            itown = "her"
            itown_capital = "Her"
        elif sex == "else":
            itnorm_capital = "They"
            itnorm_norm = "they"
            itobject = "them"
            itown = "their"
            itown_capital = "Their"
        else:
            itnorm_capital = "They"
            itnorm_norm = "they"
            itobject = "them"
            itown = "their"
            itown_capital = "Their"

        return itnorm_capital, itnorm_norm, itobject, itown, itown_capital

if __name__ == "__main__":
    num = Persona_Generator()
