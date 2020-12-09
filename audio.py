import simpleaudio as sa
import time
filename = 'audio.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)
while(1):
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing
    time.sleep(250)
