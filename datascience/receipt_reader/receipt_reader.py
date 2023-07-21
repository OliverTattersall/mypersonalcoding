import numpy as np
import cv2
import matplotlib.pyplot as plt
import pytesseract
import re

from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def plot_gray(image):
    plt.figure(figsize=(16,10))
    return plt.imshow(image, cmap='Greys_r')

def plot_rgb(image):
    plt.figure(figsize=(16,10))
    return plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

def find_amounts(text):
    amounts = re.findall(r'\d+\.\d{2}\b', text)
    floats = [float(amount) for amount in amounts]
    unique = list(set(floats))
    return unique

def get_value(file_name):
    # file_name = "result.png"
    image = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE) 
    # plot_gray(image)
    ret,thresh = cv2.threshold(image, 70 ,255, 0)
    

    # d = pytesseract.image_to_data(thresh, output_type=Output.DICT)
    # # print(d)
    # n_boxes = len(d['level'])
    # boxes = cv2.cvtColor(thresh.copy(), cv2.COLOR_BGR2RGB)
    # for i in range(n_boxes):
    #     (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])    
    #     boxes = cv2.rectangle(boxes, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
    # plot_rgb(boxes)
    # plt.show()

    extracted_text = pytesseract.image_to_string(thresh).replace(' ', '')
    # pytesseract.im
    
    extracted_text2 = pytesseract.image_to_string(image).replace(' ', '')
    # print(extracted_text)

    # print(extracted_text.replace(' ', ''))

    amounts = find_amounts(extracted_text)
    # amounts = []
    amounts2 = find_amounts(extracted_text2)
    # amounts2 = []
    # amounts.append(amounts2)
    # print(amounts)
    return amounts + amounts2

# plt.show()

if __name__ == '__main__':
    # print(get_value(r'receipts\test_receipt1.jpg'))
    print(get_value(r'receipts\test_receipt2.jpg'))
    # print(get_value(r'receipts\test_receipt3.jpg'))