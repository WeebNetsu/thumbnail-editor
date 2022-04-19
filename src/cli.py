from termcolor import colored
from parser import args


def giveError(message: str) -> None:
    """Display error message and exits program"""
    print(colored(f"Error: {message}", "red"))
    exit()


def giveWarning(message: str) -> None:
    """Display warning message, but does NOT exit the program"""
    if not args.quiet:
        print(colored(f"Warning: {message}", "yellow"))
