'''
Exercise 4: Design a class SeriesCalculator that calculates the sum of an arithmetic series.
'''

class SeriesCalculator:
    def calculator(self, x, y):
        sum = 0
        for i in range(x, y+1):
            sum = sum + i
        return sum


s = SeriesCalculator()
print(s.calculator(2,10))
