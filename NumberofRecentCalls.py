
class RecentCounter:
    def __init__(self):
        self.q = []
    
    def ping(self, t: int):

        self.q.append(t)

        while self.q[0] < t - 3000:
            self.q.pop(0)
        
        return len(self.q)
        
rc = RecentCounter()

inputs = ["RecentCounter","ping","ping","ping","ping"]
inputs = [[],[642],[1849],[4921],[5936]]

for x in inputs:
    for y in x:
        print(y, rc.ping(y))