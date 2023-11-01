from djitellopy import tello
import time
tello = tello.Tello()

tello.connect()
tello.takeoff()

tello.curve_xyz_speed(25, -25, 0, 25, -50, 0, 20)
tello.curve_xyz_speed(25, -25, 0, 25, -75, 0, 20)

tello.land()