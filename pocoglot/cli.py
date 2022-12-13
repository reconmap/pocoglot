#!/usr/bin/env python3

import logging
import os
import traceback
from importlib import import_module
from typing import List

import click
import coloredlogs
import jinja2
import yaml
from yaml.loader import SafeLoader

from pocoglot import __version__

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def list_languages_available() -> List[str]:
    files = os.listdir(os.path.join(SCRIPT_DIR, 'templates'))
    return [os.path.splitext(file)[0] for file in files]


@click.command()
@click.option('-from', '--from-file', required=True, help='Path to the source YAML file containing definitions', type=click.Path())
@click.option('-to', '--to-file', required=True, help='Path to where the targe code is going to be generated', type=click.Path())
@click.option('-lang', '--to-language', required=True, help='Language used for the generated code', type=click.Choice(list_languages_available()))
@click.option('-override', '--override-file', required=False, help='Path to the YAML file containing overrides', type=click.Path())
@click.option('-logging', '--logging-level', required=False, type=click.Choice(['INFO', 'DEBUG']), default='INFO')
@click.version_option(version=__version__)
def main(from_file, to_file, to_language, override_file, logging_level):
    logging_level = logging.getLevelName(logging_level)
    coloredlogs.install(level=logging_level, fmt='%(asctime)s.%(msecs)03d %(levelname)s %(message)s',
                        datefmt='%H:%M:%S', milliseconds=True)

    logging.info(
        f'Generating code in "{to_language}" from "{from_file}" to "{to_file}"')
    with open(from_file, 'r') as f:
        data = yaml.load(f, Loader=SafeLoader)

    if override_file:
        with open(override_file, 'r') as f:
            override_data = yaml.load(f, Loader=SafeLoader)
            data.update(override_data['common'])
            if to_language in override_data["languages"]:
                data.update(override_data["languages"][to_language])

    logging.debug(data)

    lang_module = import_module(
        f'.languages.{to_language}', package=__package__)

    lang_data = lang_module.modify_data(data)

    logging.debug(lang_data)

    tpl_loader = jinja2.FileSystemLoader(
        searchpath=os.path.join(SCRIPT_DIR, "templates"))
    tpl_env = jinja2.Environment(
        loader=tpl_loader, undefined=jinja2.StrictUndefined)
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
