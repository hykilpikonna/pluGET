"""
Holds all the utilitie code for pluGET and the webrequests function
"""

import os
import re
import shutil
import sys
from pathlib import Path

import requests
from rich.console import Console
from rich.table import Table

from ..handlers.handle_config import config_value
from ..handlers.handle_ftp import ftp_create_connection
from ..handlers.handle_sftp import sftp_create_connection
from ..settings import PLUGETVERSION, HTTP
from ..utils.console_output import rich_print_error


def get_command_help(command: str) -> None:
    """
    Prints the help page for all commands and individual commands

    :param command: Console command which the help page should show

    :returns: None
    """
    rich_console = Console()
    rich_table = Table(box=None)
    rich_table.add_column("Command", justify="left", style="bright_blue", no_wrap=True)
    rich_table.add_column("Object", style="bright_magenta")
    rich_table.add_column("Params", justify="left", style="cyan")
    rich_table.add_column("Description", justify="left", style="white")
    match command:
        case "all":
            rich_table.add_row("check", "Name/all", None, "Check for an update of an installed plugin")
            rich_table.add_row("check", "serverjar", None, "Check for an update for the installed serverjar")
            rich_table.add_row("exit", "./anything", None, "Exit pluGET")
            rich_table.add_row("get", "Name/ID", None, "Downloads the latest version of a plugin")
            rich_table.add_row("get-paper", "PaperVersion", "McVersion", "Downloads a specific PaperMc version")
            rich_table.add_row("get-purpur", "PurpurVersion", "McVersion", "Downloads a specific Purpur version")
            rich_table.add_row("get-velocity", "VelocityVersion", "McVersion", "Downloads a specific Velocity version")
            rich_table.add_row(
                "get-waterfall", "WaterfallVersion", "McVersion", "Downloads a specific waterfall version"
            )
            rich_table.add_row("help", "./anything", None, "Get specific help to the commands of pluGET")
            rich_table.add_row("remove", "Name", None, "Delete an installed plugin from the plugin folder")
            rich_table.add_row("search", "Name/all", None, "Search for a plugin and download the latest version")
            rich_table.add_row("update", "Name/all", None, "Update installed plugins to the latest version")
            rich_table.add_row("update", "serverjar", None, "Update the installed serverjar to the latest version")
        case "check":
            rich_table.add_row("check", "Name/all", None, "Check for an update of an installed plugin")
            rich_table.add_row("check", "serverjar", None, "Check for an update for the installed serverjar")
        case "exit":
            rich_table.add_row("exit", "./anything", None, "Exit pluGET")
        case "get":
            rich_table.add_row("get", "Name/ID", None, "Downloads the latest version of a plugin")
        case "get-paper":
            rich_table.add_row("get-paper", "PaperVersion", "McVersion", "Downloads a specific PaperMc version")
        case "get-purpur":
            rich_table.add_row("get-purpur", "PurpurVersion", "McVersion", "Downloads a specific Purpur version")
        case "get-velocity":
            rich_table.add_row("get-velocity", "VelocityVersion", "McVersion", "Downloads a specific Velocity version")
        case "get-waterfall":
            rich_table.add_row(
                "get-waterfall", "WaterfallVersion", "McVersion", "Downloads a specific Waterfall version"
            )
        case "help" | "all":
            rich_table.add_row("help", "./anything", None, "Get specific help to the commands of pluGET")
        case "remove":
            rich_table.add_row("remove", "Name", None, "Delete an installed plugin from the plugin folder")
        case "search":
            rich_table.add_row("search", "Name/all", None, "Search for a plugin and download the latest version")
        case "update":
            rich_table.add_row("update", "Name/all", None, "Update installed plugins to the latest version")
            rich_table.add_row("update", "serverjar", None, "Update the installed serverjar to the latest version")
        case _:
            rich_print_error(f"[not bold]Error: Help for command [bright_magenta]'{command}' [bright_red]not found!")
            rich_print_error("Use [bright_blue]'help all' [bright_red]to get a list of all commands.")
            return None

    rich_console.print(rich_table)


def api_do_request(url: str) -> list | dict | None:
    """
    Handles the webrequest and returns a json list
    """
    try:
        return HTTP.get(url).json()
    except:
        rich_print_error("Error: Couldn't parse json of webrequest")
        return None


def api_test_spiget() -> None:
    """
    Test if the Spiget api sends a 200 status code back
    """
    try:
        r = HTTP.get('https://api.spiget.org/v2/status')
        if r.status_code != 200:
            rich_print_error("Error: Problems with the API detected. Plese try it again later!")
            exit(-1)
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError):
        rich_print_error("Error: Couldn't make a connection to the API. Check you connection to the internet!")
        exit(-1)


def create_temp_plugin_folder() -> Path:
    """
    Creates a temporary folder to store plugins inside
    Returns full path of temporary folder
    """
    path_temp_plugin_folder = Path("./TempSFTPFolder")
    if os.path.isdir(path_temp_plugin_folder):
        return path_temp_plugin_folder

    try:
        os.mkdir(path_temp_plugin_folder)
    except OSError:
        rich_print_error(f"Error: Creation of directory {path_temp_plugin_folder} failed")
        rich_print_error("       Please check for missing permissions in folder tree!")
        sys.exit()
    return path_temp_plugin_folder


def remove_temp_plugin_folder() -> None:
    """
    Removes the temporary plugin folder and all content inside it
    """
    try:
        shutil.rmtree(Path("./TempSFTPFolder"))
    except OSError as e:
        rich_print_error(f"Error: {e.filename} - {e.strerror}")
    return


def convert_file_size_down(file_size) -> float:
    """
    Convert the size of the number one down. E.g. MB -> KB through division with 1024
    """
    converted_file_size = (int(file_size)) / 1024
    converted_file_size = round(converted_file_size, 2)
    return converted_file_size


def check_local_plugin_folder(config_values) -> None:
    """
    Check if a local plugin folder exists and if not exit the programm
    """
    if config_values.local_seperate_download_path:
        plugin_folder_path = config_values.local_path_to_seperate_download_path
    else:
        plugin_folder_path = config_values.path_to_plugin_folder
    if not os.path.isdir(plugin_folder_path):
        rich_print_error(f"Error: Local plugin folder '{plugin_folder_path}' couldn't be found! \
        \n       Check the config and try again!")
        sys.exit()
    return None


def check_requirements() -> None:
    """
    Check if the plugin folders are available
    """
    config_values = config_value()
    match config_values.connection:
        case "local":
            check_local_plugin_folder(config_values)
        case "sftp":
            sftp_create_connection()
        case "ftp":
            ftp_create_connection()
    return None
