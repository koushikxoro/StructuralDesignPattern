from tv import TV
from dvdoplayer import DVDPlayer
from soundsystem import SoundSystem
from hometheaterfacade import HomeTheaterFacade
if __name__=="__main__":
    tv=TV()
    dvd_player=DVDPlayer()
    sound_system=SoundSystem()
    home_theater=HomeTheaterFacade(tv,sound_system,dvd_player)
    home_theater.watch_movie("Kantara")
    home_theater.end_movie()