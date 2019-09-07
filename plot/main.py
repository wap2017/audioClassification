from pydub import AudioSegment
import matplotlib.pyplot as plt
import wave
import numpy as np
import os

def trans_mp3_to_wav(filepath, targetpath ):
    song = AudioSegment.from_mp3(filepath)
    # print(song.raw_data)
    song.export(targetpath, format="wav")


# if __name__ == "__main__":
#     a = os.listdir("./data")
#     print()

if __name__ == "__main__":
    # trans_mp3_to_wav("./data/abc.mp3")
    f = wave.open("./data/train_do/do0.wav")
    nchannels, width, frame_rate, frame_n = f.getparams()[:4]
    print(nchannels)
    print(frame_n)
    time = np.arange(0, frame_n) * (1.0/frame_rate)
    strData = f.readframes(frame_n)
    waveData = np.frombuffer(strData,np.short)
    waveData = waveData * 1.0 / np.max(np.abs(waveData))
    print(time.shape)
    print(waveData.shape)
    plt.plot(time, waveData)
    plt.show()
