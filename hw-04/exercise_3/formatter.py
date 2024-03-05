from colorama import Fore, Style


def get_colors(is_dir: bool, beautify: bool):
    if beautify:
        return Fore.LIGHTYELLOW_EX if is_dir else Fore.LIGHTWHITE_EX, Fore.RESET
    return Fore.CYAN if is_dir else Fore.GREEN, Fore.RESET


def get_assets():
    return {
        'ROOT': '📦',
        'DIR': '📂',
        'FILE': '📜',
        'LINE': '┃',
        'LINE_2': '┣'
    }


def format_path(path_name: str, is_dir: bool, depth: int, beautify=False):
    offset = Style.DIM + Fore.CYAN + '| ' * (depth - 1) + '|_' + Style.RESET_ALL if depth else ''
    asset = ''

    if beautify:
        assets = get_assets()
        offset = (assets['LINE'] + ' ') * (depth - 1) + assets['LINE_2'] if depth else ''
        asset = (assets['ROOT'] if depth == 0 else assets['DIR'] if is_dir else assets['FILE']) + ' '

    color, reset = get_colors(is_dir, beautify)
    print(f'{offset}{asset}{color}{path_name}{reset}')
