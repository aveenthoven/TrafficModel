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