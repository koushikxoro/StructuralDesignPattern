class HomeTheaterFacade:
    def __init__(self,tv,soundsystem,dvd):
        self.tv=tv
        self.soundsystem=soundsystem
        self.dvd=dvd
    def watch_movie(self,movie):
        self.tv.on()
        self.soundsystem.on()
        self.dvd.on()
        self.soundsystem.set_volume(45)
        self.dvd.play_movie(movie)
    def end_movie(self):
        self.tv.off()
        self.soundsystem.off()
        self.dvd.off()