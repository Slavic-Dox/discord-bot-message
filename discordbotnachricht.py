import discord
from discord.ext import commands

# Token deines Discord-Bots
TOKEN = 'YourToken'

# Der gewünschte Channel-ID, in den die Nachricht geschickt werden soll
ZIEL_CHANNEL_ID = 1234567890 # Ersetze dies durch die tatsächliche Channel-ID

# Initialisierung des Bots
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Event, das beim Start des Bots aufgerufen wird
@bot.event
async def on_ready():
    print(f'Eingeloggt als {bot.user.name}')

    # Channel-Objekt für den Ziel-Channel abrufen
    target_channel = bot.get_channel(ZIEL_CHANNEL_ID)

    # Nachricht senden
    if target_channel:
        await target_channel.send('Hello World :) @everyone')

# Den Bot starten
bot.run(TOKEN)
