class My_sentence:
    def __init__(self,statement):
        self.statement=statement
        self.index=0
        self.words=self.statement.split(" ")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.words):
            raise StopIteration
        index=self.index
        self.index += 1
        return self.words[index]


sentence=My_sentence("Effects of Coronavirus, maintain social distancing")
print(next(sentence))
print(next(sentence))
print(next(sentence))
print(next(sentence))
print(next(sentence))
print(next(sentence))