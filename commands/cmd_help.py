import discord


async def handle_help(client: discord.Client, message: discord.Message):
    """ Show the help for all available commands """
    
    from . import COMMAND_MAP

    help_str = '**Available Commands**\n'
    for cmd_str, cmd_func in COMMAND_MAP.items():
        help_str += f'!{cmd_str}\n```\n{cmd_func.__doc__}```\n'

    await message.channel.send(help_str)
