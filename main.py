import discord
import os
client = discord.Client()

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
    await message.channel.send("")


client.run(os.environ['tokken'])
  