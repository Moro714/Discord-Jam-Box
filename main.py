import os
import logging
from dotenv import load_dotenv
from core.bot import MusicJamBot
# No need to import cogs directly here, bot.py handles it

# You can remove these lines after testing
# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Configure logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
logging.basicConfig(level=logging.INFO, handlers=[handler], format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

async def main():
    """Initializes and runs the bot."""
    bot = MusicJamBot()
    # setup_hook in bot.py will handle db init and cog loading
    await bot.start(TOKEN)

if __name__ == "__main__":
    import asyncio
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot shutting down due to keyboard interruption.")
    except Exception as e:
        logging.error(f"An error occurred during bot startup: {e}", exc_info=True)