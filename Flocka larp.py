import discord
import getpass
import os

TOKEN = getpass.getpass("Paste your NEW bot token: ")

VC_ID = 1547412624348545144
SONG = "pupsies - Misery. (Lyrics).mp3"

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    channel = client.get_channel(VC_ID)

    if channel is None:
        print("ERROR: Voice channel not found.")
        await client.close()
        return

    if not isinstance(channel, discord.VoiceChannel):
        print("ERROR: That ID is not a normal voice channel.")
        await client.close()
        return

    if not os.path.exists(SONG):
        print(f"ERROR: Cannot find {SONG}")
        await client.close()
        return

    try:
        voice = await channel.connect()
        print(f"Joined: {channel.name}")

        while True:
            print("Playing song...")

            source = discord.FFmpegPCMAudio(SONG)
            voice.play(source)

            while voice.is_playing():
                await asyncio.sleep(1)

            print("Song finished — looping...")

    except Exception as e:
        print(f"ERROR: {e}")


import asyncio

client.run(TOKEN)