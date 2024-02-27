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


def log(file: str, message: str, level=0) -> None:
    log_levels = ('log', 'warn', 'err')
    WriteFile(fileName=file, message=f'[{log_levels[level]}] -> {message}')

log('log.txt', 'hello')
log('log.txt', 'hello1', level=1)
log('log.txt', 'hello2', level=2)