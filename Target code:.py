class Target:

    def __init__(self, shape_color, char_color, shape_type, char_type):
        self.shape_color = shape_color 
        self.char_color = char_color 
        self.shape_type = shape_type 
        self.char_type = char_type 

def checking_target(predicted_target, expected_targets):

    for expected_target in expected_targets:
        print(type(expected_target.shape_color))
        print(type(predicted_target.shape_color))
        if expected_target.shape_color == predicted_target.shape_color:
            return 1 
        else: 
            return 0



red = Target("red", "yellow", "circle", "A")
orange = Target("orange", "yellow", "circle", "A")
blue = Target("blue", "yellow", "circle", "A")
predicted = Target("red", "yellow", "circle", "A")

expected_targets = [red, orange, blue] 


print(checking_target(predicted, expected_targets))
