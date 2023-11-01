from djitellopy import tello
import time
tello = tello.Tello()

tello.connect()
tello.takeoff()

for i in range(4):
    tello.move_forward(50)
    tello.rotate_counter_clockwise(90)

tello.land()