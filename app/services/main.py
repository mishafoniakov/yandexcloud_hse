from services import YandexStudioAIOilService, YandexStudioGemma
from services.hugging import HuggingFaceDetector
from technics import upload_file

class MultiSystem:

    def __init__(self, img):
        self.img = img
    
    def __call__(self):
        img_path = upload_file(self.img)
        #detect = HuggingFaceDetector(img_path)
        #print(detect.detect_oil())
        model = YandexStudioGemma(img_path)
        text = model()
        agent = YandexStudioAIOilService(text)
        result = agent()
        return result