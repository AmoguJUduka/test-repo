class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid Format")
        self.filename = filename
        

class MP3(AudioFile):
    ext = "mp3"
    def play(self):
        print("Playing an MP3 file")

class ogg(AudioFile):
    ext = "ogg"
    def play(self):
        print("Playing ogg file")

