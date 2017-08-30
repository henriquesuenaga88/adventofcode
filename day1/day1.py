def calcTaxiCabGeometry(filePath):
    degrees = 0;
    coordinate_x = 0;
    coordinate_y = 0;

    input = open(str(filePath), "r").read();

    for movement in input.split(", ") :
        if movement[0] == 'R':
            degrees += 90;
        else :
            degrees += -90;

        module = degrees % 360;

        steps = int(movement[1:]);

        if (module == 0):
            coordinate_y += steps;
        elif (module == 90 or module == -270):
            coordinate_x += steps;
        elif (abs(module) == 180):
            coordinate_y -= steps;
        elif (module == 270 or module == -90):
            coordinate_x -= steps;

    distance = abs(coordinate_x) + abs(coordinate_y);
    print "The distance is " + str(distance);

if __name__ == '__main__': calcTaxiCabGeometry("input.txt")