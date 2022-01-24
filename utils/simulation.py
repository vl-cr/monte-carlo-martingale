import numpy as np
from typing import Tuple

def simulate(simulations: int = 10, bet: float = 0.01,
             bank: int = 100, goal: int = 1000) -> Tuple[list, list, list, list, list, int]:
    """
    Runs a Monte Carlo simulation of the Martingale Strategy. Very slow because it's not optimized by Numba.
    Please note that the code in this function is very simple. This is intentional.
    The reason for that is the fact that it was written with the limitations of Numba in mind.

    Martingale Strategy won't be explained here. Instead, the simulation process will be described.
    Here are the rules for any given simulation:
        - Player starts with an initial bank (e.g. 1000).
        - Player chooses the initial bet (e.g. 0.01) and always goes back to it after a win.
        - Player doubles the previous bet after each loss.
        - Player always chooses red (in fact, the choice doesn't matter: probability of both red and black is 48.7%).
        - If player has to bet more than what they have in the bank, then they go back to the initial bet.
        - Player bets until they reach their goal or lose all their bank.

    Args:
        simulations: (int) number of simulations to be executed (1 simulation = 1 gambler trying out the strategy).
        bet: (float) the initial bet amount in any sequence of bets.
        bank: (int) gambler's initial bank that will start growing or shrinking as the game goes by.
        goal: (int) gambler's target bank, the game will stop if gambler achieves this bank or loses all money.

    Returns:
        Tuple with data related to the completed simulations:
            - steps: a list that contains the number of steps required to complete each individual simulation.
            - max_banks: a list that contains the max bank achieved (in each simulation).
            - max_bets: a list that contains the highest bet amount that the player had to place (in each simulation).
            - wbanks: a list that stores the bank progression of up to 4 winners (used for plots).
            - lbanks: a list that stores the bank progression of up to 4 losers (used for plots).
            - winners: (int) the number of simulations that resulted in the player achieving the goal.
    """
    steps = []
    max_banks = []
    max_bets = []
    wbanks = []
    lbanks = []
    winners = 0

    # 37 possible outcomes in a European roulette. Here 1=red, 2=black, 0=zero.
    outcomes = np.array([1]*18 + [2]*18 + [0])
    choice = 1  # Red is represented as 1

    for i in range(simulations):
        # Reinitialize the variables for each new simulation
        current_bank = bank
        current_bet = bet
        banks = []  # For bank history
        max_bank = 0
        max_bet = 0
        step = 0

        while current_bank > 0 and current_bank < goal:
            if current_bank > max_bank:
                max_bank = current_bank
            if current_bet > current_bank:
                current_bet = bet
            if current_bet > max_bet:
                max_bet = current_bet

            current_bank -= current_bet  # Bet placed
            # Spin the wheel, the outcome will be one of the following: [0, 1, 2]
            outcome = outcomes[np.random.choice(outcomes.shape[0], 1)[0]]

            if choice == outcome:
                current_bank += current_bet * 2
                current_bet = bet  # In Martingale Strategy, player goes back to initial bet after a win

                if current_bank >= goal:
                    winners += 1
                    max_bank = goal
            else:
                current_bet *= 2  # Double the bet in case of a loss

            step += 1
            banks.append(current_bank)

        steps.append(step)
        max_bets.append(max_bet)
        max_banks.append(max_bank)

        # For plots (we only want to plot up to 4 examples of winners and losers)
        if len(wbanks) < 4:
            if int(current_bank) >= goal:
                wbanks.append(banks)
        if len(lbanks) < 4:
            if int(current_bank) == 0:
                lbanks.append(banks)

    return steps, max_banks, max_bets, wbanks, lbanks, winners


def check_random_outcomes(outcomes: np.ndarray, nb: int = 100) -> Tuple[int, int, int]:
    """
    Selects a random outcome out of a numpy array a number of times.
    The numpy array contains string representations of all possible outcomes of a roulette wheel.
    Counts how many times red, black and zero were chosen with np.random.choice.
    Outcomes array will contain the following integers: 1 (red), 2 (black), 0 (zero).
    
    Args:
        outcomes: numpy array that contains all outcomes. For European roulette: 18 red, 18 black, 1 zero.
        nb: (int) number of times a random choice will be made from "outcomes" array.
    
    Returns:
        A tuple with 3 ints: counts of red, black and zero outcomes.
    """
    assert list(np.sort(np.unique(outcomes))) == [0, 1, 2], \
        "Incorrect outcomes array, it should only contain the following outcomes: [0, 1, 2]"

    # Initialize the counts
    red_count = 0
    black_count = 0
    zero_count = 0

    for i in range(nb):
        # Spin the wheel, the outcome will be one of the following: [0, 1, 2]
        outcome = outcomes[np.random.choice(outcomes.shape[0], 1)[0]]

        # Update the count that corresponds to the observed outcome
        if outcome == 1:
            red_count += 1
        elif outcome == 2:
            black_count += 1
        else:
            zero_count += 1  # Guaranteed to be 0 because of assert above

    return red_count, black_count, zero_count
