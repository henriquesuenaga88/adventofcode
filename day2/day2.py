dict = {
      'U': -1
    , 'D': 1
    , 'L': -1
    , 'R': 1
}

x_position = 1;
y_position = 1;

def getKeypadFromPosition(x, y) :
    keypad = [
          ['1', '2', '3']
        , ['4', '5', '6']
        , ['7', '8', '9']
    ];

    return keypad[y][x];

def isAcceptableVerticalValue(direction) :
    return direction in ['U','D'] and ((
                                           direction == 'U'
                                           and y_position > 0
                                       ) or
                                       (
                                           direction == 'D'
                                           and y_position < 2
                                       ))

def isAcceptableHorizontalValue(direction) :
    return direction in ['L', 'R'] and ((
                                            direction == 'L'
                                            and x_position > 0
                                        ) or
                                        (
                                            direction == 'R'
                                            and x_position < 2
                                        ));

def getPasswordUnitFrom(line) :
    global x_position, y_position;

    for direction in line :
        if isAcceptableVerticalValue(direction) :
            y_position += dict[direction];
        elif isAcceptableHorizontalValue(direction) :
            x_position += dict[direction];

    return getKeypadFromPosition(x_position, y_position);


def getBathroomPasswordFrom(filePath) :
    file = open(filePath, "r").readlines()

    password = "";
    for line in file :
        password += getPasswordUnitFrom(line);

    print "password is " + password;


if __name__ == '__main__': getBathroomPasswordFrom("input.txt")