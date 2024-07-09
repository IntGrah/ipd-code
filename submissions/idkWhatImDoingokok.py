class Strategy:
  def __init__(self):
    self.prev = []
    self.soFar = 0
    self.goods1SoFar = 0
    self.bad1SoFar = 0
    self.goods2SoFar = 0
    self.bad2SoFar = 0
    self.res = True

  def action(self, prev_action: bool | None) -> bool:
    if len(self.prev) < 5:
      return True
    if prev_action == True:
        self.goods1SoFar += 1
    else:
        self.bad1SoFar += 1

    if len(self.prev) < 10:
        return False
    else:
        return True


# acc at the start ud prolly wanna test the waters a bit, be good for 5, be bad for 5. If they
# are good for ur good and bad for ur bad then be good. if they are good for ur good and good for ur bad then be bad
# if they are bad for ur good then just be bad the entire way
# if they are 


"""
Good
Bad
Good
Good
Good
Good


but wait!
it is more advantageous to be good, then see if the opps are being bad, then switch to bad if they are 
manipulating us
this way if they are good ppl, then we are also good ppl. also it 


"""