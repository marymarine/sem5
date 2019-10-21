"""Multithreading execution"""

import os
import time
import warnings
from threading import Thread
import librosa
import numpy as np

warnings.filterwarnings('ignore')

def extract_mfccs(test_dir, res_dir):
    """"Create numpy arrays"""
    # generate mfccs
    y, sr = librosa.load(test_dir)
    mfcc = librosa.feature.mfcc(y, sr)
    # save to a binary file in .npy format
    np.save(res_dir, mfcc)

def run_threads(test_dir, res_dir):
    """Search audio files (*.m4a) and create threads"""
    threads = []
    for name in os.listdir(test_dir):
        test_path = os.path.join(test_dir, name)
        res_path = os.path.join(res_dir, name)
        if name[-4:] == '.m4a':
            # create and run new thread
            thr = Thread(target=extract_mfccs, args=(test_path, res_path,))
            threads.append(thr)
            thr.start()
        else:
            # create directories in the resulting directory
            os.mkdir(res_path)
            # execute the next iteration
            run_threads(test_path, res_path)
            continue
    for thr in threads:
        thr.join()

if __name__ == '__main__':
    start_time = time.time()
    # create the resulting directory
    res = os.path.join(os.getcwd(), 'result')
    os.mkdir(res)
    # create numpy arrays
    run_threads(os.path.abspath('test'), res)
    # get program execution time
    print(time.time() - start_time)
