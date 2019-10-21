"""Multiprocessing execution"""

import os
import time
import warnings
from multiprocessing import Process
import librosa
import numpy as np


warnings.filterwarnings('ignore')

def extract_mfccs(test_dir, res_dir):
    """"Create numpy arrays"""
    # generate mfccs
    y, sr = librosa.load(test_dir)
    mfcc = librosa.feature.mfcc(y, sr)
    # save an array to a binary file in .npy format
    np.save(res_dir, mfcc)

def run_processes(test_dir, res_dir):
    """Search audio files (*.m4a) and create processes"""
    processes = []
    for name in os.listdir(test_dir):
        test_path = os.path.join(test_dir, name)
        res_path = os.path.join(res_dir, name)
        if name[-4:] == '.m4a':
            # create and run new process
            proc = Process(target=extract_mfccs, args=(test_path, res_path,))
            processes.append(proc)
            proc.start()
        else:
            # create directories in the resulting directory
            os.mkdir(res_path)
            # execute the next iteration
            run_processes(test_path, res_path)
            continue
    for proc in processes:
        proc.join()

if __name__ == '__main__':
    start_time = time.time()
    # create the resulting directory
    res = os.path.join(os.getcwd(), 'result')
    os.mkdir(res)
    # create numpy arrays
    run_processes(os.path.abspath('test'), res)
    # get program execution time
    print(time.time() - start_time)
