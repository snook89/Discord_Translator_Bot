# Discord Translation Bot 🤖

A simple yet powerful Discord bot that translates messages to English (or other languages) using Google Translate.

## Features ✨

*   **Command Translation**: Reply to any message with `!translate` to translate it to English.
*   **Flag Reactions**: React to a message with a country flag to get a DM with the translation in that language.
    *   🇺🇸 🇬🇧 -> English
    *   🇺🇦 -> Ukrainian
    *   🇪🇸 -> Spanish
    *   🇫🇷 -> French
    *   🇩🇪 -> German
    *   🇮🇹 -> Italian
    *   🇯🇵 -> Japanese
    *   🇨🇳 -> Chinese (Simplified)
    *   🇷🇺 -> Russian
    *   🇵🇱 -> Polish

## Installation 🛠️

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/snook89/Discord_Translator_Bot.git
    cd Discord_Translator_Bot
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment**:
    *   Create a file named `.env` in the root directory.
    *   Add your Discord Bot Token:
        ```env
        DISCORD_TOKEN=your_discord_bot_token_here
        ```

4.  **Run the Bot**:
    ```bash
    python main.py
    ```

## Permissions 🔒

Make sure your bot has the following permissions in the Discord Developer Portal:
*   **Read Messages/View Channels**
*   **Send Messages**
*   **Add Reactions**
*   **Read Message History**
*   **Message Content Intent** (Under "Privileged Gateway Intents")

## Usage 📖

### Translate to English
*   **Reply** to a message with `!translate`.
*   **Type** `!translate <text>` to translate specific text.

### Translate to Specific Language
*   **React** to a message with one of the supported flags (e.g., 🇺🇦 for Ukrainian).
*   The bot will send you a **Direct Message (DM)** with the translation.

## Troubleshooting ❓

*   **No DM received?**: Check your server privacy settings to allow DMs from server members.
*   **Login Failure?**: Ensure your `.env` file has the correct **Token** (not Public Key or Client Secret).
