from .cmd_help import handle_help
from .cmd_mod import handle_demod, handle_mod
from .cmd_quit import handle_quit


# ASCII Art: http://patorjk.com/software/taag/#p=display&f=Ogre&t=Commands

#    ___                                          _
#   / __\___  _ __ ___  _ __ ___   __ _ _ __   __| |___
#  / /  / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` / __|
# / /__| (_) | | | | | | | | | | | (_| | | | | (_| \__ \
# \____/\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|___/

COMMAND_MAP = {
    'help': handle_help,
    'mod': handle_mod,
    'demod': handle_demod,
    'quit': handle_quit,
}
