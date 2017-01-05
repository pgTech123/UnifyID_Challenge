import wave
import get_random

def main():
    wav = wave.open("random_sound.wav", 'w')
    # (nchannels, sampwidth, framerate, nframes, comptype, compname)
    wav.setparams((2, 1, 44100, 0, 'NONE', 'not compressed'))
    # 2 channels * 44100 sample/sec * 3 sec
    num_random_numbers = 2 * 44100 * 3
    # 8 bits/sample -> range from -128 to 127
    audio = get_random.get_random(num_random_numbers, -128, 127)
    wav.writeframes(audio)

    wav.close()

if __name__ == '__main__':
    main()