
import sys
from datetime import datetime, timedelta

"""
Converts a text file containing steps and captions into a subtitle file format.

00:00:00: Windows 11, XeonSilver CPU 

1
00:00:00 --> 00:00:05
- Windows 11, XeonSilver CPU


Author: Jenu Chacko
License: MIT
"""

if len(sys.argv) < 2:
    print("Please provide the filename as an argument.")
    sys.exit()

filename = sys.argv[1]

with open(filename) as fid:
    steps= fid.readlines()

display_duration = 5 #seconds

output_string = ''

for ix,step in enumerate(steps):
    time_    = step.split(': ')[0]
    caption_  = step.split(': ')[1]

    step_start = datetime.strptime(time_, '%H:%M:%S')
    step_end   = step_start + timedelta(seconds=display_duration)

    if ix!=len(steps)-1:
        next_step  = datetime.strptime(steps[ix+1].split(': ')[0], '%H:%M:%S')
    else:
        next_step = step_end

    if step_end<=next_step:
        start_time = step_start.strftime('%H:%M:%S')
        end_time   = step_end.strftime('%H:%M:%S')
        
    else:
        start_time = step_start.strftime('%H:%M:%S')
        end_time   = next_step.strftime('%H:%M:%S')
    
    srt_ = f'{ix+1}\n{start_time},001 --> {end_time},001\n{caption_}\n'

    output_string = output_string + srt_

# Write output_string to a file
with open(filename[:-4]+'.srt', 'w') as f:
    f.write(output_string)
