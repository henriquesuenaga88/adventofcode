from coordinateCalculator import CoordinateCalculator

def startCoordinateCalculator() :

    input = open("input.txt", "r").read()
    calculator = CoordinateCalculator(input).calcTaxiCabGeometryFrom();

    print "---------------------------------------------"
    print "--------------- AdventOfCode ----------------"
    print "---------------------------------------------"
    print "Q: How far from the starting point the full instructions leaves you?"
    print "A: The total distance is {} blocks"\
        .format(calculator.total_distance);
    print "---------------------------------------------"
    print "Q: How far is the Easter Bunny Headquarters?"
    print "A: The Easter Bunny HQ is {} blocks away from your starting point."\
        .format(calculator.firstLocationVisitedTwiceDistance);

if __name__ == '__main__': startCoordinateCalculator()
