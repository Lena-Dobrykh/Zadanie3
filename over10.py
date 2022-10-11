class MyList(list):
    def __init__(self, x):
        if len(x) > 10:
            raise ValueError('>10')
        else:
            super().__init__(x)
            
    def append(self, x):
        if len(self) == 10:
            raise ValueError('>10')
        else:
            super().append(x)

y=MyList([1,2,3,4,5,6,7,8,9,10])

print(len(y))
