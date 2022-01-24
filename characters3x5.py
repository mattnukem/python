# This module creates a 3x5 pixel font system for the Pimoroni Unicorn HAT HD. It outputs a
# set of x and y coordinates and an RGB value in the format of a nested list: [x, y, r, g, b].

# The 'charactertable' dictionary defines the relative x and y coordinates of all of the 
# characaters and indexes them to their respective characater.
charactertable = {0: [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [4, 1], [4, 0],
                      [3, 0], [2, 0], [1, 0]],
    1: [[0, 2], [1, 2], [2, 2], [3, 2], [4, 2]],
    2: [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [2, 1], [2, 0], [3, 0], [4, 0], [4, 1], [4, 2]],
    3: [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [2, 1], [2, 0], [3, 2], [4, 2], [4, 1], [4, 0]],
    4: [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2], [1, 2], [0, 2], [3, 2], [4, 2]],
    5: [[0, 2], [0, 1], [0, 0], [1, 0], [2, 0], [2, 1], [2, 2], [3, 2], [4, 2], [4, 1], [4, 0]],
    6: [[0, 2], [0, 1], [0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [4, 1], [4, 2], [3, 2], [2, 2],
        [2, 1]],
    7: [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2], [4, 2]],
    8: [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [4, 1], [4, 0], [3, 0], [2, 0],
        [1, 0], [2, 1]],
    9: [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [2, 1], [2, 0], [3, 2], [4, 2], [4, 1], [4, 0],
        [1, 0]]}

# The 'colortable' dictionary defines a set of RGB values and indexes them to their name.
colortable = {'red': [255, 0, 0], 'light red': [255, 75, 75], 'green': [0, 255, 0],
    'light green': [75, 255, 75], 'lime': [150, 255, 0], 'blue': [0, 0, 255],
    'light blue': [75, 75, 255], 'yellow': [255, 255, 0], 'cyan': [0, 255, 255],
    'pink': [255, 0, 255], 'orange': [255, 128, 0], 'purple': [128, 0, 255],
    'white': [255, 255, 255]}

# The 'ledlistmaker' function takes inputs of the desired character and color, and returns a
# nested list necessary to draw the character using the unicornhathd.set_point function.
def ledlistmaker(character, color, xoffset, yofffset):

    # Making an empty list
    ledlist = []

    # Covert the incoming character to an integer if it's a number, else a string.
    if character.isnumeric():
        character = int(character)
    else:
        character = str(character)

    # Pulling the desired color RGB values from 'colortable'
    rgb = colortable[color]

    # For each coordinate pair (x) in the list pulled from 'charactertable' for the desired
    # character, we form a new list made up of the x, y, and RGB values, and append them to
    # 'ledlist'.
    for x in charactertable[character]:
        ledlist.append([x[0] + xoffset, x[1] + yofffset, rgb[0], rgb[1], rgb[2]])

    # Return the nested list.
    return ledlist
