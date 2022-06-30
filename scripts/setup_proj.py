#!/usr/bin/python3
'''
project setup scripts

version: 0.2.0

This script should
 - setup a virtual environment
 - installs requirements from a requirement.txt file
 - installs a database
'''
import sys
import os
import subprocess
import pathlib
from exceptions import (
    NoOptionPassed,
    OptionNo
)

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
setup_db_file = 'setupdb'


def install_db():
    ''' installs a database by running script
    '''
    install_pgsql = ['./scripts/setupdb']
    subprocess.run(install_pgsql, cwd=BASE_DIR)


def setup_venv():
    pass

def main():
    ''' script entry point
    '''
    idb = input('install a postgresql db (y/n)? ')
    if idb != 'n':
        try:
            install_db()
        except Exception as e:
            print(e)

    ivenv = input('create a virtual environment (y/n)?')
    if ivenv != 'n':
        try:
            venv_name: str
            venv_name = input('virtual environemt name (defualt: proj_env)? ')
            if venv_name:
                pass
            else:
                raise(NoOptionPassed)
        except NoOptionPassed:
            venv_name = 'proj_env'

        # installs virtualenv
        # creates a virtual environment
        # install dependecies
        # stores some output in a logfile
        install_virtualenv = ['./scripts/install_virtualenv']
        make_venv = ['virtualenv', f'{venv_name}']
        install_dependecies = [f'{venv_name}/bin/python3',
                            '-m', 'pip', 'install', '-r', 'requirements.txt']

        with open('logfile', mode='w', encoding='utf8') as logfile:
            try:
                subprocess.run(install_virtualenv, stdout=logfile, cwd=BASE_DIR)
                subprocess.run(make_venv, stdout=logfile, cwd=BASE_DIR)

                install_option = input(
                    'would you like to install requirements.txt (y/n, Yes/No)? ')

                if install_option in ('y', 'Yes'):
                    subprocess.run(install_dependecies, cwd=BASE_DIR)
                if install_option in ('n', 'No'):
                    raise(OptionNo)
                else:
                    raise(NoOptionPassed)

            except OptionNo:
                pass
            except Exception as e:
                print(e)


if __name__ == '__main__':
    main()
