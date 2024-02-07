import random

class bosnian:

    def __str__(self):

        text = [
            "kada igram {aktivnost} zelim igrati sa {igrac} u {team}.",
            "{team} je najbolji {aktivnost} tim na svijetu, ali {team1} su bolji.",
            "Kada {igrac} igra za {team} oni su gotovo nepobjedivi, osim ako ne bode {nesto}."
        ]

        randomText = random.choice(text)
        opt_activity = ['football', 'kosarka']

        activity = random.choice(opt_activity)


        opt_team = []
        opt_player = []

        if activity == "football":
            opt_team = ['manchester city', 'manchester united', 'liverpool', 'arsenal', 'na etihad', 'na old trafford', 'na anfield', 'na emirates']
        elif activity == "kosarka":
            opt_team = ['na lakers', 'na celtics', 'na clippers', 'na bulls']

        team = random.choice(opt_team)
        team1 = random.choice(opt_team)

        if team == "manchester city" or team == "na etihad":
            opt_player = ['de bruyne', 'haaland', 'rodri', 'foden']
        elif team == "manchester united" or team == "na old trafford":
            opt_player = ['fernandes', 'hoojlund', 'casemiro', 'maguire']
        elif team == "liverpool" or team == "na anfield":
            opt_player = ['salah', 'van dijk', 'allison', 'trent']
        elif team == "arsenal" or team == "na emirates":
            opt_player = ['oodegard', 'martinelli', 'saka', 'saliba']
        elif team == "na celtics":
            opt_player = ['tatum', 'the legend larry bird']
        elif team == "na bulls":
            opt_player = ['the goat jordan', 'the legend pippen']
        elif team == "na lakers":
            opt_player = ['lebron james', 'the great kareem']
        elif team == "na clippers":
            opt_player = ['the historic mcadoo', 'blake']

        if not opt_player:
            print("List is empty")
            return

        player = random.choice(opt_player)


        opt_cause = ['bolestan', 'povredjo']
        cause = random.choice(opt_cause)

        sentence = {
            'aktivnost': activity,
            'team': team,
            'team1': team1,
            'igrac': player,
            'nesto': cause
        }

        set1 = randomText.format(**sentence)


        #print("Bosnian class: ",set1)
        return set1
#for i in range(0, 10):
    #bosnian1 = bosnian()
    #bosnian1.__str__()