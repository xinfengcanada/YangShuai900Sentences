from PIL import Image
import pytesseract

img = Image.open(r'214.jpg')
text = pytesseract.image_to_string(img,lang='chi_sim+eng')
# text = pytesseract.image_to_string(img,lang='eng')
print(text)