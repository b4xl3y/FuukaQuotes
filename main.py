import discord
import os
import random

client = discord.Client()

def get_quote():
  quote_list = ["Yes! You knocked the enemy off balance!", 
  "*gasp* The enemy!", 
  "Trans Rights!", 
  "Be careful, I sense Death!",
  "There are two powerful enemies!",
  "Give me a sec; I'll scan the target.",
  "No... It can't end like this!",
  "Cheating, huh? I'm disappointed in you.",
  "Minato, what the hell is your problem?"]
  quote = random.choice(quote_list)
  return(quote)

def get_weakness():
  weakness_response = ["One second, I'm googling it.", "Sorry, the SMT Wiki is down!"]
  weakness = random.choices(weakness_response, weights=(90, 5), k=1)
  return(weakness)

def list2string(weakness):
  str1 = " "
  return(str1.join(weakness))

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Mass Destruction'))

    print('Logged in as {0.user}'.format(client))
    print('Connected')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!quote'):
    quote = get_quote()
    await message.channel.send(quote)
  
  if message.content.startswith('i like your shoelaces'):
    tumblr = 'Thanks! I got them from the president.'
    await message.channel.send(tumblr)

  if message.content.startswith("Fuuka, what is this shadow's weakness?"):
    weakness = get_weakness()
    weakness2 = list2string(weakness)
    await message.channel.send(weakness2)

client.run(os.getenv('TOKEN'))
