import discord 
import asyncio
import random
from PIL import Image
from discord.ext import commands
from discord.ext.commands import Bot

TOKEN="NTQ5NzAyMjU3MjIyODc3MTkz.D1XtzQ.zX3yk7fVtcrOF-WYjS1EeANP7HU"

$ heroku create myapp --buildpack heroku/python

"""cit1="Город разрушен - город не нужен."
cit2="Брат может не быть другом, но друг всегда брат."
cit3="Ты не знаешь меня, ты знаешь только то, что я позволяю тебе знать."
"""

mama=["Город разрушен - город не нужен.","Если мир встанет против тебя - у меня встанет на тебя","Мысли как охотник, ежи", "Брат может не быть другом, но друг всегда брат.","Ты не знаешь меня, ты знаешь только то, что я позволяю тебе знать.","Это твое, если ты делаешь красиво.", "-Брат, нассы на весь мир. -Брат, ты для меня весь мир"]
papa=["D:\danil.png", "D:\danil1.png", "D:\kuzhel.png", "D:\dimakuzhel.png", "D:\sratiki.png", "D:\srodanil.png", "D:\srodanilochka.png", "D:\srothers.png", "D:\superfamily.png", "D:\никита.png", "D:\suka.png"]
#secure_random = random.SystemRandom()

Bot=commands.Bot(command_prefix='!!')

@Bot.event
async def on_ready():
	print("ready for sucking")

@Bot.command(pass_context= True)
async def hello(ctx):
	await Bot.say("Hi, ziabl")

@Bot.command(pass_context= True)
async def love(ctx):
	await Bot.say("I love you, my dear")

@Bot.command(pass_context= True)
async def citation(ctx):
	await Bot.say(random.choice(mama))

@Bot.command(pass_context= True)
async def bro(ctx):
	area=ctx.message.channel
	await Bot.send_file(area, random.choice(papa))
	await Bot.say(random.choice(mama))
	
"""@Bot.command(pass_context= True)
async def bro(ctx):
	bro_pic=random.randint(1,3)
	if bro_pic==1:
		with open('danil.png', 'rb') as picture: await Bot.send_file(ctx.message.channel, picture)
	elif bro_pic==2:
		with open('danil1.png', 'rb') as picture: await Bot.send_file(ctx.message.channel, picture)
	elif bro_pic==3:
		with open('kuzhel.png', 'rb') as picture: await Bot.send_file(ctx.message.channel, picture)	
"""


@Bot.command(pass_context= True)
async def link(ctx):
	await Bot.say("!!citation")
	if Bot.say("!!citation"):
		await Bot.say(random.choice(mama))

	"""with open('dffanil.png', 'rb') as picture:
	#await Bot.send_file(channel, picture)
	await Bot.send_file(channel, 'danil.png')
	"""

#(local_file='danil.jpg',local_file='danil1.jpg')
	


Bot.run(TOKEN)
