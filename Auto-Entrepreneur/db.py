from dataclasses import dataclass
from pathlib import Path
import logging
logger = logging.getLogger(__name__)

class DB:
    def __init__(self, path):
        self.path = Path(path).absolute()
        self.path.mkdir(parents=True, exist_ok=True)

    def __getitem__(self, key):
        full_path = self.path / key
        try:
            with full_path.open("r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            logger.error(f"Key not found: {key}")
            raise KeyError(key)
        except Exception as e:
            logger.error(f"Error reading key {key}: {e}")
            raise

    def __setitem__(self, key, val):
        full_path = self.path / key
        full_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            if isinstance(val, str):
                full_path.write_text(val, encoding="utf-8")
            else:
                raise TypeError("val must be either a str or bytes")
        except Exception as e:
            logger.error(f"Error writing key {key}: {e}")
            raise

    def __delitem__(self, key):
        full_path = self.path / key
        if full_path.is_file():
            full_path.unlink()
        else:
            raise KeyError(key)

    def keys(self):
        return [str(p.relative_to(self.path))
