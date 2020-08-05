
from PIL import Image
import pytesseract 
import os.path
# from utils.config import Config

script_dir = os.path.dirname(os.path.abspath(__file__))
Image = Image.open(os.path.join(script_dir, 'ocr_test.jpg'))   # 打开图片

# c = Config()
# screenshot_path = c.screen_shot_path()
# Image = Image.open(screenshot_path + "vantpy2.0.jpg")


text = pytesseract.image_to_string(Image,lang='chi_sim')  #使用简体中文解析图片
print(text)