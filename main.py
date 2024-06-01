from UF3 import UF3
import random

class createQuestion:
    #Constructor sets up the UF3 object and creates a random number of unions
    def __init__(self):

        self.uf = UF3()
        self.uf.make(random.randint(3, 12))
        self.size = self.uf.size()

        print(f"A union-find instance u has been initialised with n = {self.size}.")
        self.operations = []

        #random number of unions between 2 and 5
        loops = random.randint(2, 5)
        for _ in range(loops):
            #random values to union between 0 and inital make size
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            #appends the union to the operations list
            self.operations.append(f"union({x},{y})")
            #unions the two values
            self.uf.union(x, y)

        #sets the groups variable to the number of groups in the UF
        self.groups = self.uf.groups


    #Function to return the awnser message
    def correctawswer(self,correct, awnser = False):
        if correct:
            print("Correct Answer \n")
        else:
            print(f"The correct answer is: {awnser} \n")


    #Function to ask the question and return result
    def question(self, question , check):
        print(question)
        response = input()
        self.correctawswer(response == check, check)

    #Function to ask the questions with randon values
    def askQuestion(self):
        self.question(f"At this point, before any calls to union have been made, how many different values does find have?", str(self.size))

        #prints all the union operations
        for i in self.operations:
            print(i)
        print(" \n")

        #random value to ask the user what the value of find is
        valueQuestion = random.randint(0, self.size -1)
        self.question(f"What is the value of find({valueQuestion})?", str(self.uf.find(valueQuestion)))

        #question to ask the user how many unique groups there are
        self.question("How many groups are there?", str(self.groups))


        #finds the largest group and counts how many are in that group
        largestGroup = self.uf.rank.index(max(self.uf.rank))
        count = 0
        for i in self.uf.reps:
            if self.uf.reps[i] == largestGroup:
                count += 1

        #asks the user how many elements are in the largest group
        self.question(f"What is {largestGroup}'s group size?", str(count))


    #Function to run the program and print finial UF once the questions are asked
    def run(self):
        self.askQuestion()
        #prints the final UF to show what has happened,
        print(self.uf)












x = createQuestion()
x.run()