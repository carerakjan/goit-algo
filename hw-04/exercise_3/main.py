import sys
from pathlib import Path
from colorama import Fore
from formatter import format_path


def print_path(source_path: Path, beautify: bool, depth=0, depth_limit=20):
    if depth > depth_limit:
        return

    is_dir = source_path.is_dir()
    format_path(source_path.absolute().name, is_dir=is_dir, depth=depth, beautify=beautify)

    if is_dir:
        for dir_or_file in sorted(source_path.iterdir()):
            print_path(dir_or_file.absolute(), beautify, depth + 1, depth_limit)


def main():
    try:
        if len(sys.argv) < 2:
            raise Exception('Path is not specified')

        root_path = Path(sys.argv[1])
        beautify = True if len(sys.argv) > 2 and sys.argv[2] == '-b' else False

        if not root_path.exists():
            raise Exception(f'"{root_path}" is not exists')

        if not root_path.is_dir():
            raise Exception(f'"{root_path}" is not a directory')

        print_path(root_path, beautify)
    except Exception as e:
        print(f'{Fore.RED}{e}{Fore.RESET}')


if __name__ == '__main__':
    main()
