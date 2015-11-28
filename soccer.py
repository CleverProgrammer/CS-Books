"""
Create a soccer world cup.
Author: Rafeh Qazi
"""
import random
from collections import defaultdict


ALL_TEAMS = ['pakistan', 'athletico madrid', 'london fc', 'man blue',
                  'bayern', 'psg', 'spain', 'germany', 'argentina',
                  'barcelona', 'real madrid', 'my club', 'barcelona']


def make_2_random_groups(all_teams):
    """
    Take a list of teams and randomly put them into two groups.
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

print(*make_2_random_groups(ALL_TEAMS))


def pick_random_teams(all_teams, person1, person2, person3):
    """
    Take a list of teams as input and return them randomly for 3 people.
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
    print(next_turn)
    for i in range(len(all_teams)):
        team = all_teams.pop(all_teams.index(random.choice(all_teams)))  # randomly popoff from list.
        turn = next_turn.pop()
        if turn == '0':
            first_guy[person1].append(team)
        elif turn == '1':
            second_guy[person2].append(team)
        else:
            third_guy[person3].append(team)
    return first_guy, second_guy, third_guy

print(*pick_random_teams(ALL_TEAMS, 'waqas', 'saqib', 'rafeh'))
