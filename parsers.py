import re


class BoolParser(object):
    def __call__(self, token: str) -> bool:
        token = token.lower()

        valid_falses = ['0', 'false', 'f', 'off']
        valid_trues = ['1', 'true', 't', 'on']

        val = None

        if token in valid_trues:
            val = True
        elif token in valid_falses:
            val = False

        if val is None:
            raise ValueError(f'{token} is not a valid boolean value.')

        return val


class UserParser(object):
    def __call__(self, token: str) -> str:
        # TODO: Check for mentions?

        # User regex to find regular full discord usernames
        magic_goop = r"\w+#\d{4}"
        match = re.search(magic_goop, token)

        if match:
            return match[0]

        raise ValueError(f'Invalid discord username: {token}')


if __name__ == "__main__":
    # TODO: Add tests
    pass
