from coordinateCalculator import CoordinateCalculator

def start_coordinate_calculator() :

    input = open("input.txt", "r").read()
    calculator = CoordinateCalculator(input).calc_taxicab_geometry_from();

    print ("---------------------------------------------")
    print ("--------------- AdventOfCode ----------------")
    print ("---------------------------------------------")
    print ("Q: How far from the starting point the full instructions leaves you?")
    print ("A: The total distance is {} blocks"\
        .format(calculator.total_distance));
    print ("---------------------------------------------")
    print ("Q: How far is the Easter Bunny Headquarters?")
    print ("A: The Easter Bunny HQ is {} blocks away from your starting point."\
        .format(calculator.first_location_visited_twice_distance));

if __name__ == '__main__': start_coordinate_calculator()
