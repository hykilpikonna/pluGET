import argparse

from .handlers.handle_config import check_config, validate_config
from .handlers.handle_input import handle_input
from .settings import PLUGETVERSION
from .utils.console_output import rename_console_title, clear_console, print_logo, \
    print_console_logo
from .utils.utilities import check_requirements, api_test_spiget, check_for_pluGET_update

__version__ = PLUGETVERSION


def run():
    parser = argparse.ArgumentParser(description="Arguments for pluGET",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("mode", help="Mode (install/update/etc.)", nargs='?', default=None)
    parser.add_argument("object", help="Object/Plugin Name", nargs='?', default=None)
    parser.add_argument("version", help="Version", nargs='?', default=None)
    parser.add_argument("--no-confirmation", action="store_true", help="Skip confirmation messages")
    args = vars(parser.parse_args())

    rename_console_title()
    check_config()
    validate_config()
    api_test_spiget()
    check_requirements()

    if args["mode"] is not None and args["object"] is not None:
        # arguments were used so call the handle_input function to get the right function call
        print_console_logo()
        check_for_pluGET_update()
        handle_input(args["mode"], args["object"], args["version"], args["no_confirmation"], arguments_from_console=True)
    else:
        # no arguments were used so start pluGET console
        clear_console()
        print_logo()
        check_for_pluGET_update()
        handle_input()
