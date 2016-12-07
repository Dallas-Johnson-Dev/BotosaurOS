#!/usr/bin/python3.5

import discord
import commandfunctions
import adminfunctions
import command
from adminfunctions import admincoroutinereturn

client = discord.Client()
runner = command.CommandRunner(commandfunctions.cmdtable)
adminrunner = command.AdminCommandRunner(adminfunctions.cmdtable)
currentChannel = "#general"


# username = input("Email: ")
# password = input("Password: ")


@client.event
async def on_member_join(member):
    await client.send_message(currentChannel, 'Welcome to the server {0}'.format(member.name))


@client.event
async def on_message(message):
    if not client.user.name == message.author.name:
        if message.content[0] == '~':
            await client.send_message(message.channel, runner.executeFunction(client, message).getcontent())
        elif message.content[0] == '!':
            #Roles returns a list of the author's roles. Check the roles to see if they have a permission set for each command run.
            adminresult = adminrunner.executeFunction(client, message, message.author.roles).getcontent()
            print(type(adminresult))
            if type(adminresult) is str:
                await client.send_message(message.channel, adminresult)
            elif adminresult.rettype == "mute":
                await client.server_voice_state(adminresult.member, mute=True)
                await client.send_message(message.channel, adminresult.message)
    return

#put the run stuff here once it's transferred.
