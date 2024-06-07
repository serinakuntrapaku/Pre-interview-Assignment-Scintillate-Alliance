import pytesseract
import PIL.Image
import cv2

"""fdfasd"""
"""
Page segmentation modes:
0 Orientation and script detection (OSD) only.
1 Automation page segmentation with OSD.

2 Automation page segmentation, but no OSD, or OCR.
3 Fully automatic page segmentation, but no OSD.(Default)
4 Assume a single column of text of variable sizes.
5 Assume a single uniform block of text.
6 Treat the image as a single text line.
7 Treat the image as a single word.
8 Treat the image as a single word in acircle.
9 Treat the image as a single character.
10 Sparse text. Find as much text as possible in no particular order.
11 Sparse text with OSD.
12 Raw line. Treat the image as asingle text line,
                    bypassing hacks that are Tesseract-specific.
                    
"""

"""
OCR Engine Mode
0 Legacy engine only.
1 Neural nets LSTM engine only.
2 Legacy + LSTM engines.
3 Default, based on what is available.
"""
myconfig = r"--psm 11 --oem 3"
img = cv2.imread("firstbook.png")
print("name")
print("price")
print("rating")
cv2.imshow("img",img)
img = cv2.imread("secondbook.png")
print("name")
print("price")
print("rating")
cv2.imshow("img",img)

#text = pytesseract.image_to_string(PIL.Image.open("books.jpg"), config=myconfig)