"""
Create a soccer world cup.
Author: Rafeh Qazi
"""
import random
import itertools
import csv
from collections import defaultdict

# PICK YOUR TEAMS HERE!
# ************************************************************
TEAMS = ['london fc', 'bayern munchen', 'psg']
PICKED = ['barcelona', 'man blue', 'real madrid']
HEADER = ["Group", "Matches", "Win", "Draw", "Loss", "GA", "GF", "Points", "MOTM", "Rafeh", "Waqas", "Saqib"]
OUTPUT_FILE = "soccer/cup.csv"
# ************************************************************

# Title case team names
ALL_TEAMS = []
for team in TEAMS:
    ALL_TEAMS.append(team.title())


# Title case team names
PICKED_TEAMS = []
for team in PICKED:
    PICKED_TEAMS.append(team.title())


def make_2_random_groups(all_teams):
    """
    Take a list of teams and randomly puts them into two groups.
    :param all_teams: list
    :return: tuple containing two lists.
    """
    all_teams = all_teams.copy()
    group1, group2 = [], []
    num1, num2 = 0, 1
    for i in range(len(all_teams)):
        num1, num2 = num2, num1  # switching/alternating technique.
        if num1 == 0:
            group1.append(all_teams.pop(all_teams.index(random.choice(all_teams))))
        else:
            group2.append(all_teams.pop(all_teams.index(random.choice(all_teams))))
    return group1, group2


def pick_random_teams(all_teams, person1, person2, person3):
    """
    Take a list of teams as input and returns them randomly for 2 people.
    :param all_teams: list
    :param person1: str
    :param person2: str
    :param person3: str
    :return: tuple of lists.
    """
    all_teams = list(set(all_teams.copy()))
    first_guy = defaultdict(list)
    second_guy = defaultdict(list)
    third_guy = defaultdict(list)
    next_turn = ('0 1 2 ' * int(len(all_teams) / 3)).split()
    for i in range(len(all_teams)):
        team_ = all_teams.pop(all_teams.index(random.choice(all_teams)))  # randomly popoff from list.
        turn = next_turn.pop()
        if turn == '0':
            first_guy[person1].append(team_)
        elif turn == '1':
            second_guy[person2].append(team_)
        elif turn == '2':
            third_guy[person3].append(team_)

    return first_guy, second_guy, third_guy


def possible_combination_of_games(all_teams, picked_teams):
    """
    print_qualifier_games() function is dependent on this function.
    :param all_teams: list
    :param picked_teams: list
    :return: list
    """
    return list(itertools.combinations(all_teams + picked_teams, 2))


def next_qualifier_game(all_teams, picked_teams):
    """
    takes in as input all possible game combinations
    and yields the next game.
    :yield: tuple
    """
    matches = possible_combination_of_games(all_teams, picked_teams)
    total_games = len(possible_combination_of_games(all_teams, picked_teams))
    all_matches = []
    print("------------------ALL POSSIBLE GAMES ({0})-----------------------".format(total_games))
    for _ in possible_combination_of_games(all_teams, picked_teams):
        # yield ' VS. '.join(matches.pop(matches.index(random.choice(matches))))
        all_matches.append([' VS. '.join(matches.pop(matches.index(random.choice(matches))))])
    return all_matches


def csv_writer(file_object):
    """
    takes in a file path as input and writes to it.
    :param file_object: string
    """
    with open(file_object, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, dialect='excel')
        header = spamwriter.writerow(HEADER)
        data = next_qualifier_game(ALL_TEAMS, PICKED_TEAMS)
        print(data)
        spamwriter.writerows(data)


def run_all():
    """
    run all functions here.
    """
    print(*make_2_random_groups(ALL_TEAMS))
    # print(*pick_random_teams(ALL_TEAMS, 'rafeh', 'saqib', 'waqas'))
    csv_writer(OUTPUT_FILE)


run_all()
