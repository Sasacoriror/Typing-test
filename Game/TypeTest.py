import time
import json
import os
from matplotlib import pyplot as plt
from Texts.English import english
from Texts.Norwegian import norwegian
from Texts.German import german
from Texts.Bosnian import bosnian


class typeTest:

    #Stats holds the data for the round data to store in file
    stats = {}
    #Stats1 holds the data for the plot bar
    stats1 = {}

    def textChocie(self):

        #Calls the method that prints out the top 3 players
        self.scores_load(3)
        print(" ")

        #List of languages the user can choose from
        languages = ["english", "norwegian", "bosnian", "german"]

        print("We have multiple languages to choose from")
        #User can choose the language they want thei text in
        choiche = input("Choose between english, norwegian, bosnian, german: ")

        #Incase they write something that does not match the languages in the list
        if choiche not in languages:
            while True:
                print(f"You chose '{choiche}' thats not an option")
                choiche = input("Choose between english, norwegian, bosnian, german: ")
                #If the language you chose is in the list the loop breaks
                if choiche in languages:
                    break

        #Input gamer name
        name = input("Your game name or real name: ")

        #How many rounds you want to play
        rounds = int(input("How many rounds do you want to play: "))
        #your language choiche
        if choiche == "english":
            #Tells you to get ready
            input("Press 'Enter' when ready")
            #Takes you name, language and rounds to play
            self.type_Test(choiche, rounds, name)
        elif choiche == "norwegian":
            input("Press 'Enter' når du er klar")
            self.type_Test(choiche, rounds, name)
        elif choiche == "bosnian":
            input("Pritisnite 'Enter' kada ste spremni")
            self.type_Test(choiche, rounds, name)
        elif choiche == "german":
            input("Drücken Sie die 'Eingabetaste', wenn Sie fertig sind")
            self.type_Test(choiche, rounds, name)

    def type_Test(self, language, rounds, name):

        fullTime1 = 0
        accuracy1 = 0
        wpm = 0


        for i in range(1, rounds + 1):
            instanceA = english()
            instanceB = norwegian()
            instanceC = german()
            instanceD = bosnian()

            setning = instanceA.__str__()
            setning1 = instanceB.__str__()
            setning2 = instanceC.__str__()
            setning3 = instanceD.__str__()

            if language == "english":
                print(setning)
                text = "Write here: "

            elif language == "norwegian":
                print(setning1)
                text = "Skriv her: "

            elif language == "german":
                print(setning2)
                text = "Hier schreiben"

            elif language == "bosnian":
                print(setning3)
                text = "pisite ovdje"

            print(text)

            time1 = time.time()
            typeTest = input(str())
            time2 = time.time()

            print(" ")

            fullTime2 = time2 - time1
            fullTime1 += fullTime2

            words = typeTest.split()
            written_Corectly = 0

            for word in words:
                if language == "english":
                    if word in setning.split():
                        written_Corectly += 1
                elif language == "norwegian":
                    if word in setning1.split():
                        written_Corectly += 1
                elif language == "german":
                    if word in setning2.split():
                        written_Corectly += 1
                elif language == "bosnian":
                    if word in setning3.split():
                        written_Corectly += 1

            text1 = setning.split()
            text2 = setning1.split()
            text3 = setning2.split()
            text4 = setning3.split()

            if language == "english":
                try:
                    accuracy = (written_Corectly / len(text1)) * 100
                    accuracy1 += accuracy
                except:
                    accuracy1 += 0
            elif language == "norwegian":
                try:
                    accuracy = (written_Corectly / len(text2)) * 100
                    accuracy1 += accuracy
                except:
                    accuracy1 += 0
            elif language == "german":
                try:
                    accuracy = (written_Corectly / len(text3)) * 100
                    accuracy1 += accuracy
                except:
                    accuracy1 += 0
            elif language == "bosnian":
                try:
                    accuracy = (written_Corectly / len(text4)) * 100
                    accuracy1 += accuracy
                except:
                    accuracy1 += 0

            wordsPerMin = format((len(words) / (fullTime2 / 60)), ".2f")
            wpm += int(float(wordsPerMin))
            name1 = f"{name} - round {i}"
            self.statsAddPerRound(str(name1), str(setning), wpm)

        self.barPlot()
        percentage = format((accuracy1 / rounds), ".2f")
        wpm1 = format(wpm / rounds, ".2f")

        #print("Accuracy: " + str(accuracy1) + "\nPercentage: " + str(percentage) + "\nWritten correctly: " + str(written_Corectly))
        self.printOut(wpm1, percentage, str(fullTime1))
        self.stats_add(str(fullTime1), str(percentage), str(wpm1), str(name))



    def stats_add(self, time, accuracy, wpm, name):


        self.stats[name] = {
            'Time_used': time,
            'Accuracy': accuracy,
            'Words_per_minute': wpm
        }
        file_path = "stats.json"

        with open(file_path, 'w') as json_file:
            json.dump(self.stats, json_file)


    def statsAddPerRound(self, name, sentence, wpm):


        self.stats1[name] = {
            'sentence': sentence,
            'words_per_minute': wpm
        }

    def barPlot(self):

        fig, ax = plt.subplots()

        for round_name, stats in self.stats1.items():
            sent = stats['sentence']
            stat = stats['words_per_minute']
            ax.bar(round_name, stat, label=f"Result: {stat} wpm")
            print(f"{round_name}: "+sent)

        ax.set_xlabel('Round')
        ax.set_ylabel('Words per minute')
        ax.set_title('Words Per Minute Per Round')
        ax.legend()
        plt.show()



    def from_file(self):
        if os.path.exists("stats.json"):
            try:
                with open("stats.json", "rb") as f:
                    self.stats = json.load(f)
            except Exception as e:
                print(f"Error {e}")
        else:
            print("The file 'stats.json' does not exist")

    def printOut(self, wordsPerMin, accuracy, time):

        print(f"Average WPM: {wordsPerMin}")
        print(f"Accuracy: {accuracy}%")
        print(f"Total time: {time} seconds")

        #self.stats_add(time, accuracy, wordsPerMin)

    def scores_load(self, code):
        sort = sorted(self.stats.items(), key=lambda x: x[1]['Words_per_minute'], reverse=True)

        print(f"The best {code}:")
        for rank, (name, stats) in enumerate(sort[:int(code)], start=1):
            print(f"Rank: {rank} ",f"Name: {name} ",f"\nAccuraacy: {stats['Accuracy']}%",f"Word per min: {stats['Words_per_minute']}")
            print(" ")


exam = typeTest()
#Calls the method that opens the Json file and loads stats
exam.from_file()

while True:

    print("Choose between play, leader board or end")
    choiche = input(": ")

    if choiche == "play":
        if not bool(exam.stats1):
            #stats1 dictinary is empty
            exam.textChocie()
        else:
            #stats1 dictionary is not empty
            #use clear() to empty it
            exam.stats1.clear()
            exam.textChocie()

    elif choiche == "leader board":
        #Shows the top 10 based on wpm
        exam.scores_load(10)
        print(" ")
    elif choiche == "end":
        print("Thank you for playing")
        exit()
