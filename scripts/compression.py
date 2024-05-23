import os
import numpy as np
import cv2
from scipy.fftpack import dct

# Functions for video processing (split_into_tiles, calculate_dct, calculate_correlation, process_video)...

def video_size_in_kbytes(video):
    """
    Calculate the size of the video in kilobytes.
    """
    total_size = sum(os.path.getsize(frame) for frame in video)
    return total_size / 1024

def compression(original_video, processed_video):
# Compute sizes
    original_size_kb = video_size_in_kbytes(original_video)
    processed_size_kb = video_size_in_kbytes(processed_video)

    # Compute the difference
    size_difference_kb = processed_size_kb - original_size_kb

    print("Original Video Size: {:.2f} KB".format(original_size_kb))
    print("Processed Video Size: {:.2f} KB".format(processed_size_kb))
    print("Difference in Size: {:.2f} KB".format(size_difference_kb))