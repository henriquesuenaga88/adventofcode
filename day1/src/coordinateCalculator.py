class CoordinateCalculator:

    global movement_history
    movement_history = [[0, 0]]

    global is_still_searching
    is_still_searching = True

    total_distance = 0
    first_location_visited_twice_distance = 0

    def __init__(self, instructions):
        self.input = instructions


    def add_and_check_twice_visit(self, array_to_add):
        global movement_history
        global is_still_searching
        if (is_still_searching and array_to_add in movement_history):
            is_still_searching = False
            coordinates_x, coordinates_y = array_to_add
            self.first_location_visited_twice_distance = abs(coordinates_x + coordinates_y)

        movement_history.append(array_to_add)

    def calc_taxicab_geometry_from(self):
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

            while switch(module):
                count = 0
                if case(0): #North
                    while count < steps:
                        count += 1
                        self.add_and_check_twice_visit([coordinate_x, coordinate_y + count])
                    coordinate_y += steps
                if case(90, -270): #East
                    while count < steps:
                        count += 1
                        self.add_and_check_twice_visit([coordinate_x + count, coordinate_y])
                    coordinate_x += steps
                if case(180, -180):#South
                    while count < steps:
                        count += 1
                        self.add_and_check_twice_visit([coordinate_x, coordinate_y - count])
                    coordinate_y -= steps
                if case(270, -90):#West
                    while count < steps:
                        count += 1
                        self.add_and_check_twice_visit([coordinate_x - count, coordinate_y])
                    coordinate_x -= steps
                break

        self.total_distance = abs(coordinate_x) + abs(coordinate_y)
        return self

class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switch.value for arg in args))
