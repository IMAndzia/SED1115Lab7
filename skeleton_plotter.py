from machine import Pin, PWM
from servo_translator import translate

#constants

#Expansion board servo connectors
SHOULDER_SERVO_PIN = 0  #shoulder servo
ELBOW_SERVO_PIN = 1     #elbow servo
WRIST_SERVO_PIN = 2     #pen up/down servo

#Minor Caliibration offsets - trying to find the best value
SHOULDER_OFFSET = 0.0
ELBOW_OFFSET = 0.0

#wrist servo has a very limited range 0-30 - these cannot be exceeded
PEN_UP_POSITION = 0.0       #pen up position in degrees 
PEN_DOWN_POSITION = 30.0    #pen down position in degrees

#time to wait between moves so the servos can reach their position
MOVE_DELAY = 20

class Servo:
    def __init__(self, pin: int):
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(50)  # Set frequency to 50Hz for standard servos
    def move(self, angle: float):
        #I have to write the code to move the servo to the specified angle. I will use the translate() function from the servo_translator.py file to convert the angle in degrees to the corresponding input for the duty_u16 method of the servo class.
        pass

    def disable(self):
        #I have to write the code to stop sending PWM signals to the servo. I will use the deinit() method of the PWM class to disable the servo.
        pass
    

shoulder = Servo(SHOULDER_SERVO_PIN)
elbow = Servo(ELBOW_SERVO_PIN)
wrist = Servo(WRIST_SERVO_PIN)

#G-Code Paser

def read_gcode_file(filename: str):
    #I have to write the code to read a G-Code file and parse it into a list of commands and parameters. I will use the parse_gcode_line() function to parse each line of the file.
    pass

def parse_gcode_line(line: str):
    #havent finished yet. I have to write the code to parse a single line of G-Code and return a tuple containing the command and a dictionary of parameters. I will split the line into words and extract the command and parameters from it, also the strip and split methods will be used to remove any leading or trailing whitespace and split the line into words. The first word is the command, and the rest are parameters in the form of a letter followed by a number. I will use a for loop to iterate over the parameters and extract the name and value of each parameter, and store them in a dictionary.
    pass


#command interpreter

def execute_command(command: str, params: dict):
    #havent finished yet. I have to write the code to execute a single G-Code command with the given parameters. I will use if/elif statements to check the command and call the appropriate function to move the servos or perform other actions.
    pass

def move_to_position(params: dict):
   #have to check for "S" and "E" parameters in the params dictionary, and if they are present, I will move the shoulder and elbow servos to the specified angles using the move() method of the Servo class. I will also add the calibration offsets to the angles before moving the servos. If the "S" or "E" parameters are not present, I will use the current position of the servos as the default value.
   pass

def pen_up():
    #I have to write the code to move the wrist servo to the pen up position using the move() method of the Servo class.
    pass

def pen_down():
    #I have to write the code to move the wrist servo to the pen down position using the move() method of the Servo class.
    pass

def disable_all_servos():
    #I have to write the code to disable all the servos by calling the disable() method of each Servo object.
    pass


#main program
def main(filename:str = "line.gcode"):
    #I have to write the code to read the G-Code file, parse it into a list of commands, and execute each command in order. I will use the read_gcode_file() function to read the file and get the list of commands, and then use a for loop to iterate over the commands and call the execute_command() function for each command.
    pass

if __name__ == "__main__":
    main()