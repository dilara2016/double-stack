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


class threestacks:
    def __init__(self,n):
        self.size = n
        self.ar = [None] * n
        self.top1 = -1
        self.top2 = n
        self.mid = n // 2
        self.top3 = self.mid -1

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
    
    def push3(self,x):
        if self.top3 +1 < self.top2:
            self.top3 += 1
            self.ar[self.top3] =x
        else:
            print("stack 3 overflow")

    
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

    def pop3(self):
        if self.top3 >= self.mid:
            x = self.ar[self.top3]
            self.top3 -= 1
            return x
        else:
            print("stack 3 overflow")
ts3 = threestacks(10)  
ts = twostacks(5)     


ts.push1(5)
ts.push2(10)
ts.push2(16)
ts.push1(13)
ts.push2(6)
print("Popped element from stack1: " + str(ts.pop1()))
ts.push2(12)
print("Popped element from stack2: " + str(ts.pop2()))

ts3.push1(11)
ts3.push2(99)
ts3.push3(55)
ts3.push3(66)
print("Popped element from stack3: " + str(ts3.pop3()))
