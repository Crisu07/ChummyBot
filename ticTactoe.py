import discord
import random 

async def game_options(msg, client):
  embed = discord.Embed(
    title = "Game Options",
    description = "1. TicTacToe (with a friend) \n 2. TicTacToe (with me)"
  )
  #await msg.channel.purge(limit=1)
  mes = await msg.channel.send(embed= embed)
  await mes.add_reaction('1️⃣')
  await mes.add_reaction('2️⃣')
  react = await get_char(msg, client)

  if str(reaction.emoji)
  
async def play_tic(msg, client):
  blank = '⬜'
  #emojis that represent the spaces that are available and a quit button
  emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🛑']
  #game board
  board = [blank, blank, blank,
           blank, blank, blank,
           blank, blank, blank,]
  characters = ['❎', '🅾️']

  await msg.channel.purge(limit=1) # Deletes message after reacting to avoid spam
  #asks player for their choice of character, X or O
  embed = discord.Embed(
    title = 'Choose your charcter for Tic Tac Toe!',
    decription = '(Timeout time for reaction responses is 30 seconds)',
    color = 0xFABFB2
  )
  mes = await msg.channel.send(embed = embed)
  await mes.add_reaction('❎')
  await mes.add_reaction('🅾️')
  player = await get_char(msg, client)
  characters.remove(player)
  bot = characters[0]
  
  #recaps who's what character 
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

  #initialize winner to being none
  winner = 'none'
  await player_turn(msg, board, emojis, client, player)
  while winner == 'none':
    await msg.channel.purge(limit=2)
    winner = await check_win(board, player, bot)
    if winner != 'none':
      break
    await player_turn(msg, board, emojis, client, player)
  await msg.channel.send('Winner!' + winner)


  
  #To Do: inform command  time out #function to wait for reaction response
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
  mes = await msg.channel.send(line)
  for i in emojis:
    await mes.add_reaction(i)


#function for when it is the player's turn 
async def player_turn(msg, board, emojis, client, player):
  await msg.channel.send('Choose a position to place your character:')
  await print_board(msg, board, emojis)
  move = await get_char(msg, client)
  emojis.remove(move)
  if move == '1️⃣':
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
  elif move == '🛑':
    pass

# Check who won
async def check_win(board, player, bot):
  winner = 'none'
  #checking horizontal
  if (board[0] == board[1] == board[2]):
    winner = board[0]
  elif (board[3] == board[4] == board[5]):
    winner = board[3]
  elif (board[6] == board[7] == board[8]):
    winner = board[3]
  
  #checking vertical 
  if (board[0] == board[3] == board[6]):
    winner = board[0]
  elif (board[1] == board[4] == board[7]):
    winner = board[1]
  elif (board[2] == board[5] == board[8]):
    winner = board[2]
  
  #checking diagonal
  if (board[0] == board[4] == board[8]):
    winner = board[0]
  elif (board[2] == board[4] == board[6]):
    winner = board[2]

  if winner != player and winner != bot:
    winner = 'none'
  return winner

async def bot_turn(msg, board, emojis, client, bot):
  for chara in ['❎', '🅾️']:
    for i in emojis:
      board_copy = board[:]

