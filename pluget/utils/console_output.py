"""
Handles the console on first startup of pluGET and prints logo and sets title
"""

import os
from rich.console import Console

from ..settings import PLUGETVERSION


def rich_print_error(error_message) -> None:
    """
    Prints a formatted error message from rich
    """
    console = Console()
    console.print(error_message, style="bright_red")
    return None


def rename_console_title() -> None:
    """
    Renames the console title on first startup
    """
    if os.name == "nt":
        os.system("title " + "pluGET │ By Neocky")
    return None


def clear_console() -> None:
    """
    Clears the console on first startup
    """
    os.system('cls' if os.name=='nt' else 'clear')
    return None


def print_logo() -> None:
    """
    Prints the logo of pluGET and the link to the github repo
    """
    # use rich console
    console = Console()
    # line 1
    console.print()
    # line 2
    console.print("    ██████",style="bright_magenta", end='')
    console.print("╗ ", style="bright_yellow", end='')
    console.print("██", style="bright_magenta", end='')
    console.print("╗     ", style="bright_yellow", end='')
    console.print("██", style="bright_magenta", end='')
    console.print("╗   ", style="bright_yellow", end='')
    console.print("██", style="bright_magenta", end='')
    console.print("╗ ", style="bright_yellow", end='')
    console.print("██████", style="bright_magenta", end='')
    console.print("╗ ", style="bright_yellow", end='')
    console.print("███████", style="bright_magenta", end='')
    console.print("╗", style="bright_yellow", end='')
    console.print("████████", style="bright_magenta", end='')
    console.print("╗", style="bright_yellow")
    # line 3
    console.print("    ██", style="bright_magenta", end='')
    console.print("╔══", style="bright_yellow", end='')
    console.print("██", style="bright_magenta", end='')
    console.print("╗",	style="bright_yellow", end='')
    console.print("██", style="bright_magenta", end='')
    console.print("║     ", style="bright_yellow", end='')
    console.print("██", style="bright_magenta", end='')
    console.print("║   ", style="bright_yellow", end='')
    console.print("██", style="bright_magenta", end='')
    console.print("║", style="bright_yellow", end='')
    console.print("██", style="bright_magenta", end='')
    console.print("╔════╝ ", style="bright_yellow", end='')
    console.print("██", style="bright_magenta", end='')
    console.print("╔════╝╚══", style="bright_yellow", end='')
    console.print("██", style="bright_magenta", end='')
    console.print("╔══╝", style="bright_yellow")
    # line 4
    console.print("    ██████", style="bright_magenta", end='')
    console.print("╔╝", style="bright_yellow", end='')
    console.print("██", style="bright_magenta", end='')
    console.print("║     ", style="bright_yellow", end='')
    console.print("██", style="bright_magenta", end='')
    console.print("║   ", style="bright_yellow", end='')
    console.print("██", style="bright_magenta", end='')
    console.print("║", style="bright_yellow", end='')
    console.print("██", style="bright_magenta", end='')
    console.print("║  ", style="bright_yellow", end='')
    console.print("███", style="bright_magenta", end='')
    console.print("╗", style="bright_yellow", end='')
    console.print("█████", style="bright_magenta", end='')
    console.print("╗     ", style="bright_yellow", end='')
    console.print("██", style="bright_magenta", end='')
    console.print("║   ", style="bright_yellow")
    # line 5
    console.print("    ██", style="bright_magenta", end='')
    console.print("╔═══╝ ", style="bright_yellow", end='')
    console.print("██", style="bright_magenta", end='')
    console.print("║     ", style="bright_yellow", end='')
    console.print("██", style="bright_magenta", end='')
    console.print("║   ", style="bright_yellow", end='')
    console.print("██", style="bright_magenta", end='')
    console.print("║", style="bright_yellow", end='')
    console.print("██", style="bright_magenta", end='')
    console.print("║   ", style="bright_yellow", end='')
    console.print("██", style="bright_magenta", end='')
    console.print("║", style="bright_yellow", end='')
    console.print("██", style="bright_magenta", end='')
    console.print("╔══╝     ", style="bright_yellow", end='')
    console.print("██", style="bright_magenta", end='')
    console.print("║   ", style="bright_yellow")
    # line 6
    console.print("    ██", style="bright_magenta", end='')
    console.print("║     ", style="bright_yellow", end='')
    console.print("███████", style="bright_magenta", end='')
    console.print("╗╚", style="bright_yellow", end='')
    console.print("██████", style="bright_magenta", end='')
    console.print("╔╝╚", style="bright_yellow", end='')
    console.print("██████", style="bright_magenta", end='')
    console.print("╔╝", style="bright_yellow", end='')
    console.print("███████", style="bright_magenta", end='')
    console.print("╗   ", style="bright_yellow", end='')
    console.print("██", style="bright_magenta", end='')
    console.print("║   ", style="bright_yellow")
    # line 7
    console.print("    ╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ", style="bright_yellow")
    # line 8
    console.print()
    # line 9
    console.print("          ┌────────────────────────────────────┐", style="bright_black")
    # line 10
    console.print("          │             [", style="bright_black", end='')
    console.print("By Neocky", style="bright_magenta", end='')
    console.print("]            │                                   ", style="bright_black")
    # line 11
    console.print("          │  ", style="bright_black", end='')
    console.print("https://github.com/Neocky/pluGET", style="link https://github.com/Neocky/pluGET", end='')
    console.print("  │                                                  ", style="bright_black")
    # line 12
    console.print("          └────────────────────────────────────┘", style="bright_black")
    console.print("    ───────────────────────────────────────────────────")
    return None


def print_console_logo() -> None:
    """
    Prints the logo of pluGET if it is called from console
    """
    console = Console()
    console.print(f"[not bold][bright_magenta]pluGET [bright_green]{PLUGETVERSION} ", end='')
    console.print("created by Neocky → ", end='')
    console.print("https://github.com/Neocky/pluGET", style="link https://github.com/Neocky/pluGET")
    return None
