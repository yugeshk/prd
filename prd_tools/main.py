"""
The main entry point for handling your PRD submission for SwEnt
USAGE: swent-prd [OPTIONS] COMMAND [ARGS]...

Commands : 

1. Initialize : swent-prd init (<folder_name>)
2. Generate PDF : swent-prd generate (<folder_name>)
"""

import os
import click
from .prd import PRD

@click.group()
def main():
    pass

@click.command()
@click.argument('folder_name', required=False, default='sections')
def init(folder_name):
    try:
        os.makedirs(folder_name, exist_ok=True)
        print(f'Folder "{folder_name}" created successfully.')
    except Exception as e:
        print(f'Error creating folder "{folder_name}": {e}')
        return

    prd = PRD(folder_name)
    prd.generate_section_files()

@click.command()
@click.argument('folder_name', required=False, default='sections')
@click.option('--team', required=True, type=click.IntRange(1, 25), help='Team Number (between 1 and 25)')
def generate(folder_name, team):
    prd = PRD(folder_name)
    try:
        pdf_name = f"Team_{team}_prd.pdf"
        prd.compile_to_pdf_from_folder(folder_name=folder_name, output_file=pdf_name)
    except FileNotFoundError:
        print(f"Error: The folder '{folder_name}' does not exist. Please specify a valid folder name.")

main.add_command(init)
main.add_command(generate)

if __name__ == '__main__':
    main()
