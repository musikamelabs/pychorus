# Denoising size in seconds
SMOOTHING_SIZE_SEC = 2.5

# Number of samples to consider in one chunk.
# Smaller values take more time, but are more accurate
# N_FFT = 2**14
N_FFT = 4**14

# For line detection
LINE_THRESHOLD = 0.15
MIN_LINES = 4
NUM_ITERATIONS = 4

# We allow an error proportional to the length of the clip
OVERLAP_PERCENT_MARGIN = 0.5
