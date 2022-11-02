from settings import Settings
from client import DavnClient


if __name__ == "__main__":
    print('Launching from main')

    print('Loading settings...')
    settings = Settings()
    print('Done')

    # Instantiate discord

    client = DavnClient(settings)
    client.run(settings.token)

    print('Exiting from main')
