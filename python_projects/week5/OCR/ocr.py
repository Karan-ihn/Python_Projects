import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\HP\\Appdata\\local\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('ocr sample 2.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

cv2.imshow('result',img)
cv2.waitKey(0)
data = pytesseract.image_to_string(img)
with open('ocr_to_text.txt','w',newline='') as o:
    o.write(data)
    o.close()
