import cv2

def extract_frames_from_video(video_path):
    """
    Extract frames from a video.
    :param video_path: path to the video.
    :return: a list of frames
    """
    # Abrir el archivo de video
    cap = cv2.VideoCapture(video_path)
    frames = []

    # Verificar si el video se abrió correctamente
    if not cap.isOpened():
        print(f"Error: No se puede abrir el archivo de video {video_path}")
        return frames

    # Leer los frames del video
    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Fin del video
        frames.append(frame)

    # Liberar el objeto VideoCapture
    cap.release()
    return frames