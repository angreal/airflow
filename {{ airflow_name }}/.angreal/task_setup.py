import os
import subprocess

import angreal
from angreal.integrations.venv import VirtualEnv

venv_location = os.path.join(angreal.get_root(),'..','.venv')
cwd = os.path.join(angreal.get_root(), '..')

@angreal.command(name='dev-setup', about="setup a development environment")
def setup_env():
    v = VirtualEnv(venv_location, now=True, requirements="dev_requirements.txt")
    v.install_requirements()
    subprocess.run(
        (
        "pre-commit install;"
        "pre-commit run --all-files;"
        ),
        shell=True,
        cwd=cwd
    )
