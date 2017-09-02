class CoordinateCalculator:

    global movement_history
    movement_history = [[0, 0]]

    global is_still_searching
    is_still_searching = True

    input = ""
    total_distance = 0
    firstLocationVisitedTwiceDistance = 0

    def __init__(self, instructions):
        self.input = instructions


    def addAndCheckTwiceVisit(self, array_to_add):
        global movement_history
        global is_still_searching
        if (is_still_searching and array_to_add in movement_history):
            is_still_searching = False
            coordinates_x, coordinates_y = array_to_add
            self.firstLocationVisitedTwiceDistance = abs(coordinates_x + coordinates_y)

        movement_history.append(array_to_add)

    def calcTaxiCabGeometryFrom(self):
        coordinate_x = 0
        coordinate_y = 0
        degrees = 0

        for movement in self.input.split(", "):
            if movement[0] == 'R':
                degrees += 90
            else:
                degrees -= 90

            module = degrees % 360
            steps = int(movement[1:])

            count = 0
            if (module == 0):
                while count < steps:
                    count += 1
                    self.addAndCheckTwiceVisit([coordinate_x, coordinate_y + count])
                coordinate_y += steps
            elif (module == 90 or module == -270):
                while count < steps:
                    count += 1
                    self.addAndCheckTwiceVisit([coordinate_x + count, coordinate_y])
                coordinate_x += steps
            elif (abs(module) == 180):
                while count < steps:
                    count += 1
                    self.addAndCheckTwiceVisit([coordinate_x, coordinate_y - count])
                coordinate_y -= steps
            elif (module == 270 or module == -90):
                while count < steps:
                    count += 1
                    self.addAndCheckTwiceVisit([coordinate_x - count, coordinate_y])
                coordinate_x -= steps

        self.total_distance = abs(coordinate_x) + abs(coordinate_y)
        return self