import discord
import os


client=discord.client()

@client.event
async def on_ready():
	print (f"Logged In {client.user} ")

@client.Event
async def on_message(message):
	if message.author == client.user:#Check if it is the bots that sends the message
		return ''
	if message.content.startswith('$hello'):
		await message.channel.send('Hello')# Tell send response to the user



client.run(os.getenv('TOKEN'))