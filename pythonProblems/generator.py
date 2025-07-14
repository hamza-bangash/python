class evenSquare():
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start>self.end:
            raise StopIteration
        if self.start % 2 == 0:
            result = self.start ** 2
            self.start += 1
            return result
        
def oddSquare(start,end):
    while start>end:
        if start % 2 !=0:
            result = start**2
            start += 1
            yield result


check = evenSquare(1,10)
print(next(check))
print(next(check))

temp = oddSquare(1,10)
print(next(temp))
print(next(temp))