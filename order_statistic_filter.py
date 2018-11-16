import cv2


def median_filter(image):
    median_image = image.copy()
    height = image.shape[0]
    width = image.shape[1]
    for row in range(height):
        for col in range(width):
            pixel = get_neighbors(row, col, width, height, image)
            pixel.sort()
            median_image[row, col] = pixel[4]

    return median_image


def max_filter(image):
    max_image = image.copy()
    height = image.shape[0]
    width = image.shape[1]
    for row in range(height):
        for col in range(width):
            pixel = get_neighbors(row, col, width, height, image)
            max_image[row, col] = max(pixel)

    return max_image


def min_filter(image):
    median_image = image.copy()
    height = image.shape[0]
    width = image.shape[1]
    for row in range(height):
        for col in range(width):
            pixel = get_neighbors(row, col, width, height, image)
            median_image[row, col] = min(pixel)

    return median_image




def get_neighbors(row, col, width, height, img):
    left = max(0, col - 1)
    up = max(0, row - 1)
    right = min(width - 1, col + 1)
    down = min(height - 1, row + 1)
    pixel = [img[up][left], img[up][col],
             img[up][right], img[row][right],
             img[row][left], img[down][left],
             img[down][col], img[down][right]]
    return pixel


image = cv2.imread("gaussian.png", 0)
restored_image = min_filter(image)
cv2.imshow("asd", restored_image)
cv2.waitKey(0)