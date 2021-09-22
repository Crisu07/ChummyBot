import discord
import youtube_dl

from youtube_dl import YoutubeDL

class musicplayer():
  def __init__(self):
    # (From Discord API) Ensures that bot is playing best audio available 
    self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    
    self.is_playing = False # Tracker to see if bot is currently playing music or not
    self.music_queue = [] # Music Queue list

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
    #checks if message has a url 
    vc = msg.guild.voice_client
    vc.stop() # stops current song to play the next (queue not available yet)
    if "https://" in msg.content:
      url = msg.content.split(' ')[1]
      # vc.stop() # If Music already playing, stop it and play the next
      # Video Streaming
      with youtube_dl.YoutubeDL(self.YDL_OPTIONS) as ydl:
        # Gets information about the video source
        info = ydl.extract_info(url, download=False)
        url = info['formats'][0]['url'] # Video URL 

    else: # If message does not contain a url
      url = await self.search(msg)

    searchresult = " ".join(msg.content.split(' ')[1:])
    await msg.channel.send("Playing {} 🔊".format(searchresult))
    # Playing the audio
    source = await discord.FFmpegOpusAudio.from_probe(url, **self.FFMPEG_OPTIONS)
    vc.play(source)
    # Add Music to queue
    #'title' = info['title']

  # Youtube Search Feature
  async def search(self, msg):
    with YoutubeDL(self.YDL_OPTIONS) as ydl:
      try: 
        # Searches first video entry 
        search = " ".join(msg.content.split(' ')[1:])
        query = "ytsearch:{}".format(search)
        info = ydl.extract_info(query, download=False)['entries'][0]
        # info = ydl.extract_info("ytsearch:%s" % msg, download=False)['entries'][0]
      except Exception: 
          await msg.channel.send("Could not find track. Try a different keyword. 😔")
          return False

    url2 = info['formats'][0]['url']
    return url2

  """# Check if there is no infinite loop on the music
  async def play_music(self):
      if len(self.music_queue) > 0:
          self.is_playing = True
          url1 = self.music_queue[0][0]['source']
          
          # Connects to channel if not already connected (Should be fixed/debugged with joined)
          if self.voicecheck == "" or not self.voicecheck.is_connected() or self.voicecheck == None:
              self.voicecheck = await self.music_queue[0][1].connect()
          else:
              await self.voicecheck.move_to(self.music_queue[0][1])
          
          print(self.music_queue)
          self.music_queue.pop(0)

          self.voicecheck.play(discord.FFmpegPCMAudio(url1, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
      else:
          self.is_playing = False

  # Check queue list of songs
  async def queue(self, msg):
      retrieval = ""
      for i in range(0, len(self.music_queue)):
          retrieval += self.music_queue[i][0]['title'] + "\n"

      print(retrieval) # Test command
      if retrieval != "":
          await msg.channel.send(retrieval)
      else:
          await msg.channel.send("There is currently no tracks in queue. 🗑️")

  # Skip Song in Track
  async def skip(self, msg):
      if self.voicecheck != "" and self.voicecheck:
          self.voicecheck.stop()
          
          # Plays next track if applicable
          await self.play_music()

  # Play next track in queue
  async def play_next(self):
      if len(self.music_queue) > 0: # If the music queue is not empty
          self.is_playing = True
          url1 = self.music_queue[0][0]['source'] # Get the URl source
          self.music_queue.pop(0) # Remove the song from queue as bot is currently playing it
          self.voicecheck.play(discord.FFmpegPCMAudio(url1, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
      else:
          self.is_playing = False"""

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