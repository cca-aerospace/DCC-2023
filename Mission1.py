from djitellopy import tello
import time
tello = tello.Tello()

tello.connect()
tello.takeoff()

time.sleep(15)

tello.land()