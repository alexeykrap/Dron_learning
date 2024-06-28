from practice4 import Drone
import time

drone1 = Drone('T-1000', 5, 2000, '12342341')
# drone1.get_info()
# drone1.get_coords()
# drone1.get_dist()
# drone1.camera.live_video_on()
# time.sleep(5)
# drone1.camera.live_video_off()

drone1.flight_controller.takeoff()