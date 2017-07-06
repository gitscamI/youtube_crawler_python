from pydub import AudioSegment
from os.path import join
import re

def m4aToWav(filename, outDir):
    try:
        sound = AudioSegment.from_file(filename, "m4a")
    except Exception as e:
        print(str(e))
        return
    # remove forward directory and .m4a in filename
    filename = filename.split('/')
    order = len(filename) -1
    filename = filename[order]
    filename = filename.split('.')
    filename = filename[0] + '.wav'

    sound.export(join(outDir, filename), format = 'wav')

if __name__ == '__main__':
    filename = './Music/live concert 1983 In Hong Kong 邓丽君Teresa Teng - hit song2.m4a'
    outDir = './'
    m4aToWav(filename, outDir)
