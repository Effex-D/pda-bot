# bot.py
import os
import random
import asyncio
import json

with open('config.json') as config_file:
    config = json.load(config_file)
    token = config['token']
    master_user = config['master_user']

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')



@bot.event
async def on_connect():
    print(f'{bot.user.name} connected.')

@bot.event
async def on_disconnect():
    print(f'{bot.user.name} disconnected.')

@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready for action!')

#@client.event
#async def on_member_join(member):
#    await member.create_dm()
#    await member.dm_channel.send(
#        f'Hi {member.name}, welcome to my Discord server!'
#    )

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    #print(message.author)
    #print(master_user_string)
    message_channel = message.channel

    if (message.author.id == master_user['id']) and (message.channel.type is discord.ChannelType.private):
        print("Responding to DM from master user.")
        response = "message logged"
        await message.channel.send(response)

    if (message.content != '' and message.content[0] != "!"):
        print("Logging message: {}".format(message))

    elif message.content == 'raise-exception':
        raise discord.DiscordException
    await bot.process_commands(message)

@bot.command()
async def debug(ctx):
    if (ctx.author.id == master_user['id']):
        message = "I guess your debug command works."

        await ctx.send(message)

async def background_loop():
    await bot.wait_until_ready()
    print("Async message loop starting.")
    while bot.is_ready:
        print("Async loop: Loop functional.")
        need_to_message = False
        if need_to_message:
            user = bot.get_user(master_user["id"])
            print("Sending to: {}".format(user.id))
            await user.send("A random message. Hurrah!")
        delay_time = 43 * 60 + random.randint(1, int((30*60)/2)) # Weirdly random delay time.
        print("Async loop: Delaying for {} seconds".format(delay_time))
        await asyncio.sleep(delay_time)

bot.loop.create_task(background_loop())
bot.run(token)