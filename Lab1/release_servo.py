import pymycobot as mc

# Example:
#       mycobot-M5:
#           linux:
#              mc = MyCobot("/dev/ttyUSB0", 115200)
#          or mc = MyCobot("/dev/ttyAMA0", 115200)
#           windows:
#              mc = MyCobot("COM3", 115200)
from pymycobot import MyCobot
mc = MyCobot("COM8 ", 115200)
mc.release_all_servos()
