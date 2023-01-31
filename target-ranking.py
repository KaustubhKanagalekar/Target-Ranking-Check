class Target:

    def __init__(self, shape_color, char_color, shape_type, char_type):
        self.shape_color = shape_color 
        self.char_color = char_color 
        self.shape_type = shape_type 
        self.char_type = char_type 

def checking_target_sc(predicted_target, expected_targets):
    final_list = []

    for expected_target in expected_targets:
        excol = valid_colors[expected_target.shape_color]
        prcol = valid_colors[predicted_target.shape_color]
        final_list.append(abs(excol - prcol))
    return final_list

def checking_target_cc(predicted_target, expected_targets):
    final_list = []

    for expected_target in expected_targets:
        excol = valid_colors[expected_target.char_color]
        prcol = valid_colors[predicted_target.char_color]
        final_list.append(abs(excol - prcol))
    return final_list

def checking_target_st(predicted_target, expected_targets):
    final_list = []
    for expected_target in expected_targets:
        exshp = valid_shapes[expected_target.shape_type]
        prshp = valid_shapes[predicted_target.shape_type]
        final_list.append(abs(exshp - prshp))
    return final_list

def checking_target_ct(predicted_target, expected_targets):
    final_list = []
    for expected_target in expected_targets:
        excol = valid_let[expected_target.char_type]
        prcol = valid_let[predicted_target.char_type]
        final_list.append(abs(excol - prcol))
    return final_list



target1 = Target("red", "red", "circle", "A")
target2 = Target("orange", "orange", "square", "K")
target3 = Target("blue", "blue", "semicircle", "3")
target4 = Target("gray", "gray", "octagon", "9")
target5 = Target("yellow", "yellow", "triangle", "E")
target6 = Target("brown", "brown", "pentagon", "Y")

predicted = Target("orange", "yellow", "square", "G")



expected_targets = [target5, target2, target3] 

valid_colors = {
"white" : 0,
"black" : 10,
"gray": 9, 
"blue": 1, 
"green": 3,
"yellow": 4,
"red" : 7,
"purple" : 2,
"brown" : 8,
"orange" : 6
}

valid_shapes = {
"circle" : 10 ,
"semicircle" : 3,
"quartercircle" : 2,
"triangle" :1,
"square" : 4,
"rectangle": 4.5,
"trapezoid" : 3.5,
"pentagon": 5,
"hexagon" : 6,
"heptagon": 7,
"octagon": 8,
"star": 0,
"cross": 4.25
}

valid_let = {
"A" : 1,
"B" : 2,
"C" : 3,
"O" : 4,
"0" : 4.5,
"D" : 5,
"E" : 6,
"3" : 6.5,
"F" : 7,
"G" : 8,
"6" : 8.5,
"9" : 8.75,
"H": 10,
"I" : 11,
"1" : 11.5,
"J" : 12,
"K" : 13,
"L" : 14,
"M" : 15,
"W" : 15.5,
"N" : 16,
"Z": 16.5,
"P" : 18,
"Q" : 19,
"R": 20,
"S": 21,
"5": 21.5,
"T" : 22,
"U": 23,
"V": 24,
"X": 25,
"Y": 26,
"2": 27,
"4": 28,
"7": 29,
"8": 30,
}

print(checking_target_sc(predicted, expected_targets))
print(checking_target_cc(predicted, expected_targets))
print(checking_target_st(predicted, expected_targets))
print(checking_target_ct(predicted, expected_targets))