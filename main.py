#!/usr/bin/python3.5

import discord
import asyncio
import commandfunctions
import command

client = discord.Client()
runner = command.commandrunner(commandfunctions.cmdtable)
currentChannel = ""

#username = input("Email: ")
#password = input("Password: ")


@client.event
async def on_member_join(member):
    await client.send_message(currentChannel, 'Welcome to the server {0}'.format(member.name))


@client.event
async def on_message(message):
    if not client.user == message.author and message.content[0] is '~':
        await client.send_message(message.channel, runner.executeFunction(client, message).getcontent())
    return


#client.run(username,password)
