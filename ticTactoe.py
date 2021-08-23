import discord
import random 

#function asks user if they want to play with another person or the bot 
async def game_options(msg, client):
  choice = 0
  embed = discord.Embed(
    title = "Game Options",
    description = "1. TicTacToe (with a friend) \n 2. TicTacToe (with me)"
  )
  #await msg.channel.purge(limit=1)
  mes = await msg.channel.send(embed= embed)
  await mes.add_reaction('1️⃣')
  await mes.add_reaction('2️⃣')
  react = await get_char(msg, client)

  if react == '1️⃣':
    choice = 1
  elif react == '2️⃣':
    choice = 2
  return choice

#------------------------------------------------------------------------------------
async def play_tic(msg, client):
  blank = '⬜'
  #emojis that represent the spaces that are available and a quit button
  emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🛑']
  index = [0,1,2,3,4,5,6,7,8]
  #game board
  board = [blank, blank, blank,
           blank, blank, blank,
           blank, blank, blank,]
  characters = ['❎', '🅾️']

  await msg.channel.purge(limit=1) # Deletes message after reacting to avoid spam
  #asks player for their choice of character, X or O
  choice = await game_options(msg, client)
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
  Player2_char = characters[0]

  #recaps who's what character 
  await msg.channel.purge(limit=1)
  if choice == 1:
    Player2 = 'Player 2'
  else:
    Player2 = 'Chummy(PLayer 2)'

  embed = discord.Embed(
    title = 'Your character will be: ' + player + '\n' + Player2 + 'will be: ' + Player2_char,
    color = 0xFABFB2
  )
  await msg.channel.send(embed = embed)

  #randomly selects who will go first, player or cpu
  
  num = random.randint(1,2)
  if num == 1:
    currentplayer = num
    await msg.channel.send('Player ' + str(currentplayer) + '\'s turn:')
    await player_turn(msg, board, emojis, client, index, player)
  else:
    currentplayer = num
    if choice == 1:
      await msg.channel.send('Player ' + str(currentplayer) + '\'s turn:')
      await player_turn(msg, board, emojis, client, Player2_char)
    else:
      move = await bot_turn(msg, board, emojis, index, client, Player2_char, player)
      board[move] = Player2_char

  #initialize winner to being none
  winner = 'none'
  turn = 1
  while turn < 9:
    await msg.channel.purge(limit=3)
    winner = await check_win(board, player, Player2_char)
    if winner != 'none':
      break
    if currentplayer == 1:
      currentplayer = 2
      if choice == 1:
        await msg.channel.send('Player ' + str(currentplayer) + '\'s turn:')
        await player_turn(msg, board, emojis, client, index, player)
      else:
        move = await bot_turn(msg, board, emojis, index, client, Player2_char, player)
        board[move] = Player2_char
        await msg.channel.send(index) #for testing
    else:
      currentplayer = 1
      await msg.channel.send('Player ' + str(currentplayer) + '\'s turn:')
      await player_turn(msg, board, emojis, client, index, player)
    turn += 1
    await msg.channel.send('Player ' + str(currentplayer) + '\'s turn:')
  if turn == 9:
    await msg.channel.send('Tie!')
  else:
    await msg.channel.send('Winner! ' + winner)


  
#------------------------------------------------------------------------------------
async def get_char(msg, client):
  def check_reaction( reaction, user):
    return not user.bot

  reaction, user = await client.wait_for("reaction_add", timeout = 30.0, check = check_reaction)
  return str(reaction.emoji)

#------------------------------------------------------------------------------------
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

#------------------------------------------------------------------------------------
#function for when it is the player's turn 
async def player_turn(msg, board, emojis, client, index, player):
  #await msg.channel.send('Choose a position to place your character:')
  await print_board(msg, board, emojis)
  move = await get_char(msg, client)
  emojis.remove(move)
  if move == '1️⃣':
    board[0] = player
    index.remove(0)
  elif move == '2️⃣':
    board[1] = player
    index.remove(1)
  elif move ==  '3️⃣':
    board[2] = player
    index.remove(2)
  elif move ==  '4️⃣':
    board[3] = player
    index.remove(3)
  elif move ==  '5️⃣':
    board[4] = player
    index.remove(4)
  elif move ==  '6️⃣':
    board[5] = player
    index.remove(5)
  elif move ==  '7️⃣':
    board[6] = player
    index.remove(6)
  elif move ==  '8️⃣':
    board[7] = player
    index.remove(7)
  elif move ==  '9️⃣':
    board[8] = player
    index.remove(8)
  elif move == '🛑':
    pass

#------------------------------------------------------------------------------------
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

#------------------------------------------------------------------------------------
async def bot_turn(msg, board, emojis, index, client, bot, player):
  move  = 0 
  #this makes it so that 1/3 chances, the bot would not block the user from winning, so that there won't always be a tie
  ratio = random.randint(1,3)
  if ratio != 3:
    for chara in ['❎', '🅾️']:
      for i in index:
        board_copy = board[:]
        board_copy[i] = chara
        win = await check_win(board_copy, player, bot)
        if win == chara:
          move = i
          emojis.pop(index.index(move))
          index.remove(move)
          return move
  num = random.randint(0 , len(index) -1)
  move = index[num]
  emojis.pop(index.index(move))
  index.remove(move)
  return move