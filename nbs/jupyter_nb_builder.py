"""
Run this file to build all jupyter notebooks from markdown files:
- find out all the folders in the nbs folder
- These will be all jupyter notebook files, let's make it in alphabetical order
- for each we then read the markdown file, and build a jupyter note
"""
import json
from pathlib import Path


def get_title_and_lines(md_file: Path) -> (str, str, list):
    """
    Opens a md_file and gets the name and all the lines.
    """

    file_title = md_file.name.split('.')[0]
    title = file_title.replace('_', ' ')
    # title = title[0].capitalize() + title[1:]

    with open(md_file, 'r') as f:
        lines = f.readlines()

    return file_title, title, lines


def get_json_from_md(subfolder: Path):
    """
    jupyter notebook is basically json, that consists of 4 cells.
    """

    md_files = list(subfolder.glob('*.md'))

    for md_file in md_files:

        output_file_name, title, lines = get_title_and_lines(md_file)

        initial_cell = {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"# {title}"
            ]
        }

        lines_cell = {
            "cell_type": "markdown",
            "metadata": {},
            "source": lines
        }

        output = {
            "cells": [initial_cell, lines_cell],
            "metadata": {"kernelspec": {
                               "display_name": "Python 3 (ipykernel)",
                               "language": "python",
                               "name": "python3"
                           }},
            "nbformat": 4,
            "nbformat_minor": 4
        }
        output_file_path = subfolder / f"{output_file_name}.ipynb"
        with output_file_path.open('w') as f:
            json.dump(output, f, indent=1)
            f.write('\n')  # adding new line here only for some weird quirk to pass CI worklfow (in .github/workflows/test.yaml)

        print(f"Built {output_file_path}.")


nbs_path = Path(__file__).parent
subfolders = [x for x in list(nbs_path.iterdir()) if (x.is_dir() and x.name[0] != '.')]
for subfolder in subfolders:
    get_json_from_md(subfolder)



