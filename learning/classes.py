class WriteFile:
    def __init__(self, fileName: str, message: str) -> None:
        try:
            self.file = open(fileName, 'r+', encoding='utf-8')
        except:
            self.file = open(fileName, 'w+', encoding='utf-8')

        lines = self.file.readlines()
        index = 0

        if len(lines) > 0:
            last = lines[-1]
            index = int(last.split(':')[0]) + 1

        self.file.write(f'{index}:{message}\n')


    def __del__(self) -> None:
        self.file.close()


from pathlib import Path

# Початковий шлях
base_path = Path("log.txt")

def log(base_path: Path, message: str, level=0) -> None:
    text = ''
    if base_path.exists():
        text = base_path.read_text()
        text += '\n'
    log_levels = ('log', 'warn', 'err')
    base_path.write_text(f'{text}[{log_levels[level]}] -> {message}')

log(base_path, 'hello')
log(base_path, 'hello1', level=1)
log(base_path, 'hello2', level=2)