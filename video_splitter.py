
import json
from pprint import pprint
import imageio
imageio.plugins.ffmpeg.download()
import moviepy.editor as mpy
import datetime

with open('c:/tervil/Input_paramter.json') as f:
    data = json.load(f)

pprint(data)
i_start_time = data["start_time"]
i_end_time = data["end_time"]
i_video_split_fl_nm = data["video_split_fl_nm"]
i_video_split_fl_nm_fin = "c:/tervil/" + i_video_split_fl_nm
pprint(i_video_split_fl_nm_fin)



from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip("c:/tervil/file_example.mp4",i_start_time , i_end_time, targetname=i_video_split_fl_nm_fin)

