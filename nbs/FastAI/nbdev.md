```zsh
nbdev_help  # this list all commands 
```

Tutorial says we might need to also run the following after export once: `pip install -e .`
 (-e installs a project in editable mode (i.e. setuptools "develop mode") from a local project path (.))

| Command | Action | 
| - | - |
| `nbdev_prepare` | use it before commit and push, it will run all the code though | 
| `nbdev_update` | propagates changes from python to jupyter | 
| `nbdev_preview` | to see pages, and this one is live | 
| `nbdev_export` | will export all cells with `#export` flag into a filename defined in the top using <code>#&vert; default_exp filename</code> |

One can also export from jupyter notebook:

``` jupyter
from nbdev import nbdev_export
nbdev_export()
```
