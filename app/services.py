import os
import openai
from dotenv import load_dotenv

load_dotenv()

from settings import YandexStudioAIOilAgent

class YandexStudioAIOilService:

    def __init__(self, message):
        self.client = openai.OpenAI(
            api_key=os.getenv('YANDEX_CLOUD_API'),
            base_url=YandexStudioAIOilAgent.BASE_URL,
            project=YandexStudioAIOilAgent.PROJECT
        )
        self.message = message
    
    def __call__(self):
        response = self.client.responses.create(
            prompt={
                "id": YandexStudioAIOilAgent.PROMPT,
            },
            input=self.message,
        )

        return response.output_text