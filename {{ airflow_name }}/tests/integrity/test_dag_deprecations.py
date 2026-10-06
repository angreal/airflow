import os
import subprocess
import sys

import pytest

from ..conftest import DAGS_FOLDER


def _dag_files():
    files = []
    for root, _, names in os.walk(DAGS_FOLDER):
        files += [os.path.join(root, n) for n in names if n.endswith(".py")]
    return sorted(files)


@pytest.mark.parametrize(
    "path", _dag_files(), ids=[os.path.relpath(p, DAGS_FOLDER) for p in _dag_files()]
)
def test_no_deprecations(path):
    """Test DAG files raise no deprecation warnings"""
    # Airflow reports deprecated imports as FutureWarning (DeprecatedImportWarning) and
    # deprecated interfaces as DeprecationWarning, so both are errors here.
    # A fresh interpreter per file makes sure every warning is raised again.
    env = {**os.environ, "PYTHONPATH": os.pathsep.join([DAGS_FOLDER, os.environ.get("PYTHONPATH", "")])}
    rv = subprocess.run(
        [sys.executable, "-W", "error::DeprecationWarning", "-W", "error::FutureWarning", path],
        capture_output=True,
        text=True,
        env=env,
    )
    assert rv.returncode == 0, rv.stderr
