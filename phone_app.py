from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
import random
import time


class SoundAppLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.label = Label(text="Press play to start the process")
        self.add_widget(self.label)

        self.start_button = Button(text="Play")
        self.start_button.on_press = self.start_process
        self.add_widget(self.start_button)

        self.pause_button = Button(text="Pause")
        self.pause_button.on_press = self.pause_process
        self.add_widget(self.pause_button)

        self.restart_button = Button(text="Restart")
        self.restart_button.on_press = self.restart_process
        self.add_widget(self.restart_button)

        self.current_phase = 0
        self.phases = [
            4.6154,
            4.2857,
            4.0000,
            3.7500,
            3.5294,
            3.3333,
            3.1589,
            3.0000,
            2.8571,
            2.7273,
            2.6087,
        ]
        self.end_time = 0
        self.is_paused = False
        self.scheduled_event = None
        self.last_played_number = None
        self.remaining_time = 0

    def start_process(self):
        if self.is_paused:
            self.end_time = time.time() + self.remaining_time
            self.scheduled_event = Clock.schedule_interval(
                self.play_sound, self.phases[self.current_phase]
            )
            self.play_sound(0)
        else:
            self.current_phase = 0
            self.start_phase()
            self.play_sound(0)
        self.is_paused = False

    def pause_process(self):
        if self.scheduled_event:
            self.remaining_time = self.end_time - time.time()
            Clock.unschedule(self.scheduled_event)
            self.scheduled_event = None
            self.is_paused = True
            self.label.text = f"Paused\nTransition: {self.current_phase + 1}\nNumber: {self.last_played_number}"

    def restart_process(self):
        if self.scheduled_event:
            Clock.unschedule(self.scheduled_event)
            self.scheduled_event = None

        self.current_phase = 0
        self.is_paused = False
        self.end_time = 0
        self.last_played_number = None
        self.remaining_time = 0
        self.label.text = "Press play to start the process"

    def start_phase(self):
        if self.current_phase < len(self.phases) and not self.is_paused:
            self.end_time = time.time() + 180
            self.scheduled_event = Clock.schedule_interval(
                self.play_sound, self.phases[self.current_phase]
            )
        elif not self.is_paused:
            self.label.text = "Done!"

    def play_sound(self, dt):
        if time.time() >= self.end_time:
            if not self.is_paused:
                Clock.unschedule(self.scheduled_event)
                self.current_phase += 1
                if self.current_phase < len(self.phases):
                    transition_text = f"Transition: {self.current_phase + 1}"
                    self.label.text = transition_text
                    playsound = SoundLoader.load("sounds/Beep.mp3")
                    if playsound:
                        playsound.play()
                    self.start_phase()
                else:
                    self.label.text = "Done!"
            return False
        self.last_played_number = random.randint(1, 4)
        sound = SoundLoader.load(f"sounds/{self.last_played_number}.mp3")
        if sound:
            sound.play()
        self.label.text = f"Playing\nTransition: {self.current_phase + 1}\nNumber: {self.last_played_number}"


class SoundApp(App):
    def build(self):
        return SoundAppLayout()


if __name__ == "__main__":
    SoundApp().run()
