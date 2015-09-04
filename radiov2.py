import vlc, time
import dothat.touch as j
import dothat.lcd as l
import dothat.backlight as b
import signal

global p
smooth = "http://media-ice.musicradio.com:80/SmoothNorthWestMP3"
radio2 ="http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio2_mf_p?s=1441287890&e=1441302290&h=6bbd33e79355706e2815c2c4c508dbeb"
radio6 = "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_6music_mf_p?s=1441280021&e=1441294421&h=f2fdb3ac23e533316da8c536dd399e67"

def player(radio):
    global p
    p = vlc.MediaPlayer(radio)
    p.play()

def stop():
    p.stop()

stations = [smooth,radio2,radio6]
for station in stations:
    player(station)
    time.sleep(5)
    stop()



