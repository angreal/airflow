import os
import subprocess
import webbrowser

import angreal
from angreal.integrations.venv import VirtualEnv, venv_required

venv_location = os.path.join(angreal.get_root(),'..','.venv')
cwd = os.path.join(angreal.get_root(), '..')
requirements = os.path.join(cwd,'dev_requirements.txt')
venv_python = VirtualEnv(venv_location, now=False).python_executable


tests = angreal.command_group(name="test", about="commands for executing tests")


@tests()
@angreal.command(name='run', about="run our test suite. default is unit tests only")
@angreal.argument(name="integrity", long="integrity", short='i', takes_value=False, is_flag=True, help="run integrity tests only")
@angreal.argument(name="full", long="full", short='f', takes_value=False, is_flag=True, help="run integration and unit tests")
@angreal.argument(name="open", long="open", short='o', takes_value=False, is_flag=True, help="open results in web browser")
@venv_required(venv_location,requirements=requirements)
def run_tests(integrity=False,full=False,open=False):

    v = VirtualEnv(venv_location,requirements=requirements,now=True)
    v.install_requirements()

    if full:
        integrity=False
    output_file = os.path.realpath(os.path.join(cwd,'htmlcov','index.html'))

    my_env = {**os.environ, "AIRFLOW_HOME":"/tmp"}

    if integrity:
        rv = subprocess.run(f'{venv_python} -m pytest tests/integrity',shell=True, cwd=cwd, env=my_env)
        open=False
    if full:
        rv = subprocess.run(f'{venv_python} -m pytest -vvv --cov=dags --cov-report html --cov-report term tests/',shell=True, cwd=cwd,env=my_env)
    if not integrity and not full:
        rv = subprocess.run(f'{venv_python} -m pytest -vvv --cov=dags --cov-report html --cov-report term tests/unit',shell=True, cwd=cwd,env=my_env)
    if open:
        webbrowser.open_new(f'file://{output_file}')
    if rv.returncode != 0:
        raise SystemExit(rv.returncode)


@tests()
@angreal.command(name='lint', about="lint our project")
@angreal.argument(name="open", long="open", short='o', takes_value=False, is_flag=True, help="open results in web browser")
@venv_required(venv_location,requirements=requirements)
def lint(open):

    rv = subprocess.run(
        (
        "pre-commit run --all-files"
        ),
        shell=True,
        cwd=cwd
    )
    if rv.returncode != 0:
        raise SystemExit(rv.returncode)

    if open:
        webbrowser.open(f'file:://{os.path.join(cwd,"typing_report","index.html")}')
