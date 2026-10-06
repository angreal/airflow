import os
import subprocess

from angreal.integrations.git import Git
from angreal.integrations.venv import VirtualEnv


def _project_root():
    """angreal runs init() from the rendered project (or its .angreal folder); older
    versions ran it from the parent folder."""
    here = os.getcwd()
    if os.path.basename(here) == ".angreal":
        return os.path.dirname(here)
    if os.path.isdir(os.path.join(here, ".angreal")):
        return here
    return os.path.join(here, "{{ airflow_name }}")


def init():
    os.chdir(_project_root())
    VirtualEnv(".venv", now=True, requirements="dev_requirements.txt").install_requirements()

    g = Git()
    g.init()
    g.add('.')

    subprocess.run(
        (
        "pre-commit install;"
        "pre-commit run --all-files;"
        "pre-commit run --all-files;"
        ),
        shell=True,
    )

    g.add('.')
    g.commit("{{ airflow_name }} initialized via angreal")
