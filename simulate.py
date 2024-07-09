from random import random

T = 5 # Temptation to defect
R = 3 # Reward for mutual cooperation
P = 1 # Punishment for mutual defection
S = 0 # Sucker's payoff

def simulate(p1_strategy, p2_strategy, r, p = 0.05):
    p1_score = 0
    p2_score = 0
    
    p1_prev = None
    p2_prev = None

    for _ in range(r):
        p1_action = bool(p1_strategy.action(p2_prev))
        p2_action = bool(p2_strategy.action(p1_prev))
        
        p1_prev = not p1_action if random() < p else p1_action
        p2_prev = not p2_action if random() < p else p2_action

        if p1_action and p2_action:       # mutual cooperation
            p1_score += R
            p2_score += R
        elif p1_action and not p2_action: # p2 defects
            p1_score += S
            p2_score += T
        elif not p1_action and p2_action: # p1 defects
            p1_score += T
            p2_score += S
        else:                             # mutual defection
            p1_score += P
            p2_score += P

    return p1_score, p2_score
