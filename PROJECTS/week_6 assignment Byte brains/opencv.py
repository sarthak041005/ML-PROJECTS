import cv2
import numpy as np
import os

# -----------------------------
# Input and Output Folders
# -----------------------------
IMAGE_FOLDER = "images"
OUTPUT_FOLDER = "results"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# -----------------------------
# Process Each Image
# -----------------------------
for filename in os.listdir(IMAGE_FOLDER):

    image_path = os.path.join(IMAGE_FOLDER, filename)
    image = cv2.imread(image_path)

    if image is None:
        continue

    output = image.copy()

    # -----------------------------
    # Convert to Grayscale
    # -----------------------------
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # -----------------------------
    # Blur
    # -----------------------------
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # -----------------------------
    # Threshold
    # -----------------------------
    _, thresh = cv2.threshold(
        blur,
        0,
        255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    # -----------------------------
    # Morphological Operations
    # -----------------------------
    kernel = np.ones((3,3), np.uint8)

    thresh = cv2.morphologyEx(
        thresh,
        cv2.MORPH_OPEN,
        kernel,
        iterations=1
    )

    thresh = cv2.morphologyEx(
        thresh,
        cv2.MORPH_CLOSE,
        kernel,
        iterations=2
    )

    # -----------------------------
    # Find Contours
    # -----------------------------
    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    count = 0

    # -----------------------------
    # Draw Bounding Boxes
    # -----------------------------
    for contour in contours:

        area = cv2.contourArea(contour)

        if area > 200:

            x, y, w, h = cv2.boundingRect(contour)

            count += 1

            cv2.rectangle(
                output,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            cv2.putText(
                output,
                str(count),
                (x, y - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 0, 0),
                2
            )

    # -----------------------------
    # Display Total Count
    # -----------------------------
    cv2.putText(
        output,
        f"Total Objects: {count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    print(f"{filename} --> {count} objects detected")

    # Save Result
    cv2.imwrite(os.path.join(OUTPUT_FOLDER, filename), output)

    # Show Images
    cv2.imshow("Original", image)
    cv2.imshow("Threshold", thresh)
    cv2.imshow("Detected Objects", output)

    key = cv2.waitKey(500)  # Display each image for 0.5 seconds

    # Press ESC to stop
    if key == 27:
        break

cv2.destroyAllWindows()

print("Processing Completed!")