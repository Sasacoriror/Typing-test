import random

class english:

    def __str__(self):

        #Templets that are pre written with placeholders
        text = [
            "when i play {activity} i want to play with {player} at {team}.",
            "{team} is the best {activity} team in the world, but {team1} are better.",
            "When {player} is playing for {team} they are almost unbeatable, unless they get {cause}."
        ]

        #Random text chosen
        randomText = random.choice(text)
        #Two sport activities
        opt_activity = ['football', 'basketball']

        #Random activity
        activity = random.choice(opt_activity)


        #two different lists
        opt_team = []
        opt_player = []

        #Teams in that activity
        if activity == "football":
            opt_team = ['manchester city', 'manchester united', 'liverpool', 'arsenal', 'the etihad', 'the emirates', 'anfield', 'old trafford']
        elif activity == "basketball":
            opt_team = ['the lakers', 'the celtics', 'the clippers', 'the bulls']

        #Two teams chosen
        team = random.choice(opt_team)
        team1 = random.choice(opt_team)

        #Based on the team, what player
        if team == "manchester city" or team == "the etihad":
            opt_player = ['de bruyne', 'haaland', 'rodri', 'foden']
        elif team == "manchester united" or team == "old trafford":
            opt_player = ['fernandes', 'hoojlund', 'casemiro', 'maguire']
        elif team == "liverpool" or team == "anfield":
            opt_player = ['salah', 'van dijk', 'allison', 'trent']
        elif team == "arsenal" or team == "the emirates":
            opt_player = ['oodegard', 'martinelli', 'saka', 'saliba']
        elif team == "the celtics":
            opt_player = ['tatum', 'the legend larry bird']
        elif team == "the bulls":
            opt_player = ['the goat jordan', 'the legend pippen']
        elif team == "the lakers":
            opt_player = ['lebron james', 'the great kareem']
        elif team == "the clippers":
            opt_player = ['the historic mcadoo', 'blake']

        #Test incase the list is empty
        if not opt_player:
            print("List is empty")
            return

        #Random player chosen from the player list
        player = random.choice(opt_player)


        #List of couses and ramdom choiche
        opt_cause = ['sick', 'injured']
        cause = random.choice(opt_cause)

        #Dictionary for the place holders
        sentence = {
            'activity': activity,
            'team': team,
            'team1': team1,
            'player': player,
            'cause': cause
        }

        #Completing the text
        set1 = randomText.format(**sentence)


        #print("English class: ",set1)
        return set1
#for i in range(0, 10):
    #english1 = english()
    #english1.__str__()