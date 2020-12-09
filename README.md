#  TV Streamer keep connection alive python script
## Problem
The problem is that the TV Streamer does not keep the connection alive after idling for another 5 minutes after no sound is presented from it. So the hearing aid and sound processor go back to the normal program 
## solutiion
 Tried a a few audio files that were out of range for processor / hearing aid to hear. so I used a sine tone wave to generate an audio at 30 hz  at -30 db  with 200 ms play timre seem to work reliably. I wrote this python script that let it play  every 250  second to keep the connection alive
## install
1.  install python and open your favorite terminal 
2.  do a git clone or download .zip file then extract it 
3.  `cd tv-streamer-keep-connection-alive`
4.  `pip install -r requirements.txt`
5.  `python audio.py`
## license
Apache 2.0 
