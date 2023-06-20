import openai
import logging
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()

logger = logging.getLogger(__name__)




class AI:
    def __init__(self, model=None, temperature=0.5):
        self.model = model or os.getenv("MODEL")
        self.temperature = temperature
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def generate(self, prompt):
        try: 
            response = openai.Completion.create(
                engine=self.model,
                prompt=prompt,
                temperature=self.temperature
            )
            return response.choices[0].text.strip()
        except Exception as e:
            logger.error(f"Error generating AI response: {e}")
            return None
    def generate_business_plan(self, prompt):
        try: 
            plan = self.generate(prompt)
            return Document("Business Plan", plan, "AI")
        except Exception as e:
            logger.error(f"Error generating AI response for the business plan: {e}")
            return None