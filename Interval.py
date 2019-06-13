class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self): # __str__ for printing single object
        return '[' + str(self.start) + ', '+str(self.end) + ']'
    
    def __repr__(self): # __repr__ for printing this object in a iterable container
        return self.__str__()

# test code
if __name__ == "__main__":
    A = [(1, 2), (3, 4)]
    _list = []
    for a in A:
        _list.append(Interval(*a))
    
    print(_list)
    