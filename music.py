import discord
import youtube_dl

class musicplayer():
  def __init__(self):
    # (From Discord API) Ensures that bot is playing best audio available 
    self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    

  async def join(self, msg):
    if msg.author.voice is None: # If user is not in a voice channel then notify them 
        await msg.channel.send("Baka {}! You're not in a voice channel!".format(msg.author.mention))
    voice_channel = msg.author.voice.channel

    if msg.guild.voice_client is None: # If the bot is not already in a voice channel, connect
        await voice_channel.connect()
        await msg.channel.send("Connected to a voice channel! ✅")

    else: # If the bot is already connected to a different voice channel, move to the one the command was called in
        await msg.guild.voice_client.move_to(voice_channel)
        await msg.channel.send("Moved to a different voice channel! ✅")

  # Play Music
  async def play(self, msg):
    url = msg.content.split(' ')[1]
    vc = msg.guild.voice_client
    vc.stop() # If Music already playing, stop it and play the next

    # Video Streaming
    with youtube_dl.YoutubeDL(self.YDL_OPTIONS) as ydl:
      await msg.channel.send("Playing {} 🔊".format(url))
      info = ydl.extract_info(url, download=False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2, **self.FFMPEG_OPTIONS)
      vc.play(source)

  # Continue Playing
  async def resume(self, msg):
    msg.guild.voice_client.resume()
    await msg.channel.send('▶️ Resuming')

  # Pause Audio
  async def pause(self, msg):
    msg.guild.voice_client.pause()
    await msg.channel.send('⏸️ Paused')

  # Disconnect from Voice
  async def disconnect(self, msg):
    await msg.guild.voice_client.disconnect()
    await msg.channel.send('🔇 Disconnected')