from openai import OpenAI

class TranslationService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = OpenAI(api_key=self.api_key)
        # openai.api_key = self.api_key

    def translate_text(self, text, target_language='English'):
        """
        Translate the provided text into the specified language using the ChatGPT-4 API.

        :param text: Text to translate
        :param target_language: Language to translate the text into (default is English)
        :return: Translated text
        """
        prompt = f"Translate the following text to {target_language} and provide only the translated text: \"{text}\""
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that translates text."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=1000,
            temperature=0.5,
        )
        
        translation = response.choices[0].message.content.strip()
        return translation

