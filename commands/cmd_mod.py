import client_decorators
import parsers

import discord

@client_decorators.require_moderator
@client_decorators.require_args(parsers.UserParser())
async def handle_mod(client: discord.Client, message: discord.Message, username: str):
    """ [Moderator] Add someone to the moderator list
        param1: full_discord_name#1234 """
    if username not in client.game.moderators:
        client.game.moderators.append(username)
        await message.channel.send(f'{username} has been added to the game moderators list')
        return

    await message.channel.send(f'{username} is already in the game moderators list')



@client_decorators.require_moderator
@client_decorators.require_args(parsers.UserParser())
async def handle_demod(client: discord.Client, message: discord.Message, username: str):
    """ [Moderator] Remove someone from the moderator list
        param1: full_discord_name#1234 """
    if username in client.game.moderators:
        client.game.moderators.remove(username)
        await message.channel.send(f'{username} has been removed from the game moderators list')
        return

    await message.channel.send(f'{username} was not in the game moderators list')