from machine import Pin, PWM
import time
from servo_translator import translate

# Expansion board servo connectors
SHOULDER_SERVO_PIN = 0  #shoulder servo
ELBOW_SERVO_PIN = 1     #elbow servo
WRIST_SERVO_PIN = 2     #pen up/down servo

#Minor calibtration offsets - trying to find the best value
SHOULDER_OFFSET = 0.0
ELBOW_OFFSET = 0.0

#Wrist servo has a very limited ranfe of motion - these cannot be exceeded
PEN_UP_POSITION = 0.0       #pen up position in degrees
PEN_DOWN_POSITION = 30.0    #pen down position in degrees

#time to wait between moves so the servos can reach their position
MOVE_DELAY = 20

#servo translator
class Servo:
    def __init__(self, pin: int):
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(50)  # Set frequency to 50Hz for standard servos

    def move (self, angle: float):
        #uses the translatore function from servo_translator.py to convert the angle in degrees to the corresponding input for the duty_u16 method of the servo class
        self.pwm.duty_u16(translate(angle))

    def disable(self):
        #stops sending PWM signals to the servo.
        self.pwm.duty_u16(0)
        self.pwm.deinit()  # Deinitialize the PWM to disable the servo

shoulder = Servo(SHOULDER_SERVO_PIN)
elbow = Servo(ELBOW_SERVO_PIN)
wrist = Servo(WRIST_SERVO_PIN)


#G-Code PArser

def parse_gcode_line(line: str):
    line = line.strip()
    #skip empty lines.
    if not line:
        return None

    words = line.split()
    command = words[0]

    params ={}
    for word in words[1:]:
        #First character is the paramter name, the rest is the value
        name = word[0].upper()
        value = float(word[1:])
        params[name] = value
    return (command, params)

def read_gcode_file(filename: str):
    commands = []
    with open(filename, 'r') as f:
        for line in f:
            command = parse_gcode_line(line)
            if command is not None:
                commands.append(command)
    return commands


#Command Interpreter

def execute_command(command:tuple):
    name, params = command
    if name == 'G1':
        move_to_angles(params)
    elif name == 'M3':
        pen_down()
    elif name == 'M5':
        pen_up()
    elif name == 'M18':
        disable_all_servos()
    else:
        print("Unknown command:", name)

def pen_up():
    wrist.move(PEN_UP_POSITION)
    time.sleep(MOVE_DELAY / 1000.0)

def pen_down():
    wrist.move(PEN_DOWN_POSITION)
    time.sleep(MOVE_DELAY / 1000.0)

def disable_all_servos():
    shoulder.disable()
    elbow.disable()
    wrist.disable()

def move_to_angles(params: dict):
    if "s" in params:
        shoulder.move(params["S"] + SHOULDER_OFFSET)
    if "e" in params:
        elbow.move(params["E"] + ELBOW_OFFSET)
    time.sleep(MOVE_DELAY / 1000.0)  # Convert milliseconds to seconds and give time for the servos to reach their position


#main program

def main(filename: str ="line.gcode"):
    print ("Drawing", filename)

    commands = read_gcode_file(filename)
    for command in commands:
        print(command)
        execute_command(command)

    print("Finished drawing")


if __name__ == "__main__":
    main()  