import asyncio
from unittest.mock import AsyncMock, MagicMock
from deep_translator import GoogleTranslator

# Mocking Discord objects to test logic without connecting
class MockUser:
    def __init__(self, bot=False):
        self.bot = bot
        self.display_name = "TestUser"
        self.name = "TestUser"
        self.send = AsyncMock()

class MockMessage:
    def __init__(self, content):
        self.content = content

class MockReaction:
    def __init__(self, emoji, message):
        self.emoji = emoji
        self.message = message

FLAG_TO_LANG = {
    '🇺🇦': 'uk',
    '🇺🇸': 'en'
}

async def test_reaction_logic():
    print("Testing reaction logic...")
    
    # Test Case 1: Translate to Ukrainian
    user = MockUser()
    message = MockMessage("Hello world")
    reaction = MockReaction('🇺🇦', message)
    
    if reaction.emoji in FLAG_TO_LANG:
        target_lang = FLAG_TO_LANG[reaction.emoji]
        print(f"Detected flag {reaction.emoji}, translating to {target_lang}...")
        
        translator = GoogleTranslator(source='auto', target=target_lang)
        translation = translator.translate(message.content)
        
        print(f"Original: {message.content}")
        print(f"Translation: {translation}")
        
        if translation:
            print("SUCCESS: Translation occurred.")
        else:
            print("FAILURE: No translation returned.")
            
    # Test Case 2: Ignore unknown flag
    reaction_unknown = MockReaction('👽', message)
    if reaction_unknown.emoji not in FLAG_TO_LANG:
        print("SUCCESS: Ignored unknown flag 👽")
    else:
        print("FAILURE: Did not ignore unknown flag.")

if __name__ == "__main__":
    asyncio.run(test_reaction_logic())
