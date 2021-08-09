import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
import json

load_dotenv()
TOKEN = 'NzE1OTg3NDY2MzY4MzE5NjMw.XtFPNw.E3QQNyX4WWSkE7DTRs5EOKt81TI'
GUILD = 'PythonBot'

# myfile=open("discord.json","r")
# stuff=json.load(myfile)
# myfile.close()
# print(stuff)
# print(len(stuff))
# stuff[1]['items']="6"
# stuff.append({'id':'numbers', 'items':'8'})
# myfile=open("discord.json","w")
# json.dump(stuff, myfile)
# # myfile.write(stuff)
# myfile.close()


client = discord.Client()
client=commands.Bot(command_prefix='/')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# @client.event
# async def on_message(message):
#     if message.content.startswith('hello'):
#         await message.channel.send('hello')

@client.command(name="hello", help="hello")
async def hello(ctx):
    await ctx.send("hello")
    #ctx.send('f"{ctx.message.author.id}"')
    print(f"{ctx.message.author.id}")

@client.command(name="bet", help="bet half your money")
async def bet(ctx):
    await ctx.send('Confirm this is the answer you want by using `Y` or `n`.')
    @client.event
    async def profile(ctx, message):
        if ctx.message.server == None:
            pass
        else:
            print("hello")



client.run(TOKEN)