#Python Iterator
class Iterator:

    def __init__(self,start,end):
        self.value=start
        self.end=end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value <= self.end:
            current = self.value
            self.value += 1
            return current
        else:
            raise StopIteration

# Generators  are also Iterators ,
# only they automatically create and initialize
# __next__() and __iter__() methods

# Python Generator
def generator(start,end):
    current=start
    while current <= end:
        yield current
        current += 1

no=generator(10,20)
for i in no:
    print(i,end=",")

nums=Iterator(21,31)

print(next(nums))
print(next(nums))
print(next(nums))

for num in nums:
    print(i,end=" ")


