from abc import ABC, abstractmethod

class Electronics(ABC):
    @abstractmethod
    def play_video():
        pass
class laptop(Electronics):
    def play_video(self):
        print("press play button from keyboard")
class mobile(Electronics):
    def play_video(self):
        print("press play button from keypad")
laptop1 = laptop()
laptop1.play_video()
mobile1 = mobile()
mobile1.play_video()