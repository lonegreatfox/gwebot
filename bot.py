import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from random import randint, seed
from time import time


seed(time())


Bot = commands.Bot(command_prefix="!")


@Bot.event
async def on_ready():
    print("Bot is online")


# list of commands
@Bot.command(pass_context=True)
async def gwe_help(ctx):
    await ctx.send('(!rand_of_team | количество команд | список игроков) — распредляет людей по командам')
    await ctx.send('(!creation_time | пользователь) — время регистрации пользователя')


# randomization of teams
@Bot.command(pass_context=True)
async def rand_of_team(ctx, count_of_team, *arg):
    players = list(arg)
    count_of_team = int(count_of_team)
    count_of_players = len(players) // count_of_team
    msg = ""
    for i in range(count_of_team):
        msg += "Команда " + str(i+1) + ':' + '\n'
        for j in range(0, int(count_of_players)):
            s = players[randint(0, len(players) - 1)]
            msg += " " + s
            players.remove(s)
        msg += "\n"
    await ctx.send(msg)


# the time of account creation
@Bot.command(pass_context=True)
async def creation_time(ctx, user: discord.User):
    await ctx.send("{}".format(user.created_at))


token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
