from flask import Flask
from flask import render_template
app = Flask(__name__)
TEAM1 = 0
TEAM2 = 1

class Team:
    def __init__(self, team_name):
        self.name = team_name

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
    def __init__(self, team1, team2, score=Score(0,0))
        """ init a series with team1 as the home-advantage team and team2 as the second team. """
        self.team1 = team1
        self.team2 = team2
        self.score = score


class Round:
    def __init__(self, number, series):
        self.number = number
        self.series = series

class Bracket:
    def __init__(self, east_rounds, west_rounds, final):
        self.east_rounds = east_rounds
        self.west_rounds = west_rounds
        self.final = final

@app.route('/<name>')
def display_bracket():
    return render_template('user_bracket.html', name=name)
