import client_decorators

import discord


@client_decorators.require_admin
async def handle_quit(client: discord.Client, message: discord.Message):
    """[Admin] Request a graceful shutdown"""
    await message.channel.send('Close requested by admin. Goodbye!')
    # TODO: Figure out why this causes an on_message error
    await client.close()
