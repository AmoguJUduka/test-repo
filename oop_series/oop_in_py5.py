class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid Format")
        self.filename = filename
    
   
class MP3(AudioFile):
    ext = "mp3"
    def play(self):
        print(f"Playing a {self.ext} MP3 file")

class ogg(AudioFile):
    ext = "ogg"
    def play(self):
        print("Playing ogg file")

b = MP3("music.mp3")
b.play()
