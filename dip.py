# 1. Install OpenCV library
from google.colab import drive

drive.mount('/content/drive')

# 2. Load Image of Lena and display it in another screen
# 4.1
from google.colab.patches import cv2_imshow
import cv2

lena_image = cv2.imread('/content/drive/MyDrive/modi.jpg')
if lena_image is not None:
    cv2_imshow(lena_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Failed to load the image.')

# 3. Border around the image
import cv2
import numpy as np

# Load the image
image = cv2.imread('/content/drive/MyDrive/modi.jpg')
border_size = 5
border_color = (0, 24, 255)
bordered_image = cv2.copyMakeBorder(image, border_size, border_size,
                                    border_size, border_size, cv2.BORDER_CONSTANT, value=border_color)
cv2_imshow(bordered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 4. Blending Pepsi logo over the Lena image
import cv2
import numpy as np
from PIL import Image

# Load Lena image
lena_image = cv2.imread('/content/drive/MyDrive/modi.jpg')

# Load and resize Pepsi logo
pepsi_logo = Image.open('/content/drive/MyDrive/india.png')
pepsi_logo = pepsi_logo.resize((lena_image.shape[1], lena_image.shape[0]))
pepsi_logo = np.array(pepsi_logo)

# Check if the sizes match
if lena_image.shape[:2] == pepsi_logo.shape[:2]:
    # Convert Pepsi logo to BGR (3 channels) if it's in grayscale
    if len(pepsi_logo.shape) == 2:
        pepsi_logo = cv2.cvtColor(pepsi_logo, cv2.COLOR_GRAY2BGR)

    alpha = 0.2
    blended_image = cv2.addWeighted(lena_image, 1 - alpha, pepsi_logo, alpha, 0)
    cv2_imshow(blended_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Image sizes do not match for blending.')


# 5. Using bitwise AND, OR, and NOT operators, paste the image of Pepsi on Lena's image.
# The background of the Pepsi logo should not be pasted over, but only ROI will be pasted
import cv2

lena_image = cv2.imread('/content/drive/MyDrive/modi.jpg')
pepsi_logo = cv2.imread('/content/drive/MyDrive/india.png')
x_pos = 100
y_pos = 100
logo_height, logo_width, _ = pepsi_logo.shape

# Create a region of interest (ROI) in the Lena image
roi = lena_image[y_pos:y_pos + logo_height, x_pos:x_pos + logo_width]

# Resize the Pepsi logo image to match the dimensions of the ROI
resized_pepsi_logo = cv2.resize(pepsi_logo, (roi.shape[1], roi.shape[0]))

# Blend the images without transparency
blended_image = cv2.addWeighted(roi, 1, resized_pepsi_logo, 0.5, 0)

# Paste the result back into the Lena image
lena_image[y_pos:y_pos + logo_height, x_pos:x_pos + logo_width] = blended_image

cv2_imshow(lena_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 6. Olympic circle using OpenCV
import cv2
import numpy as np

canvas = np.ones((400, 600, 3), dtype=np.uint8) * 255
radius = 60
thickness = 10
circle_centers = [(150, 150), (300, 150), (450, 150), (225, 210), (375, 210)]
circle_colors = [(255, 0, 0), (0, 255, 255), (0, 0, 0), (0, 128, 0), (0, 0, 255)]

for center, color in zip(circle_centers, circle_colors):
    cv2.circle(canvas, center, radius, color, thickness)

cv2_imshow(canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 1. Resize to twice the original image size
import cv2

original_image = cv2.imread("/content/drive/MyDrive/modi.jpg")
original_height, original_width = original_image.shape[:2]
resized_image = cv2.resize(original_image, (2 * original_width, 2 * original_height))
cv2.imwrite("modi.jpg", resized_image)

# 2. Translate 30 pixels horizontally and 50 pixels vertically
import cv2
import numpy as np

original_image = cv2.imread("/content/drive/MyDrive/modi.jpg")

# Define the translation matrix
translation_matrix = np.float32([[1, 0, 30], [0, 1, 50]])

# Apply the translation to the original image
translated_image = cv2.warpAffine(original_image, translation_matrix, (original_image.shape[1], original_image.shape[0]))
cv2.imwrite("translated_image.jpg", translated_image)

# 3. Rotate image by 45 degrees clockwise
import cv2

original_image = cv2.imread("/content/drive/MyDrive/modi.jpg")
center = (original_image.shape[1] / 2, original_image.shape[0] / 2)
rotation_angle = -45

# Rotation
rotation_matrix = cv2.getRotationMatrix2D(center, rotation_angle, 1.0)
rotated_image = cv2.warpAffine(original_image, rotation_matrix, (original_image.shape[1], original_image.shape[0]))
cv2.imwrite("rotated_image.jpg", rotated_image)

# 4. Different types of thresholding
import cv2

image = cv2.imread("/content/drive/MyDrive/modi.jpg", cv2.IMREAD_GRAYSCALE)
threshold_value = 128

# Apply different thresholding methods
_, binary_threshold = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
_, binary_inv_threshold = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY_INV)
_, trunc_threshold = cv2.threshold(image, threshold_value, 255, cv2.THRESH_TRUNC)
_, tozero_threshold = cv2.threshold(image, threshold_value, 255, cv2.THRESH_TOZERO)
_, tozero_inv_threshold = cv2.threshold(image, threshold_value, 255, cv2.THRESH_TOZERO_INV)

# Save the thresholded images
cv2.imwrite("binary_threshold.jpg", binary_threshold)
cv2.imwrite("binary_inv_threshold.jpg", binary_inv_threshold)
cv2.imwrite("trunc_threshold.jpg", trunc_threshold)
cv2.imwrite("tozero_threshold.jpg", tozero_threshold)
cv2.imwrite("tozero_inv_threshold.jpg", tozero_inv_threshold)

# 5. Adaptive thresholding and Otsu’s binarization.
import cv2

image = cv2.imread("/content/drive/MyDrive/modi.jpg", cv2.IMREAD_GRAYSCALE)

# Adaptive Thresholding
adaptive_threshold = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Otsu's Binarization
_, otsu_threshold = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imwrite("adaptive_threshold.jpg", adaptive_threshold)
cv2.imwrite("otsu_threshold.jpg", otsu_threshold)

# 6. Gaussian, median and average filter
import cv2

image = cv2.imread("/content/drive/MyDrive/modi.jpg")

# Apply Gaussian Blur

blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Median filter
median_filtered = cv2.medianBlur(image, 5)

# Average filter
average_filtered = cv2.blur(image, (5, 5))

cv2_imshow(blurred_image)
cv2_imshow(median_filtered)
cv2_imshow(average_filtered)

cv2.waitKey(0)
cv2.destroyAllWindows()
