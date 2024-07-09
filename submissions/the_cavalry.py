import random
from typing import Optional


class Strategy:
    """
    This strategy aims to be collaborative with a hint of cheek.
    In order to prevent the beginning of any tit-for-tat battles caused by false information given in the game,
    this strategy will only retaliate after it has been attacked twice in a row, or if the opposition is defecting a large amount.
    Beyond that, 5% of the time this strategy will defect, hoping the opponent sees this as just noise and continues to collaborate.
    """

    def __init__(self):
        self.opponent_cooperations = 0
        self.opponent_defects = 0
        self.opponent_action_two_rounds_ago: Optional[bool] = None

    def action(self, prev_action: Optional[bool]) -> bool:
        # By default co-operate, and only defect if the cases below trigger.
        my_action = True

        if prev_action is None:
            my_action = False  # Start with a defect to try and win a point.
        elif prev_action is False:
            self.opponent_defects += 1
            if self.opponent_action_two_rounds_ago is False:
                my_action = False  # Opponent has defected twice in a row, time to hit them back.
        else:
            self.opponent_cooperations += 1

        if (
            2 * self.opponent_defects > self.opponent_cooperations
            and self.opponent_cooperations + self.opponent_defects > 10
        ):
            my_action = False  # The opponent is defecting an awful lot, time to try and get one back.

        if random.random() < 0.05:
            my_action = False  # A cheeky defect to try and win one up.

        self.opponent_action_two_rounds_ago = prev_action
        return my_action
