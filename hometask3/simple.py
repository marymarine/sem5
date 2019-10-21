"""Sequential program execution"""

import os
import time
import warnings
import librosa
import numpy as np

warnings.filterwarnings('ignore')

def extract_mfccs(test_dir, res_dir):
    """Search audio files (*.m4a) and create numpy arrays"""
    for name in os.listdir(test_dir):
        if name[-4:] == '.m4a':
            path = os.path.join(test_dir, name)
            #generate mfccs
            y, sr = librosa.load(path)
            mfcc = librosa.feature.mfcc(y, sr)
            #save to a binary file in .npy format
            np.save(res_dir, mfcc)
        else:
            #create directories in the resulting directory
            res_path = os.path.join(res_dir, name)
            os.mkdir(res_path)
            #execute the next iteration
            test_path = os.path.join(test_dir, name)
            extract_mfccs(test_path, res_path)
            continue

if __name__ == '__main__':
    start_time = time.time()
    #create the resulting directory
    res = os.path.join(os.getcwd(), 'result')
    os.mkdir(res)
    #create numpy arrays
    extract_mfccs(os.path.abspath("test"), res)
    #get program execution time
    print(time.time() - start_time)
