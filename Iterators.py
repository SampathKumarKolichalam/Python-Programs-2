#Method:-1
nums=[6,9,3,1]
itr=iter(nums)
print(itr.__next__())
     #OR
print(next(itr))
#Method:-2
class show:
    def __init__(self) -> None:
     self.num=1
    def __iter__(self)-> None:
     return self
    def __next__(self)-> None:
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
values=show()
#print(next(values))
for i in values:
    print(i)