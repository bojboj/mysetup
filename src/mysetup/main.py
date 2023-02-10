import os
from pathlib import Path

import typer


def main():
    config = Path.home().joinpath('.config')
    myconfig = config.joinpath('myconfig')
    nvim = config.joinpath('nvim')

    print(f'updating {myconfig}')
    os.system(f'cd {myconfig} && git pull')

    print(f'updating {nvim}')
    os.system(f'cd {nvim} && git pull')
    os.system(f'cd {nvim} && nvim -S plugsnapshot.vim')
    
if __name__ == "__main__":
    typer.run(main)
