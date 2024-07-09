import random
class Strategy:
  def action(self, prev_action: bool | None) -> bool:
    return random.choice((True,False))
