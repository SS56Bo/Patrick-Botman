import discord
import os
import random
from discord.ext import commands
client = discord.Client()

def get_quote():
    file=open('quote.txt','r')
    opn=file.read().splitlines()
    return (random.choice(opn))

@client.event
async def on_ready():
  print ('My Name is Patrick Botman')

@client.event
async def on_message(message):
  if message.author==client.user:
    return

  if message.content.startswith('hello!'):
    await message.channel.send("Hi, I'm Pat Botman")

  if message.content.startswith('give me a quote'):
    await message.channel.send(get_quote())

  if message.content.startswith('give me another'):
    await message.channel.send(get_quote())


  if message.content.startswith('play some music'):
    await message.channel.send("Do you like Huey Lewis and the News?")



  
client.run(os.environ['tokken'])
  