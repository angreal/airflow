import os
import subprocess

import angreal

cwd = os.path.join(angreal.get_root(), '..')
compose_file = os.path.join(angreal.get_root(), '..', 'dev', 'docker-compose.yaml')
logs = os.path.join(angreal.get_root(), '..', 'logs')
compose = f"docker compose -f {compose_file}"
demo = angreal.command_group(name="demo", about="commands for controlling the demo environment")


def _run(command):
    rv = subprocess.run(command, shell=True, cwd=cwd)
    if rv.returncode != 0:
        raise SystemExit(rv.returncode)


@demo()
@angreal.command(name="start", about="start services for example dags")
def demo_start():
    _run(f"{compose} build --no-cache && {compose} up -d --wait")


@demo()
@angreal.command(name="stop", about="stop services for example dags")
def demo_stop():
    _run(f"{compose} down")


@demo()
@angreal.command(name="clean", about="shut down services and remove files")
def demo_clean():
    _run(f"{compose} down --volumes --remove-orphans")
    _run(f"find {logs} -mindepth 1 ! -name .empty -delete")


@demo()
@angreal.command(name="restart", about="restart all service")
def demo_restart():
    demo_stop()
    demo_start()
