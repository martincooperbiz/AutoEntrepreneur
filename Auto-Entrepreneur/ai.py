from __future__ import annotations

import logging
logger = logging.getLogger(__name__)
import openai


class AI:
    def __init__(self, model="text-davinci-002", temperature=0.5):
        self.model = model
        self.temperature = temperature

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