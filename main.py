import os
import discord
from discord.ext import commands
from deep_translator import GoogleTranslator
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Flag to Language mapping
FLAG_TO_LANG = {
    '🇺🇸': 'en', '🇺🇸': 'en', '🇬🇧': 'en',
    '🇺🇦': 'uk',
    '🇪🇸': 'es',
    '🇫🇷': 'fr',
    '🇩🇪': 'de',
    '🇮🇹': 'it',
    '🇯🇵': 'ja',
    '🇨🇳': 'zh-CN',
    '🇷🇺': 'ru',
    '🇵🇱': 'pl',
}

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True # Enable reaction events
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_raw_reaction_add(payload):
    # Ignore bot's own reactions
    if payload.user_id == bot.user.id:
        return

    emoji = str(payload.emoji)
    
    # Check if the emoji is in our supported flags
    if emoji in FLAG_TO_LANG:
        target_lang = FLAG_TO_LANG[emoji]
        
        try:
            channel = await bot.fetch_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            content = message.content

            if not content:
                return

            # Get the user who reacted
            user = await bot.fetch_user(payload.user_id)
            
            print(f"Translating message for {user.name} to {target_lang}")

            translator = GoogleTranslator(source='auto', target=target_lang)
            translation = translator.translate(content)
            
            embed = discord.Embed(title="Translation", color=0x00ff00)
            embed.add_field(name="Original", value=content[:1024], inline=False)
            embed.add_field(name=f"Translation ({target_lang})", value=translation[:1024], inline=False)
            embed.set_footer(text=f"Requested by {user.display_name} via reaction")
            
            # Send DM to the user who reacted
            await user.send(embed=embed)
            print(f"Sent DM to {user.name}")
            
        except discord.Forbidden:
            print(f"Could not send DM to user {payload.user_id} (DMs likely closed)")
        except Exception as e:
            print(f"Error translating reaction: {e}")

@bot.command(name='translate')
async def translate_msg(ctx, *, text=None):
    """
    Translates the referenced message or the provided text to English.
    Usage:
    1. Reply to a message with !translate
    2. !translate <text to translate>
    """
    target_text = text
    
    # If the command is used as a reply, use the replied message's content
    if ctx.message.reference:
        original_message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        if not target_text:
            target_text = original_message.content

    if not target_text:
        await ctx.send("Please provide text to translate or reply to a message.")
        return

    try:
        # Translate to English
        translator = GoogleTranslator(source='auto', target='en')
        translation = translator.translate(target_text)
        
        embed = discord.Embed(title="Translation", color=0x00ff00)
        embed.add_field(name="Original", value=target_text[:1024], inline=False)
        embed.add_field(name="English", value=translation[:1024], inline=False)
        embed.set_footer(text=f"Requested by {ctx.author.display_name}")
        
        await ctx.send(embed=embed)
        
    except Exception as e:
        await ctx.send(f"An error occurred during translation: {str(e)}")

if __name__ == "__main__":
    if not TOKEN or TOKEN == "YOUR_TOKEN_HERE":
        print("Error: DISCORD_TOKEN is not set in .env file.")
    else:
        bot.run(TOKEN)
