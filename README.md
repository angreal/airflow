# Airflow Template


Bootstrap a local airflow environment - fast.

``` pip install angreal && angreal init https://github.com/angreal/airflow.git ```

## Features

```
angreal 2.0.4

USAGE:
    angreal [OPTIONS] <SUBCOMMAND>

OPTIONS:
    -h, --help       Print help information
    -v, --verbose    verbose level, (may be used multiple times for more verbosity)
    -V, --version    Print version information

SUBCOMMANDS:
    dev-clean      shut down services and remove files
    dev-restart    restart all service
    dev-setup      setup a development environment
    dev-start      start services for example dags
    dev-stop       stop services for example dags
    help           Print this message or the help of the given subcommand(s)
    init           Initialize an Angreal template from source.
    lint           lint our project
    run-tests      run our test suite. default is unit tests only
```
