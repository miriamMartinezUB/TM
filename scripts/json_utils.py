import json
import os

name_json = 'video_info.json'


def get_path(input_path):
    return os.path.splitext(input_path)[0]


def save_info_encode(frames_info, gop, num_tiles, max_displacement, quality, fps, filters, filter_conv, input_path):
    info = {
        "gop": gop,
        "num_tiles": num_tiles,
        "fps": fps,
        "filters": filters,
        "filter_conv": filter_conv,
        "frames_info": frames_info
    }

    path = get_path(input_path)
    with open(f"{path}/{name_json}", "w") as json_file:
        json.dump(info, json_file, indent=4)


def check_video_info_json(folder_path):
    json_file = os.path.join(folder_path, name_json)
    if os.path.exists(json_file):
        return True
    else:
        raise FileExistsError