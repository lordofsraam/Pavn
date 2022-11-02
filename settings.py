import json
import datetime

from typing import Dict, List


class Settings(object):
    def __init__(self, file_name="settings.json"):
        # Load JSON file and deserialize
        with open(file_name, 'r') as f:
            self.blob = json.load(f)

        self._google_scope = ['https://spreadsheets.google.com/feeds',
                              'https://www.googleapis.com/auth/drive']

        # Variables for time based memoization
        self._squares_db_cache: List[str] = None
        self._last_fetch: datetime.datetime = None

    def __getattribute__(self, attr):
        # Forward attribute requests to JSON blob
        # Could also be done with setattr()?
        blob = super().__getattribute__('blob')

        if attr in blob:
            validator = getattr(self, 'validate_'+attr, None)
            if callable(validator):
                return validator(blob[attr])

            return blob[attr]

        return super().__getattribute__(attr)


if __name__ == "__main__":
    s = Settings()
