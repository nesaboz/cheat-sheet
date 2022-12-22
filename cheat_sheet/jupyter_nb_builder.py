"""
Run this file to build all jupyter notebooks from markdown files:
- find out all the folders in the nbs folder
- These will be all jupyter notebook files, let's make it in alphabetical order
- for each we then read the markdown file, and build a jupyter note
"""
import json
from pathlib import Path

nbs_path = Path('/Users/nenad.bozinovic/cheat-sheet/nbs')
subfolders = [x for x in list(nbs_path.iterdir()) if (x.is_dir() and x.name[0] != '.')]

def get_title_and_lines(md_file: Path) -> (str, list):
    """
    Opens a md_file and gets the name and all the lines.
    """

    title = (md_file.name.split('.')[0]).replace('_', ' ').capitalize()

    with open(md_file, 'r') as f:
        lines = f.readlines()

    return title, lines


def get_json_from_md(name, md_files, output_path):
    """
    jupyter notebook is basically json, that consists of 4 cells.
    """

    # very likely not needed
    # show_doc_import_cell =   {
    #    "cell_type": "code",
    #    "metadata": {},
    #    "outputs": [],
    #    "source": [
    #     "#| hide\n",
    #     "from nbdev.showdoc import *"
    #    ]
    #   },

    initial_cell = {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"# {name}"
        ]
    }
    cells = [initial_cell]
    for md_file in md_files:
        title, lines = get_title_and_lines(md_file)

        title_cell = {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"## {title}"
            ]
        }

        lines_cell = {
            "cell_type": "markdown",
            "metadata": {},
            "source": lines
        }

        cells.extend([title_cell, lines_cell])

    output = {
        "cells": cells,
        "metadata": {"kernelspec": {
                           "display_name": "Python 3 (ipykernel)",
                           "language": "python",
                           "name": "python3"
                       }},
        "nbformat": 4,
        "nbformat_minor": 4
    }

    with output_path.open('w') as f:
        json.dump(output, f, indent=1)  # TODO maybe add extra line to the ipynb? or run nbdev_clean


for i, subfolder in enumerate(subfolders):
    md_files = list(subfolder.glob('*.md'))
    name = subfolder.name
    output_file = f"{i:02d}_{name}.ipynb"
    get_json_from_md(name, md_files, nbs_path / output_file)
    print(f"Built {output_file}.")
