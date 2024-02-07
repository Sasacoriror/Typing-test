import random

class norwegian:

    def __str__(self):

        # Templets that are pre written with placeholders
        text = [
            "når jeg spiller {aktivitet} vil jeg spille med {player} på {team}.",
            "{team} har det beste {aktivitet} laget i verden, men {team1} er bedre.",
            "Når {player} spillern {team} er de nesten uslåelige, med mindre de får {cause}."
        ]

        # Random text chosen
        randomText = random.choice(text)
        # Two sport activities
        opt_activity = ['football', 'basketball']

        # Random activity
        aktivitet = random.choice(opt_activity)

        # two different lists
        opt_team = []
        opt_player = []

        # Teams in that activity
        if aktivitet == "football":
            opt_team = ['manchester city', 'manchester united', 'liverpool', 'arsenal', 'etihad', 'emirates', 'anfield',
                        'old trafford']
        elif aktivitet == "basketball":
            opt_team = ['lakers', 'celtics', 'clippers', 'bulls']

        # Two teams chosen
        laget = random.choice(opt_team)
        laget1 = random.choice(opt_team)

        # Based on the laget, what player
        if laget == "manchester city" or laget == "etihad":
            opt_player = ['de bruyne', 'haaland', 'rodri', 'foden']
        elif laget == "manchester united" or laget == "old trafford":
            opt_player = ['fernandes', 'hoojlund', 'casemiro', 'maguire']
        elif laget == "liverpool" or laget == "anfield":
            opt_player = ['salah', 'van dijk', 'allison', 'trent']
        elif laget == "arsenal" or laget == "emirates":
            opt_player = ['oodegard', 'martinelli', 'saka', 'saliba']
        elif laget == "celtics":
            opt_player = ['tatum', 'the legend larry bird']
        elif laget == "bulls":
            opt_player = ['the goat jordan', 'the legend pippen']
        elif laget == "lakers":
            opt_player = ['lebron james', 'the great kareem']
        elif laget == "clippers":
            opt_player = ['the historic mcadoo', 'blake']

        # Test incase the list is empty
        if not opt_player:
            print("List is empty")
            return

        # Random player chosen from the player list
        player = random.choice(opt_player)

        # List of couses and ramdom choiche
        opt_cause = ['syk', 'skadet']
        cause = random.choice(opt_cause)

        # Dictionary for the place holders
        sentence = {
            'aktivitet': aktivitet,
            'team': laget,
            'team1': laget1,
            'player': player,
            'cause': cause
        }

        # Completing the text
        set1 = randomText.format(**sentence)

        #print("Norwegian class: ", set1)
        return set1
#for i in range(0, 10):
    #norwegian1 = norwegian()
    #norwegian1.__str__()
