from pathlib import Path
from datetime import datetime

today = datetime.today()
timestamp = today.strftime('%Y%m%d')
base_path = Path(f"log_{timestamp}.txt")


def log(path: Path, message: str, level=0) -> None:
    text = ''
    lines = 0

    if path.exists():
        text = path.read_text()
        lines = len(text.split('\n'))
        text += '\n'

    log_levels = ('log', 'warn', 'err')
    path.write_text(f'{text}{lines}:[{log_levels[level]}] -> {message}')


log(base_path, 'hello')
log(base_path, 'hello1', level=1)
log(base_path, 'hello2', level=2)
