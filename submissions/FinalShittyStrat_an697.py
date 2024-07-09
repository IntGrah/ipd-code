import random
class Strategy:
    def __init__(self):
        self.coops = 0
        self.defects = 0
        self.prev_play = []

    def action(self, prev_action: bool | None) -> bool:
        if(prev_action is None):
            return True
        
        if(prev_action):
            self.coops += 1
        else:
            self.defects += 1
        self.prev_play.append(prev_action)
        #Now decide
        #If there are a large number of defects I am better of just spamming defects
        #How to decide the threshold?
        #The threshold is I guess the point where if the guy follows the same distr, I am better of in defect
        #defect than cooperating(even if the person changes his strategy)
        #Note we may want to give the person some time

        #Assume an expected decline to defect all of x(ie if i defect, the person(on average)
        #,changes to defect all with probability x(note that x should be a function of p))
        

        #I can assume a 'cooperating' player has a higher chance of defection.
        #So I guess x is a decreasing function of p. For now(as this is naive implementation), we can do
        #quadrating decrease from (0, 0.5) to (1, 0) tangent to the x axis(idk it just looks nice)
        p = self.coops/(self.coops + self.defects)   #Naive probability of cooperating
        x = (p - 1) * (p - 1) / 2     #Probability(or expected decline) that my defecting will make them defectors
        defect_threshold = 1 / 3      #This is the value where I am better off just defecting(as 3p <= 1)
        if(len(self.prev_play) >= 5):    #Arbritrary(I dont want to start the spam very soon)
            if((1 - x) * p <= defect_threshold):#So basically defect defect is better than cooperating(new p will be
                                      #(1 - x)p
                return False
        
        #defect with a probability of 0.12
        if(random.random() < 0.15):
            return False

        #Another strategy would probably be to probably defect if the last k are defects
        k = 3#A random value that seems good
        if(len(self.prev_play) >= k):
            defect_status = False
            for i in range(len(self.prev_play) - 3, len(self.prev_play)):
                defect_status = defect_status or self.prev_play[i]
            return defect_status
        
        return True#cooperate