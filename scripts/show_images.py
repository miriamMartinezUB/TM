import cv2


def show_images(image_path_files, fps):
    for image_path in image_path_files:
        img = cv2.imread(image_path)
        cv2.imshow(image_path, img)
        if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()