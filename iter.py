class MyIter:
    def __init__(self) -> None:
        self.counter = 0
        self.list = [1, 2, 3, 4, 5]

    def __next__(self):
        try:
            result = self.list[self.counter]
        except IndexError:
            raise StopIteration

        self.counter += 1

        return result

    def __iter__(self):
        return self


class Test:
    def __init__(self) -> None:
        self.counter = 0
        self.list = [1, 2, 3, 4, 5]

    def __getitem__(self, index):
        print(index, "<---")
        return self.list[index]

    def __len__(self):
        return len(self.list)
