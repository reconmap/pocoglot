#!/usr/bin/env python3

from typing import List

import traceback

import os
import yaml
from yaml.loader import SafeLoader

import logging
import coloredlogs
coloredlogs.install(level=logging.DEBUG, fmt='%(asctime)s.%(msecs)03d %(levelname)s %(message)s', datefmt='%H:%M:%S', milliseconds=True)

import jinja2

import click

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def list_languages_available() -> List[str]:
    files = os.listdir(os.path.join(SCRIPT_DIR, 'code-templates'))
    return [os.path.splitext(file)[0] for file in files]

from importlib import import_module

@click.command()
@click.option('-from', '--from-file', required=True, help='Path to the source YAML file', type=click.Path())
@click.option('-to', '--to-file', required=True, help='Path to the generated code file', type=click.Path())
@click.option('-lang', '--to-language', required=True, help='Language used for the generated code', type=click.Choice(list_languages_available()))
def main(from_file, to_file, to_language):
    logging.info(f'Generating code in "{to_language}" from "{from_file}" to "{to_file}"')
    with open(from_file, 'r') as f:
        data = yaml.load(f, Loader=SafeLoader)

    logging.debug(data)

    lang_module = import_module(f'languages.{to_language}')

    lang_data = lang_module.modify_data(data)

    logging.debug(lang_data)

    tpl_loader = jinja2.FileSystemLoader(searchpath=os.path.join(SCRIPT_DIR, "code-templates"))
    tpl_env = jinja2.Environment(loader=tpl_loader, undefined=jinja2.StrictUndefined)
    tpl = tpl_env.get_template(f'{to_language}.jinja')

    try:
        tpl.stream(poco=lang_data).dump(to_file)
        logging.info('Done!')

        if lang_module.is_valid(to_file):
            logging.info('Code validation complete')
        else:
            logging.warning('Validation failed')
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    main()

