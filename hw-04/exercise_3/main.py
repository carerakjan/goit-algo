import sys
from pathlib import Path
from colorama import Fore, Back, Style


def show_error(err: str):
    print(f'{Fore.RED}{err}{Fore.RESET}')


def get_colors(is_dir: bool):
    return (Fore.CYAN if is_dir else Fore.GREEN, Fore.RESET)


def print_path(source_path: Path, depth=0, depth_limit=20):
    if depth > depth_limit:
        return

    is_dir = source_path.is_dir()
    offset = Style.DIM + '| ' * (depth - 1) + '|_' + Style.RESET_ALL if depth else ''
    color, reset = get_colors(is_dir)
    print(f'{offset}{color}{source_path.name}{reset}')

    if source_path.is_dir():
        for dir_or_file in sorted(source_path.iterdir()):
            print_path(dir_or_file.absolute(), depth + 1, depth_limit)


def main():
    try:
        if len(sys.argv) < 2:
            raise Exception('Path is not specified')

        root_path = Path(sys.argv[1])

        if not root_path.exists():
            raise Exception(f'"{root_path}" is not exists')

        if not root_path.is_dir():
            raise Exception(f'"{root_path}" is not a directory')

        print_path(root_path)
    except Exception as e:
        show_error(e)


if __name__ == '__main__':
    main()
