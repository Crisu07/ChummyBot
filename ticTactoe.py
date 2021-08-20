import discord
import random 


async def play_tic(msg, client):
  blank = '⬜'
  emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🛑']
  board = [blank, blank, blank,
           blank, blank, blank,
           blank, blank, blank,]
  characters = ['❎', '🅾️']

  await msg.channel.purge(limit=1)

  embed = discord.Embed(
    title = 'Choose your charcter for Tic Tac Toe!',
    decription = '❎ or 🅾️',
    color = 0xFABFB2
  )
  mes = await msg.channel.send(embed = embed)
  await mes.add_reaction('❎')
  await mes.add_reaction('🅾️')
  player = await get_char(msg, client)
  characters.remove(player)
  bot = characters[0]

  await msg.channel.purge(limit=1)
  embed = discord.Embed(
    title = 'Your character will be: ' + player + '\nChummy will be: ' + bot,
    color = 0xFABFB2
  )
  await msg.channel.send(embed = embed)

  num = random.randint(1,2)
  turn = ''
  if num == 1:
    turn = 'player'
  else:
    turn = 'bot'
  await player_turn(msg, board, emojis)
  
async def get_char(msg, client):
  def check_reaction( reaction, user):
    return user == msg.author
    
  reaction, user = await client.wait_for("reaction_add", timeout = 30.0, check = check_reaction)
  return str(reaction.emoji)

async def print_board(msg,board, emojis):
  line  = ''
  for i in range(len(board)):
    if (i + 1) % 3 == 0:
      line += board[i] + '\n'
    else:
      line += board[i]
  embed = discord.Embed(
    title = line,
    color = 0xFABFB2
  )
  mes = await msg.channel.send(embed = embed)
  for i in emojis:
    await mes.add_reaction(i)

async def player_turn(msg, board, emojis):
  await msg.channel.send('Choose a position to place your character:')
  await print_board(msg, board, emojis)
  
  