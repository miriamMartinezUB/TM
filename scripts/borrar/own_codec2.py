import cv2
import numpy as np


def subdivide_image(image, tess_size):
    height, width = image.shape[:2]
    tessels = []

    for y in range(0, height, tess_size):
        for x in range(0, width, tess_size):
            tessel = image[y:y + tess_size, x:x + tess_size]
            tessels.append((x, y, tessel))

    return tessels


def calculate_correlation(tessel1, tessel2):
    # Usamos la correlación normalizada entre tesselas
    return cv2.matchTemplate(tessel1, tessel2, method=cv2.TM_CCOEFF_NORMED)[0][0]


def process_images(reference_image, current_image, tess_size, max_shift, quality_factor):
    height, width = reference_image.shape[:2]
    tessels_ref = subdivide_image(reference_image, tess_size)
    tessels_cur = subdivide_image(current_image, tess_size)

    for x, y, tessel_cur in tessels_cur:
        best_match = None
        best_score = -1

        for dx in range(-max_shift, max_shift + 1):
            for dy in range(-max_shift, max_shift + 1):
                nx, ny = x + dx * tess_size, y + dy * tess_size

                if 0 <= nx < width and 0 <= ny < height:
                    tessel_ref = reference_image[ny:ny + tess_size, nx:nx + tess_size]

                    if tessel_ref.shape == tessel_cur.shape:
                        score = calculate_correlation(tessel_ref, tessel_cur)

                        if score > best_score:
                            best_score = score
                            best_match = (nx, ny, tessel_ref)

        if best_score >= quality_factor:
            # Marcar tessel para eliminación
            current_image[y:y + tess_size, x:x + tess_size] = np.mean(reference_image, axis=(0, 1))

    return current_image


def main(video_path, tess_size, max_shift, quality_factor, gop_size, output_path):
    cap = cv2.VideoCapture(video_path)
    ret, first_frame = cap.read()

    if not ret:
        print("Error al abrir el vídeo.")
        return

    height, width = first_frame.shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (width, height))

    reference_frame = first_frame

    while True:
        gop_frames = [reference_frame]

        for _ in range(gop_size - 1):
            ret, frame = cap.read()
            if not ret:
                break
            gop_frames.append(frame)

        for i, frame in enumerate(gop_frames):
            if i == 0:
                out.write(frame)
            else:
                processed_frame = process_images(reference_frame, frame, tess_size, max_shift, quality_factor)
                out.write(processed_frame)

        reference_frame = gop_frames[-1]

        if not ret:
            break

    cap.release()
    out.release()


if __name__ == "__main__":
    video_path = "data/raw/sample.mp4"
    tess_size = 16  # Tamaño de las teselas
    max_shift = 1  # Desplazamiento máximo de teselas
    quality_factor = 0.9  # Factor de calidad para considerar las teselas iguales
    gop_size = 10  # Tamaño del GOP
    output_path = "path/to/output/video.avi"

    main(video_path, tess_size, max_shift, quality_factor, gop_size, output_path)