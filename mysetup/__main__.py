import os
from pathlib import Path

import typer

app = typer.Typer()
config = Path.home().joinpath(".config")
myconfig = config.joinpath("myconfig")
projectconfig = config.joinpath("projectconfig")
nvim = config.joinpath("nvim")


@app.command()
def install():
    if not myconfig.exists():
        print(f"installing {myconfig}")
        os.system(f"cd {config} && git clone git@github.com:bojboj/myconfig.git")

    if not projectconfig.exists():
        print(f"installing {projectconfig}")
        os.system(f"cd {config} && git clone git@github.com:bojboj/projectconfig.git")

    if not nvim.exists():
        print(f"installing {nvim}")
        os.system(f"cd {config} && git clone git@github.com:bojboj/nvim.git")

    os.system(f"cd {nvim} && nvim -S plugsnapshot.vim +qa")

    print("done")


@app.command()
def update():
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
    app()
