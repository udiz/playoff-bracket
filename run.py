from flask import Flask
from flask import render_template
app = Flask(__name__)
TEAM1 = 0
TEAM2 = 1

@app.template_global(name='zip')
def _zip(*args, **kwargs): #to not overwrite builtin zip in globals
        return __builtins__.zip(*args, **kwargs)

class Team:
    def __init__(self, team_name):
        self.name = team_name

    def __str__(self):
        return self.name

class Score:
    def __init__(self, team1_wins=0, team2_wins=0):
        self.team1_wins = team1_wins
        self.team2_wins = team2_wins
        self.winner = None
        if team1_wins >= 4:
            self.winner = TEAM1
        elif team2_wins >= 4:
            self.winner = TEAM2
 
    def team_won(winning_team):
        if winning_team == TEAM1:
            self.team1_wins += 1
        elif winning_team == TEAM2:
            self.team2_wins += 1
        self.check_winner()

class Series:
    def __init__(self, team1, team2, score=Score(0,0)):
        """ init a series with team1 as the home-advantage team and team2 as the second team. """
        self.team1 = team1
        self.team2 = team2
        self.score = score

    def is_correct(self, series_actual):
        return self.score.team1_wins == series_actual.score.team1_wins and self.score.team2_wins == series_actual.score.team2_wins

    def is_team1_wins_correct(self,series_actual):
        return self.score.team1_wins == series_actual.score.team1_wins

    def is_team2_wins_correct(self, series_actual):
        return self.score.team2_wins == series_actual.score.team2_wins

class Round:
    def __init__(self, number, series):
        self.number = number
        self.series = series

class Bracket:
    def __init__(self, east_rounds, west_rounds, final):
        self.east_rounds = east_rounds
        self.west_rounds = west_rounds
        self.east_rounds.reverse()
        self.final = final
        self.rounds = west_rounds + [final] + east_rounds

@app.route('/')
def display_bracket():
    return render_template('user_bracket.html', name="udi", bracket=bracket, bracket_actual=bracket_actual)


team1 = Team('Warriors')
team2 = Team('Spurs')
serie = Series(team1, team2, Score(4,3))
round1 = Round(1, [serie]*4)
round2 = Round(2, [serie]*2)
round3 = Round(3, [serie])
conf = [round1, round2, round3]
final = Round(4, [serie])
bracket = Bracket(conf, list(conf), final)

serie2 = Series(Team('Rockets'), team2, Score(3,4))
r1 = Round(1, [serie2]*4)
r2 = Round(2, [serie2]*2)
r3 = Round(3, [serie2])
cc = [r1, r2, r3]
ff = Round(4, [serie2])
bracket_actual = Bracket(cc, list(cc), ff)

if __name__ == '__main__':
   app.run(debug=True)
