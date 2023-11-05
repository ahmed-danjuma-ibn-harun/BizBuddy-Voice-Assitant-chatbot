import os
import argparse
from pydub import AudioSegment
from pydub.utils import make_chunks
from glob import glob

def main(args):
    
    def chunk_and_save(path):
        folder=path
        waves = glob(folder+'/'+ '*.wav')
        #print ('w',waves)
        for i in waves:
            w = i
            myaudio = AudioSegment.from_file(i)
            chunk_length_ms = args.seconds * 1000
            chunks = make_chunks(myaudio, chunk_length_ms)
            #print(chunks)
            for i, chunk in enumerate(chunks):
                chunk_name = w.split("\\")[-1].split('.')[0] + "chunk{0}.wav".format(i)
                print (chunk_name)
                wav_path = os.path.join(args.save_path, chunk_name)
                print(wav_path)
                if chunk.duration_seconds >=1:
                    chunk.export(wav_path, format="wav") 
                    print ("exported", chunk_name)
                else:
                    pass

    chunk_and_save(args.audio_file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="script to split audio files into chunks")
    parser.add_argument('--seconds', type=int, default=3,
                        help='if set to None, then will record forever until keyboard interrupt')
    parser.add_argument('--audio_file_path', type=str, default='convert/', required=False,
                        help='path of audio files')
    parser.add_argument('--save_path', type=str, default='../data/not_wake/', required=False,
                        help='full path to to save data. i.e. /to/path/saved_clips/')

    args = parser.parse_args()

    main(args)