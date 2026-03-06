import os
from pathlib import Path
import uuid
import base64

import openai
import shutil
from dotenv import load_dotenv

load_dotenv()

from settings import YandexStudioAIOilAgent, Prompts

class YandexStudioGemma:
    def __init__(self, img_path):
        self.client = openai.OpenAI(
            api_key=os.getenv('YANDEX_CLOUD_API'),
            base_url=YandexStudioAIOilAgent.BASE_URL
        )
        self.img_path = img_path

    def image_to_base64(self, img_file):
        with open(img_file, "rb") as img:
            return base64.b64encode(img.read()).decode('utf-8')
    
    def __call__(self):
        img = self.image_to_base64(self.img_path)
        response = self.client.chat.completions.create(
            model=f"gpt://{YandexStudioAIOilAgent.FOLDER_ID}/gemma-3-27b-it",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"{Prompts.SHORT}"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{img}"
                            }
                        }
                    ]
                }
            ]
        )
        return response.choices[0].message.content