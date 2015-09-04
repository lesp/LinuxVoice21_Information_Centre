#!/usr/bin/env python
import vlc, time
import dothat.touch as j
import dothat.lcd as l
import dothat.backlight as b
import signal
import os
import feedparser
import math



def feedme(feed):
    feed = feedparser.parse(feed.encode('utf-8'))
    for i in range(6):
        b.graph_set_led_state(i,1)
        print(feed['entries'][i]['title'])
        scrollText(feed['entries'][i]['title'])
    b.graph_off()

l.clear()

def scrollText(scrollBlurb):
  if len(scrollBlurb) > 16:
    padding = " " * 16
    oldText = scrollBlurb
    scrollBlurb = padding + scrollBlurb + " "
    for i in range(0,len(scrollBlurb)):
      l.set_cursor_position(0,0)
      l.write(scrollBlurb[i:(i+16)])
      time.sleep(0.25)
  else:
    l.set_cursor_position(0,0)
    l.write(scrollBlurb)
    print(scrollBlurb)


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
try:
    b.graph_off()
    @j.on(j.UP)
    def handle_up(ch,evt):
      print("Up pressed!")
      l.clear()
      b.rgb(128,0,128)
      l.write("BBC Radio 2")
      player(radio2)

    @j.on(j.DOWN)
    def handle_down(ch,evt):
      print("Down pressed!")
      l.clear()
      b.rgb(87,145,146)
      l.write("BBC 6 Music")
      player(radio6)

    @j.on(j.LEFT)
    def handle_left(ch,evt):
      print("Left pressed!")
      l.clear()
      l.write("BBC NEWS")
      time.sleep(1)
      l.clear()
      b.rgb(0,0,128)
      feedme("http://feeds.bbci.co.uk/news/rss.xml")

    @j.on(j.RIGHT)
    def handle_right(ch,evt):
      print("Right pressed!")
      l.clear()
      b.rgb(0,128,0)
      l.write("Hackaday RSS")
      time.sleep(1)
      l.clear()
      feedme("https://hackaday.com/blog/feed/")

    @j.on(j.BUTTON)
    def handle_button(ch,evt):
      print("Button pressed!")
      l.clear()
      x = 0
      l.set_cursor_position(0,0)
      l.write("Linux Voice")
      for i in range(5):
        x+=1
   
        b.sweep( (x%360)/360.0)
        b.set_graph(abs(math.sin(x/100.0)))
        time.sleep(0.01)  

        
    @j.on(j.CANCEL)
    def handle_cancel(ch,evt):
      print("Cancel pressed!")
      l.clear()
      b.rgb(0,0,0)
      stop()

    # Prevent the script exiting!
    signal.pause()
except KeyboardInterrupt:
    stop()
