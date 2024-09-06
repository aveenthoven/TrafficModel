class edge(object):
    def __init__(self,input,output,length,lanes):
        self.input = input
        self.output = output
        self.length = length
        self.lanes = lanes          
    def C(self):
        return int(self.lanes*self.length/(4.5+55))
    def clear(self):
        filter=np.nonzero(np.logical_and(self.cars[:,2]==0,self.cars[:,0]==1))
        self.cars[filter,0]=0 #only have to change occupied to false, age can stay, since it will be changed if a new car comes in anyways
        self.output.cars.append(self.cars[filter,1])
    def avgtraveltime():
        if len(np.nonzero(self.cars[:,0]==1)): #==1 is faster than just using the regular array
            return tt0 #misschien heette de variabele anders
        else:
            return np.mean(self.cars[np.nonzero(self.cars[:,0]),2])
        

class node(object):
    def __init__(self,input,output):
        self.input = input
        self.output = output
        self.cars=np.array([])
    def chose():
        output=[i for i in output if np.sum(i.cars[:,0])<C(i)]
        if len(output):
            return np.random.choice(output,[1/avgtraveltime(i) for i in output]) #works if output is list of the edges coming out of the node
        else: return None #none seems appropriate, probably will let loop break on none
class car(object):
    def __init__(self,location,time):
        self.location = location
        self.time = time
    def timepass(self):
        self.time+=1
    def begintravel():
        tt = (z['a'][1][0]*0.6)*(1+alpha*(N/C)**beta)
        self.remainingtime=5
