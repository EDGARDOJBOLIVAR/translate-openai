import argparse
from services.translation_service import TranslationService
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def main():
    parser = argparse.ArgumentParser(description='Translate text using the ChatGPT-4 API')
    parser.add_argument('text', type=str, help='Text to translate')
    parser.add_argument('--lang', type=str, default='English', help='Language to translate the text into (default is English)')
    parser.add_argument('--output_file', type=str, default='', help='File to save the translated text')

    args = parser.parse_args()
    
    original_text = args.text
    target_language = args.lang
    output_file = args.output_file

    # Initialize the translation service
    api_key = os.getenv('OPENAI_API_KEY')
    translation_service = TranslationService(api_key)

    translated_text = translation_service.translate_text(original_text, target_language)
    
    if output_file:
        with open(output_file, 'w') as file:
            file.write(translated_text)
        print(f"Original text: {original_text}")
        print(f"Translated text: {translated_text}")
        print(f"Translation saved in: {output_file}")
    else:
        print(f"Original text: {original_text}")
        print(f"Translated text: {translated_text}")

if __name__ == "__main__":
    main()
