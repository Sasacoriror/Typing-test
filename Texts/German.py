import random

class german:

    def __str__(self):

        text = [
            "Wenn ich {activity} spiele, mochte ich mit {player} bei {team} spielen.",
            "{team} ist das beste {activity} team der Welt, aber {team1} sind besser.",
            "Wenn {player} fur {team} spielt, sind sie fast unschlagbar, es sei denn, sie bekommen {cause}."
        ]

        randomText = random.choice(text)
        opt_activity = ['fusball', 'basketball']

        activity = random.choice(opt_activity)


        opt_team = []
        opt_player = []

        if activity == "fusball":
            opt_team = ['manchester city', 'manchester united', 'liverpool', 'arsenal', 'die etihad', 'old trafford', 'anfield', 'die emirates']
        elif activity == "basketball":
            opt_team = ['die lakers', 'die celtics', 'die clippers', 'die bulls']

        team = random.choice(opt_team)
        team1 = random.choice(opt_team)

        if team == "manchester city" or team == "die etihad":
            opt_player = ['de bruyne', 'haaland', 'rodri', 'foden']
        elif team == "manchester united" or team == "old trafford":
            opt_player = ['fernandes', 'hoojlund', 'casemiro', 'maguire']
        elif team == "liverpool" or team == "anfield":
            opt_player = ['salah', 'van dijk', 'allison', 'trent']
        elif team == "arsenal" or team == "die emirates":
            opt_player = ['oodegard', 'martinelli', 'saka', 'saliba']
        elif team == "die celtics":
            opt_player = ['tatum', 'the legend larry bird']
        elif team == "die bulls":
            opt_player = ['the goat jordan', 'the legend pippen']
        elif team == "die lakers":
            opt_player = ['lebron james', 'the great kareem']
        elif team == "die clippers":
            opt_player = ['the historic mcadoo', 'blake']

        if not opt_player:
            print("List is empty")
            return

        player = random.choice(opt_player)


        opt_cause = ['sick', 'injured']
        cause = random.choice(opt_cause)

        sentence = {
            'activity': activity,
            'team': team,
            'team1': team1,
            'player': player,
            'cause': cause
        }

        set1 = randomText.format(**sentence)


        #print("German class: ",set1)
        return set1
#for i in range(0, 10):
    #german1 = german()
    #german1.__str__()