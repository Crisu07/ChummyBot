import discord
from discord.ext import commands
import youtube_dl

async def join(msg):
  if msg.author.voice is None: # If the user is not in a voice channel
    await msg.send("Baka you're not in a voice channel!")
  voice_channel = msg.author.voice.channel

  if msg.guild.voice_client is None: # If the bot is not in a voice channel, then connect
    await voice_channel.connect()
  else: # If the bot is already in a channel, move to the one the command was called in
    await msg.guild.voice_client.move_to(voice_channel)

async def disconnect(msg):
  await msg.guild.voice_client.disconnect()

async def play(msg):
  url = msg.content.split(' ')[1]
  vc = msg.guild.voice_client
  vc.stop()
  # Taken from Discord API \/
  FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
  YDL_OPTIONS = {'format' : "bestaudio"} # Ensures that bot is playing best audio possible for music
  
  # Video Streaming
  with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
    await msg.channel.send("Playing {} 🔊".format(url))
    info = ydl.extract_info(url, download=False)
    url2 = info['formats'][0]['url']
    source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
    vc.play(source)

# Continue Playing
async def resume(msg):
  await msg.channel.send('▶️ Resuming')
  msg.guild.voice_client.resume()

# Pause Audio
async def pause(msg):
  await msg.channel.send('⏸️ Paused')
  msg.guild.voice_client.pause()
