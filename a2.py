class twostacks:
    def __init__(self,n):
        self.size = n
        self.ar = [None] * n
        self.top1 = -1
        self.top2 = self.size

    def push1(self,x):
        if self.top1  < self.top2 -1:
            self.top1 = self.top1 + 1
            self.ar[self.top1] = x
        
        else:
            print("stack overflow")

    def push2(self,x):
        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 -1
            self.ar[self.top2] = x

        else:
            print("stack overflow")
            exit(1)

    
    def pop1(self):
        if self.top1 >= 0:
            x = self.ar[self.top1]
            self.top1 = self.top1 - 1
            return x
        else:
            print("stack underflow")
            exit(1)

    def pop2(self):
        if self.top2 < self.size:
            x = self.ar[self.top2]
            self.top2 = self.top2 + 1
            return x
        else:
            print("stack underflow")
            exit(1)

ts = twostacks(5)
ts.push1(5)
ts.push2(10)
ts.push2(16)
ts.push1(13)
ts.push2(6)

print("Popped element from stack1: "+str(ts.pop1()))
ts.push2(12)
print("Popped element from stack2: "+str(ts.pop2()))