"""
A program to simulate racquetball
Author: Rafeh Qazi
Date: 11/21/2015
"""
import random


# Racquetball Game Rules:
# 1. First move is called the Serve.
# 2. Alternating turns with legal moves is called a Rally.
# 3. Rally ends when one player fails to hit a legal shot.
# 4. Player who misses the shot is the loser of the rally.
# 5. If server loses the point, serve switches.
# 6. If server wins the point, a point is awarded.
# 7. Players can only score during their own service.
# 8. First player to reach 15 points first wins the game.

# The program will judge the players' skill based on their probability,
# If they have 0.6 score, that means they should win 60% of the games.

def racquetball():
    """
    Given two players' probabilities for winning, it prints out their simulated result after N games.
    :param player_a: float between 0 and 1
    :param player_b: float between 0 and 1
    """
    player_a = int(float(input('Enter the probability that PLAYER A wins the serve: ')) * 10)
    player_b = int(float(input('Enter the probability that PLAYER B wins the serve: ')) * 10)
    sim_n_games = int(input('How many games would you like to simulate: '))
    # I create lists containining 1's and 0's. I then use it to simulate weighted probability.
    player_a_probability = [1 for _ in range(player_a)] + [0 for _ in range(10 - player_a)]
    player_b_probability = [1 for _ in range(player_b)] + [0 for _ in range(10 - player_b)]
    score_a = 0
    score_b = 0
    for i in range(sim_n_games):
        if random.choice(player_a_probability) > random.choice(player_b_probability):
            score_a += 1
        elif random.choice(player_a_probability) < random.choice(player_b_probability):
            score_b += 1
        else:
            # If they are both equal, select one of them randomly to be the winner.
            if random.randint(0, 1) == 0:
                score_a += 1
            else:
                score_b += 1
    print('Games Simulated: {0}'.format(sim_n_games))
    print('Wins for A: {0} ({1}%)'.format(score_a, (round((score_a / sim_n_games) * 100, 2))))
    print('Wins for B: {0} ({1}%)'.format(score_b, (round((score_b / sim_n_games) * 100, 2))))

racquetball()
