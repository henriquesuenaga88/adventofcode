movement_history = [[0, 0]];
isStillSearching = True;

def addAndCheckTwiceVisit(arrayToAdd) :
    global isStillSearching;
    if (isStillSearching and arrayToAdd in movement_history) :
        isStillSearching = False;
        distance = abs(arrayToAdd[0]) + abs(arrayToAdd[1]);
        print "You visited twice:";
        print "...... x = " + str(arrayToAdd[0]);
        print "...... y = " + str(arrayToAdd[1]);
        print "The HQ is " + str(distance) + " blocks away.";

    movement_history.append(arrayToAdd);



def calcTaxiCabGeometryFrom(filePath):
    coordinate_x = 0;
    coordinate_y = 0;
    degrees = 0;

    input = open(str(filePath), "r").read();

    for movement in input.split(", ") :
        if movement[0] == 'R':
            degrees += 90;
        else :
            degrees += -90;

        module = degrees % 360;
        steps = int(movement[1:]);

        count = 0;
        if (module == 0):
            while count < steps :
                count += 1;
                addAndCheckTwiceVisit([coordinate_x, coordinate_y + count])
            coordinate_y += steps;
        elif (module == 90 or module == -270):
            while count < steps :
                count += 1;
                addAndCheckTwiceVisit([coordinate_x + count, coordinate_y])
            coordinate_x += steps;
        elif (abs(module) == 180):
            while count < steps :
                count += 1;
                addAndCheckTwiceVisit([coordinate_x, coordinate_y - count])
            coordinate_y -= steps;
        elif (module == 270 or module == -90):
            while count < steps :
                count += 1;
                addAndCheckTwiceVisit([coordinate_x - count, coordinate_y])
            coordinate_x -= steps;

    distance = abs(coordinate_x) + abs(coordinate_y);
    print "The final path is " + str(distance) + " blocks away.";

if __name__ == '__main__': calcTaxiCabGeometryFrom("input.txt")