from replit import db
import discord

# db.clear() # clears database of friend codes (use when necessary)

# Friend Codes: Set
async def set_code(msg, type="Nintendo Switch"): # Passes in Switch Friend Code by default
  author = msg.author.name
  db_key = author + type
  code = "".join(msg.content.split(' ')[1:])
  db[db_key] = code
  success_message = "{} friend code `{}` has been saved!".format(type, code)
  await msg.channel.send(success_message)

# Friend Codes: Get
async def get_code(msg):
  if len(msg.mentions) == 0:
    requested_author = msg.author.name
    requested_author_img = msg.author.avatar_url
  else:
    requested_author = msg.mentions[0].name
    requested_author_img = msg.mentions[0].avatar_url
  try:
    db_keys = db.prefix(requested_author)
    description = ""
    for key in db_keys:
      code = db[key]
      code_type = key[len(requested_author):]
      description = description + "**{}**: {}\n".format(code_type, code)
    success_message = discord.Embed(
      title = "{}'s friend codes".format(requested_author),
      description = description,
      color = 0xFABFB2
    )
    success_message.set_thumbnail(url=requested_author_img)
    return await msg.channel.send(embed=success_message)
  except:
    return await msg.channel.send("Uh oh.")