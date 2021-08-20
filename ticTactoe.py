import discord
import random 


async def play_tic(msg, client):
  blank = '⬜'
  #emojis that represent the spaces that are available and a quit button
  emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🛑']

  #game board
  board = [blank, blank, blank,
           blank, blank, blank,
           blank, blank, blank,]
  characters = ['❎', '🅾️']

  await msg.channel.purge(limit=1)
  #asks player for their choice of character, X or O
  embed = discord.Embed(
    title = 'Choose your charcter for Tic Tac Toe!',
    decription = '❎ or 🅾️',
    color = 0xFABFB2
  )
  mes = await msg.channel.send(embed = embed)
  await mes.add_reaction('❎')
  await mes.add_reaction('🅾️')
  player = await get_char(msg, client)

  #bot is assigned left over character
  characters.remove(player)
  bot = characters[0]
  await msg.channel.purge(limit=1)
  embed = discord.Embed(
    title = 'Your character will be: ' + player + '\nChummy will be: ' + bot,
    color = 0xFABFB2
  )
  await msg.channel.send(embed = embed)

  #randomly selects who will go first, player or cpu
  num = random.randint(1,2)
  turn = ''
  if num == 1:
    turn = 'player'
  else:
    turn = 'bot'
  await player_turn(msg, board, emojis, client, player)
  await msg.channel.purge(limit=1)
  await print_board(msg, board, emojis)

#function to wait for reaction response
async def get_char(msg, client):
  def check_reaction( reaction, user):
    return user == msg.author
    
  reaction, user = await client.wait_for("reaction_add", timeout = 30.0, check = check_reaction)
  return str(reaction.emoji)

#function to print out game board
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

#function for when it is the player's turn 
async def player_turn(msg, board, emojis, client, player):
  await msg.channel.send('Choose a position to place your character:')
  await print_board(msg, board, emojis)
  move = await get_char(msg, client)
  emojis.remove(move)
  if move== '1️⃣':
    board[0] = player
  elif move == '2️⃣':
    board[1] = player
  elif move ==  '3️⃣':
    board[2] = player
  elif move ==  '4️⃣':
    board[3] = player
  elif move ==  '5️⃣':
    board[4] = player
  elif move ==  '6️⃣':
    board[5] = player
  elif move ==  '7️⃣':
    board[6] = player
  elif move ==  '8️⃣':
    board[7] = player
  elif move ==  '9️⃣':
    board[8] = player
  elif move ==  '🛑':
    pass

#async def check_win(board, player, bot):
  