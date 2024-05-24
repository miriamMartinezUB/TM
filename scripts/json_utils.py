import json
import os

from tqdm import tqdm

name_json = 'video_info.json'


def get_path(input_path):
    return os.path.splitext(input_path)[0]


def save_info_encode(processed_video, gop, num_tiles, max_displacement, quality, fps, filters, filter_conv, input_path):
    info = {
        "gop": gop,
        "num_tiles": num_tiles,
        "max_displacement": max_displacement,
        "quality": quality,
        "frames": [],
        "fps": fps,
        "filters": filters,
        "filter_conv": filter_conv
    }

    for idx, frame in enumerate(tqdm(processed_video, desc="Saving frames", unit="frame")):
        frame_info = {
            "frame_index": idx,
            "frame_data": frame.tolist()
        }
        info["frames"].append(frame_info)
    path = get_path(input_path)
    with open(f"{path}/{name_json}", "w") as json_file:
        json.dump(info, json_file, indent=4)


def check_video_info_json(folder_path):
    json_file = os.path.join(folder_path, name_json)
    if os.path.exists(json_file):
        return True
    else:
        raise FileExistsError