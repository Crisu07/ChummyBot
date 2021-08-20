import discord
import youtube_dl

# Taken from Discord API \/
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
YDL_OPTIONS = {'format' : "bestaudio", 'noplaylist': 'True'} # Ensures that bot is playing best audio possible for music
music_queue = [] # Music Queue List
is_playing = False

async def join(msg):
  if is_playing: return
  music_queue.clear()
  if msg.author.voice is None: # If the user is not in a voice channel
    await msg.send("Baka you're not in a voice channel!")
  voice_channel = msg.author.voice.channel

  if msg.guild.voice_client is None: # If the bot is not in a voice channel, then connect
    await voice_channel.connect()
  else: # If the bot is already in a channel, move to the one the command was called in
    await msg.guild.voice_client.move_to(voice_channel)

async def disconnect(msg):
  is_playing = False
  music_queue.clear() # Clears music queue upon leaving
  await msg.guild.voice_client.disconnect()

async def play(msg, url=None):
  global is_playing

  # If the URL is None, that means there is no search result, so the URL is retrieved from the message content (pasted).
  if url == None: url = " ".join(msg.content.split(' ')[1:])
  vc = msg.guild.voice_client
  search = " ".join(msg.content.split(' ')[1:])

  if not is_playing:
    vc.stop() # If Music already playing, stop it and play the next
    # Video Streaming
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      await msg.channel.send("Playing {} 🔊".format(search))
      info = ydl.extract_info(url, download=False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
      # https://stackoverflow.com/a/66330279
      vc.play(source, after=lambda x: (await play_next(msg) for _ in '_').__anext__())
    is_playing = True
  else: # Adding the video to the queue instead.
    music_queue.append(url)

# Continue Playing
async def resume(msg):
  msg.guild.voice_client.resume()
  await msg.channel.send('▶️ Resuming')

# Pause Audio
async def pause(msg):
  msg.guild.voice_client.pause()
  await msg.channel.send('⏸️ Paused')

# Searching Music
async def search(msg):
  await join(msg)
  with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
    try:
      search = " ".join(msg.content.split(' ')[1:])
      query = "ytsearch:{}".format(search)
      info = ydl.extract_info(query, download=False)['entries'][0]
      url = info['formats'][0]['url']
      await play(msg, url)
      await msg.channel.send("Adding searched video to queue.")
    except Exception:
      await msg.channel.send("Adding URL to queue.")
      return await play(msg)

# Play Next in the Queue (Helper function)
async def play_next(msg):
  global is_playing
  if len(music_queue) > 0:
    music_queue.pop(0) # remove oldest url from music_queue
    url = music_queue[0] # get next url
    queue_message = ", ".join(music_queue)
    await msg.channel.send(queue_message)
    return await play(msg, url)
  is_playing = False

# Skip to next in queue
async def skip(msg):
  msg.guild.voice_client.stop() # If Music already playing, stop it and play the next
  return await play_next(msg)
