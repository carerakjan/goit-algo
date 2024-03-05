from colorama import Fore, Style

assets = {
    'ROOT': '📦',
    'DIR': '📂',
    'FILE': '📜',
    'LINE': '┃',
    'LINE_2': '┣'
}

colors = {
    'DEFAULT': (Fore.CYAN, Fore.GREEN),
    'ASSETS': (Fore.LIGHTYELLOW_EX, Fore.LIGHTWHITE_EX)
}


def get_colors(is_dir: bool, beautify: bool):
    dir_color, file_color = colors['ASSETS' if beautify else 'DEFAULT']
    return dir_color if is_dir else file_color, Fore.RESET


def format_path(path_name: str, is_dir: bool, depth: int, beautify=False):
    offset = Style.DIM + Fore.CYAN + '| ' * (depth - 1) + '|_' + Style.RESET_ALL if depth else ''
    asset = ''

    if beautify:
        offset = (assets['LINE'] + ' ') * (depth - 1) + assets['LINE_2'] if depth else ''
        asset = (assets['ROOT'] if depth == 0 else assets['DIR'] if is_dir else assets['FILE']) + ' '

    color, reset = get_colors(is_dir, beautify)
    print(f'{offset}{asset}{color}{path_name}{reset}')
