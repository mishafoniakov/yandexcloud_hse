from transformers import pipeline
from PIL import Image

class HuggingFaceDetector:
    def __init__(self, img: str):
        self.detector = pipeline(
            "image-segmentation",
            model="nvidia/segformer-b5-finetuned-ade-640-640"
        )
        self.classifier = pipeline(
            "image-classification",
            model="google/vit-base-patch16-224"
        )
        self.img = img
    
    def detect_oil(self):
        image = Image.open(self.img)
        segmentation = self.detector(image)
        
        oil_like_classes = ['water', 'sea', 'lake', 'river']
        
        results = []
        for segment in segmentation:
            if segment['label'] in oil_like_classes:
                anomaly_score = self.check_anomalies(segment['mask'])
                if anomaly_score > 0.5:
                    results.append({
                        'region': segment['mask'],
                        'score': anomaly_score,
                        'type': 'potential_oil_spill'
                    })
        
        return results