class Fraction:

    #this is the constructor
    # notice I didn't declare instance variables
    # there is only a single constructor
    # the first parameter is always the implicit parameter -
    # object that called this
    def __init__(self , n , d ):
        self.num = n
        self.den = d

    def getNumerator(self):
        return self.num

    def getDenominator(self):
        return self.den

    def asDecimal(self):
        return self.num/self.den

    # mutator, we will multiply the current Fraction by the Fraction parameter
    def multiplyFraction(self , fraction):
        self.num *= fraction.num
        self.den *= fraction.den

    def __str__(self):
        return str(self.num) + "/"  + str(self.den)