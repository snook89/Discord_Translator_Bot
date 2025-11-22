from deep_translator import GoogleTranslator

def test_translation():
    text = "Hola mundo"
    print(f"Testing translation for: {text}")
    
    try:
        translator = GoogleTranslator(source='auto', target='en')
        translation = translator.translate(text)
        print(f"Translation result: {translation}")
        
        if translation.lower() == "hello world":
            print("SUCCESS: Translation works as expected.")
        else:
            print(f"WARNING: Translation result '{translation}' differs from expected 'Hello World'.")
            
    except Exception as e:
        print(f"FAILURE: Error during translation: {e}")

if __name__ == "__main__":
    test_translation()
