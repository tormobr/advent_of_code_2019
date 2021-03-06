import time
from collections import defaultdict, deque
from intcoder import Intcoder

class Network:

    def __init__(self, data, n):
        self.n = n
        self.data = data
        self.inputs = [deque([i]) for i in range(self.n)]
        self.NAT = (0,0)
        self.SEEN = []

    def part1(self):
        C = []
        for i in range(self.n):
            C.append(Intcoder(self.data.copy(), i))

        idle = 0
        while True:
            for i,c in enumerate(C):
                a = c.eval(self.get_input)
                x = c.eval(self.get_input)
                y = c.eval(self.get_input)
                print(a, x, y)
                if a == None:
                    continue
                idle = 0

                if a == 255:
                    self.NAT = (x, y)
                    continue
                elif a not in range(50):
                    time.sleep(.4)
                    continue
                self.inputs[a].append(x)
                self.inputs[a].append(y)
            if idle > 2:
                self.inputs[0].append(self.NAT[0])
                self.inputs[0].append(self.NAT[1])
                if len(self.SEEN) > 0 and self.NAT[1] == self.SEEN[-1]:
                    print(f"result: {self.NAT[1]}")
                    time.sleep(10)
                self.SEEN.append(self.NAT[1])
            idle += 1
    def get_input(self, i):
        if len(self.inputs[i]) == 0:
            #print(f"input for {i} = -1")
            return -1
        #print(f"input for{i} = {self.inputs[i][0]}" )
        return self.inputs[i].popleft()

if __name__ == "__main__":
    data = {i: int(x) for (i,x) in enumerate(open("input.txt", "r").read().split(","))}
    N = Network(data, 50) 
    N.part1()






