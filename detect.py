import cv2
import os
import uuid

def detect_people(image_path, output_dir='static/results'):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Could not read the image!")

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    (rects, _) = hog.detectMultiScale(image, winStride=(4, 4),
                                      padding=(8, 8), scale=1.05)

    for (x, y, w, h) in rects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    filename = f"detected_{uuid.uuid4().hex[:8]}.jpg"
    output_path = os.path.join(output_dir, filename)
    cv2.imwrite(output_path, image)

    return output_path
