"""
Run this file to build all jupyter notebooks from markdown files:
- find out all the folders in the nbs folder
- These will be all jupyter notebook files, let's make it in alphabetical order
- for each we then read the markdown file, and build a jupyter note
"""
import json
import shutil
from pathlib import Path

nbs_path = Path('/Users/nenad.bozinovic/cheat-sheet/nbs')
subfolders = [x for x in list(nbs_path.iterdir()) if (x.is_dir() and x.name[0] != '.')]
print("\n".join(map(str, subfolders)))

subfolder = subfolders[0]
md_files = list(subfolder.glob('*.md'))

md_file = md_files[0]

def get_json_from_md(md_file, output_path):
    title = md_file.name.split('.')[0]

    # get a md_file as a
    with open(md_file, 'r') as f:
        lines = f.readlines()

    """
    jupyter notebook is basically json, that consists of 4 cells, 3 we can pre-configure:
    """
    title_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            f"# {title}"
        ]
    }

    show_doc_import_cell =   {
       "cell_type": "code",
       "metadata": {},
       "outputs": [],
       "source": [
        "#| hide\n",
        "from nbdev.showdoc import *"
       ]
      },

    lines_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": lines
    }

    output = {
        "cells": [
            title_cell,
            lines_cell
        ],
        "metadata": {"kernelspec": {
                           "display_name": "Python 3 (ipykernel)",
                           "language": "python",
                           "name": "python3"
                       }},
        "nbformat": 4,
        "nbformat_minor": 4
    }

    with output_path.open('w') as f:
        json.dump(output, f, indent=1)


get_json_from_md(md_file, nbs_path / "temp.json")
shutil.copy(nbs_path / "temp.json", nbs_path / "temp.ipynb")


"""
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Terminal"
   ]
  },

  {
   "cell_type": "code",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "There are many shells one can use, Mac default is `zsh` (located at `/bin/zsh`). I set up PyCharm to use it as well in the `Preferences\\Tools\\Terminal\\Shell Path`\n",
       "\n",
       "Bash/zsh comment is the same as python: `#`\n",
       "\n",
       "```zsh\n",
       "# To open Pycharm from terminal:\n",
       "open -na \"PyCharm.app\" .\n",
       "# To open a finder from terminal:\n",
       "open .\n",
       "```\n",
       "\n",
       "To open terminal from folder I added a shortcut:\n",
       "`Control + Alt + Shift + T`\n",
       "\n",
       "To see hidden files on Mac in finder: `Command + Shift + .`\n",
       "\n",
       "## Count files\n",
       "\n",
       "To [count files](https://devconnected.com/how-to-count-files-in-directory-on-linux/) in a folder from terminal:\n",
       "```zsh\n",
       "ls /etc | wc -l\n",
       "```\n",
       "recursively:\n",
       "```\n",
       "find <directory> -type f | wc -l\n",
       "```\n",
       "\n",
       "for example:\n",
       "```\n",
       "ls '/Users/nenad.bozinovic/work/Frame/elasticity_logs' | head -4\n",
       "```\n",
       "\n",
       "## Zip/Unzip\n",
       "\n",
       "To [zip/unzip gz](https://www.cyberciti.biz/faq/unpacking-or-uncompressing-gz-files/):\n",
       "\n",
       "```zsh\n",
       "zip -d filename.gz  # unzip filename\n",
       "gzip filename  # zip it back\n",
       "gzip -k filename  # to zip it and keep original\n",
       "```\n",
       "\n",
       "## Download\n",
       "\n",
       "To download a file from URL:\n",
       "```zsh\n",
       "!curl -OL <URL>\n",
       "```\n",
       "\n",
       "## Paths\n",
       "\n",
       "Print path:\n",
       "\n",
       "```zsh\n",
       "echo \"${PATH//:/$'\\n'}\"\n",
       "```\n",
       "\n",
       "[To add folder to PATH](https://www.cyberciti.biz/faq/appleosx-bash-unix-change-set-path-environment-variable/)\n",
       "\n",
       "\n",
       "## Homebrew\n",
       "\n",
       "[Homebrew](https://brew.sh/) is a package manager for macOS, it might have some unique packages that pip doesn't have, to install `wget` for example:\n",
       "\n",
       "```zsh\n",
       "brew install wget\n",
       "wget https://your.link.png\n",
       "```\n",
       "\n",
       "## pip\n",
       "\n",
       "To install package:\n",
       "```zsh\n",
       "pip install torch torchvision tensorboard\n",
       "```\n",
       "\n",
       "When using `[]` with `pip` it is important to use `\"\"` to avoid shell parsing for example:\n",
       "```zsh\n",
       "pip install \"mpl_interactions[jupyter]\"\n",
       "```\n",
       "\n",
       "## vim\n",
       "\n",
       "\n",
       "| Command | Explanation |\n",
       "| -| - | \n",
       "| `i`  |      insert mode |\n",
       "| `:w`  |   Saves the file you are working on | \n",
       "| `:w [filename]` | Allows you to save your file with the name you've defined |\n",
       "| `:wq` | Save your file and close Vim |\n",
       "| `:q!` | Quit without first saving the file you were working on |\n",
       "\n",
       "## Conda\n",
       "\n",
       "```\n",
       "yes | conda create -n $repo_name python=$python_ver  # notice there is no keyword env\n",
       "conda env list\n",
       "conda env remove -n ENV_NAME\n",
       "conda env export > env.yml\n",
       "conda env create -n ENVNAME --file ENV.yml\n",
       "```\n"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#| hide\n",
    "from IPython.display import Markdown, display\n",
    "display(Markdown(\"Terminal/zsh.md\"))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

#

# for line in lines:
# 	if line != '\n':
# 		temp.append(line)
# 	else:
# 		groups.append(temp)
# 		temp = []

"""


