import cv2
import imutils
import numpy as np

road_img = cv2.imread("road2.jpg")
road_img = imutils.resize(road_img, height=1280, width=1080)
gray_img = cv2.cvtColor(road_img, cv2.COLOR_BGR2GRAY)
blur_road_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

edges = cv2.Canny(blur_road_img, 50, 150)

imshape = road_img.shape
vertices = np.array([[(0, imshape[0]), (450, 320), (500, 320), (imshape[1], imshape[0])]], dtype=np.int32)
mask = np.zeros_like(edges)
ignore_mask_color = 255
cv2.fillPoly(mask, vertices, ignore_mask_color)
masked_edges = cv2.bitwise_and(gray_img, mask)

rho = 3
theta = np.pi / 180
threshold = 15
min_line_length = 40  # minimum number of pixels making up a line
max_line_gap = 30  # maximum gap in pixels between connectable line segments
lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]), minLineLength=min_line_length,
                        maxLineGap=max_line_gap)


def draw_lines(img, lines, color=[255, 0, 0], thickness=7):
    line_image = np.copy(img) * 0  # creating a blank to draw lines on

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)

    # Create a "color" binary image to combine with line image
    # color_edges = np.dstack((edges, edges, edges))

    # Draw the lines on the original image
    lines_edges = cv2.addWeighted(img, 0.8, line_image, 1, 0)
    return lines_edges


draw_lines(road_img, lines)
cv2.imshow("Road img", road_img)
cv2.imshow("Road", masked_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
