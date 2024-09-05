class edge(object):
    def __init__(self,input,output,length,lanes):
        self.input = input
        self.output = output
        self.length = length
        self.lanes = lanes          
    def C(self):
        return int(self.lanes*self.length/(4.5+55))
class node(object):
    def __init__(self,input,output):
        self.input = input
        self.output = output
class car(object):
    def __init__(self,location,time):
        self.location = location
        self.time = time
    def timepass(self):
        self.time+=1
    def begintravel():
        tt = (z['a'][1][0]*0.6)*(1+alpha*(N/C)**beta)
        self.remainingtime=5
