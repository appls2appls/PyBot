import discord
import random
import os
from discord.ext import commands
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('bot is ready')


@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = [':8ball: Absolutly.', 
    ':8ball: Absolutly not.', 
    ':8ball: It is true.', 
    ':8ball: Impossible.', 
    ':8ball: Of course.', 
    ':8ball: I do not think so.', 
    ':8ball: It is true.', 
    ':8ball: It is not true.', 
    ':8ball: I am very undoubtful of that.', 
    ':8ball: I am very doubtful of that.', 
    ':8ball: Sources point to no.', 
    ':8ball: Theories prove it.', 
    ':8ball: Reply hazy try again', 
    ':8ball: Ask again later', 
    ':8ball: Better not tell you now', 
    ':8ball: Cannot predict now', 
    ':8ball: Concentrate and ask again']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    ctx.send(f'Banned {member.mention}')




client.run('y0ur_t0k3n_H3re')