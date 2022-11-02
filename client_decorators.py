import functools
import shlex
from inspect import signature


import discord


def require_admin(func):
    @functools.wraps(func)
    async def wrapper(client: discord.Client, message: discord.Message):
        if str(message.author) not in client.settings.bot_admins:
            await message.channel.send(f'Sorry {message.author.name}, only bot admins can perform that action.')
            return
        await func(client, message)

    return wrapper


def require_moderator(func):
    @functools.wraps(func)
    async def wrapper(client: discord.Client, message: discord.Message):
        if str(message.author) not in (client.game.moderators + client.settings.bot_admins):
            await message.channel.send(f'Sorry {message.author.name}, only game moderators can perform that action.')
            return
        await func(client, message)

    return wrapper


def require_args(*args):
    """ Require these arguments. They will be passed to the function as the types provided inside the kwarg 'parsed_args'. """

    # TODO: Figure out how to make this work with kwargs and default args
    def require_arg(func):
        sig = signature(func)
        needed_parameters = len(args) + 2  # +2 for client and message
        actual_parameters = len(sig.parameters)
        if actual_parameters < needed_parameters:
            raise AttributeError(
                f'Decorated function {func} does not accept the correct about of parameters. Needed {needed_parameters}, actual {actual_parameters}')

        @functools.wraps(func)
        async def wrapper(client, message):
            # Get the actual and required parameter counts
            tokens = shlex.split(message.content)
            require_count = len(args)

            # Send error message if counts dont match
            if len(tokens) - 1 < require_count:
                await message.channel.send(f'Insufficient arguments to command. {require_count} needed.')
                return

            # Parse only as many tokens as requested as requested type
            parsed_args = []
            for i, arg in enumerate(tokens[1:needed_parameters-1]):
                try:
                    parsed_args.append(args[i](arg))
                except Exception as e:
                    await message.channel.send(f'Error in parsing your argument "*{arg}*" as a "*{args[i]}*"')
                    await message.author.send(f'Error from your command:\n\t*{e}*')
                    return

            await func(client, message, *parsed_args)

        return wrapper

    return require_arg
