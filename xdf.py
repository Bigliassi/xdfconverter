# First, make sure to install the pyxdf package:
# pip install pyxdf

import pyxdf

# Ask the user for the filename
filename = input("Please enter the name of the XDF file (e.g., 'your_eeg_data_file.xdf'): ")

# Load the XDF file
data, header = pyxdf.load_xdf(filename)

# Iterate over each stream in the data
for stream in data:
    print(f"Stream Name: {stream['info']['name'][0]}")
    print(f"Number of Channels: {stream['info']['channel_count'][0]}")
    print(f"Sample Rate: {stream['info']['nominal_srate'][0]} Hz")
    print(f"Number of Samples: {len(stream['time_series'])}")
    print(f"First 5 Samples:\n{stream['time_series'][:5]}\n")
