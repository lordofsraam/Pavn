import discord

from commands import COMMAND_MAP
from settings import Settings

from typing import Any


class DavnClient(discord.Client):
    def __init__(self, settings: Settings, **options: Any) -> None:
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents, **options)

        self.settings = settings
        self.game_channel = None

    def get_channel_by_name(self, name, case_sensitive=False):
        """ Retrieve the first  that matches name from any server """
        if case_sensitive:
            name = name.lower()
        for channel in self.get_all_channels():
            if type(channel) is discord.TextChannel:
                search_name = channel.name
                if case_sensitive:
                    search_name = search_name.lower()
                if search_name == name:
                    return channel
        return None

    async def on_ready(self):
        print(f'[-] {self.user} has connected to Discord')

        # Find the main channel we will post messages in
        game_channel = self.get_channel_by_name(self.settings.game_channel)
        if not game_channel:
            print(
                f'[*] Unable to find game channel: {self.settings.game_channel}')
        self.game_channel = game_channel
        print(f'[-] Game channel set to {self.game_channel}')

    async def on_error(self, event, *args, **kwargs):
        print(f'[!] {event}\n\t{args}')

    async def on_message(self, message):
        """ Handle messages """

        # Ignore messages from yourself
        if message.author == self.user:
            return

        print(
            f'[-] "{message.content}"\n\ton: {message.channel}\n\tfrom: {message.author}')

        # Route messages to their corresponding handlers
        # TODO: Figure out if I'm using async correctly in the handlers
        if message.content.find(self.settings.command_char) == 0 and len(message.content) > 1:
            # Get the command name without the command char and arguments
            command_name = message.content.lower().split()[0][1:]

            # Try calling the handler, if it fails then its not a command
            try:
                command_function = COMMAND_MAP[command_name]
                await command_function(self, message)
            except Exception as e:
                print('[!]', e)
                await message.channel.send('No/Failed command: ' + command_name)
