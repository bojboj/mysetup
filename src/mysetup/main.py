import os
from pathlib import Path

import typer


def main():
    config = Path.home().joinpath(".config")
    myconfig = config.joinpath("myconfig")
    projectconfig = config.joinpath("projectconfig")
    nvim = config.joinpath("nvim")

    print(f"updating {myconfig}")
    os.system(f"cd {myconfig} && git pull")

    print(f"updating {projectconfig}")
    os.system(f"cd {projectconfig} && git pull")

    print(f"updating {nvim}")
    os.system(f"cd {nvim} && git pull")

    print("restoring neovim plugins from snapshot")
    os.system(f"cd {nvim} && nvim -S plugsnapshot.vim +qa")

    print("done")


if __name__ == "__main__":
    typer.run(main)
