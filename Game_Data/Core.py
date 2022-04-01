class Round():
    def __init__(self):
        self.state = 0
        return
    
    def start(self):
        self.state = 1
        return

    def isEnd(self):
        return (self.state==0)