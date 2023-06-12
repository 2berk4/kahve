import math
import rumps
import pyautogui
import time


class KahveApp(object):
    def __init__(self):
        self.config = {
            "app_name": "Pomodoro",
            "start": "Start jiggle",
            "pause": "Pause jiggle",

            "break_message": "Time is up! Take a break :)",
            "interval": 1500,
        }
        self.app = rumps.App(self.config["app_name"])
        self.timer = rumps.Timer(self.on_tick, 10)
        self.interval = self.config["interval"]
        self.set_up_menu()
        self.start_pause_button = rumps.MenuItem(
            title=self.config["start"], callback=self.start_timer
        )
        self.app.menu = [self.start_pause_button]

    def set_up_menu(self):
        self.timer.stop()
        self.app.title = "☕"

    def on_tick(self, sender):
        if sender.jiggle:
                # Set the center of the circle
            center_x, center_y = 500, 500

            # Set the radius of the circle
            radius = 200

            # Set the angle increment for each step
            angle_increment = 20

            # Loop through the angles and move the mouse
            for angle in range(0, 360, angle_increment):
                # Calculate the x and y coordinates for the current angle
                x = center_x + int(radius * math.cos(math.radians(angle)))
                y = center_y + int(radius * math.sin(math.radians(angle)))
                
                # Move the mouse to the current coordinates
                pyautogui.moveTo(x, y, duration=0.000001)


    def start_timer(self, sender):
        if sender.title.lower().startswith(("start", "continue")):
            if sender.title == self.config["start"]:
                self.timer.jiggle = True
            sender.title = self.config["pause"]
            self.timer.start()
        else:
            sender.title = self.config["start"]
            self.timer.jiggle = False
            self.timer.stop()


    def stop_timer(self, sender):
        self.set_up_menu()
        self.start_pause_button.title = self.config["start"]

    def run(self):
        self.app.run()


if __name__ == "__main__":
    app = KahveApp()
    app.run()
