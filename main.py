from UF3 import UF3
import random

class createQuestion:
    #Constructor sets up the UF3 object and creates a random number of unions
    def __init__(self):
        self.uf = UF3()
        self.uf.make(random.randint(3, 12))
        print(self.uf)
        self.size = self.uf.size()

        loops = random.randint(2, 5)
        for _ in range(loops):
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            print(f"union({x},{y})")
            self.uf.union(x, y)

        self.groups = self.uf.groups


    #Function to return the awnser message
    def correctawswer(self,correct, awnser = False):
        if correct:
            print("Correct Answer")
        else:
            print("The correct answer is: " + awnser)


    #Function to ask the question and return result
    def question(self, question , check):
        print(question)
        response = input()
        self.correctawswer(response == check, check)

    #Function to ask the questions with randon values
    def askQuestion(self):
        #Question One (value of random number)
        valueQuestion = random.randint(0, self.size -1)
        self.question(f"What is the value of find({valueQuestion})?", str(self.uf.find(valueQuestion)))

        #Question Two (group count)
        self.question("How many groups are there?", str(self.groups))



        #Question Three (largest group size)
        largestGroup = self.uf.rank.index(max(self.uf.rank))
        count = 0
        for i in self.uf.reps:
            if self.uf.reps[i] == largestGroup:
                count += 1

        self.question(f"What is {largestGroup}'s group size?", str(count))


    #Function to run the program and print finial UF once the questions are asked
    def run(self):
        self.askQuestion()
        print(self.uf)












x = createQuestion()
x.run()