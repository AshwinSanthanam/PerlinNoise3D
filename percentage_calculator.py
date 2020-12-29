class PercentageCalculator:
    def __init__(self, total):
        self.__total = total
        self.__count = 0

    @property
    def percentage(self):
        return self.__count / self.__total

    def add_count(self, count):
        if self.__count + count > self.__total:
            raise ValueError("supplied count exceeds the total")
        else:
            self.__count += count
        return self.__count == self.__total
