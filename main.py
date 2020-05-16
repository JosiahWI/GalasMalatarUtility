#!/usr/bin/python3

import aiosqlite
import discord
from discord.ext import commands

bot = commands.Bot('g.')

@bot.command()
async def checkclaim(ctx, *, pagename):
    async with aiosqlite.connect('pages.db') as conn:
        cursor = await conn.execute(
            'SELECT * FROM pages WHERE (page == ?)', [pagename.lower()])
        claim = await cursor.fetchone()
    if claim is None:
        await ctx.send('Page does not exist.')
    elif claim[1] is None:
        await ctx.send('Page is not claimed.')
    else:
        await ctx.send(f'{claim[1]} has claimed that page.')

@bot.command()
async def listclaims(ctx):
    async with aiosqlite.connect('pages.db') as conn:
        claims = await conn.execute(
            'SELECT * FROM pages WHERE (author != NULL);')
    await ctx.send(':+1:')

with open('token.txt', 'r') as fstream:
	token = fstream.readline().strip()

bot.run(token)
