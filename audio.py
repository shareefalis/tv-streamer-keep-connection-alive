import simpleaudio as sa
import time
import sys
filename = 'audio.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)
while(1):
    try:
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Wait until sound has finished playing
        time.sleep(250)
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        pass
