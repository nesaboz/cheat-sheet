There are many shells one can use, Mac default is `zsh` (located at `/bin/zsh`). I set up PyCharm to use it as well in the `Preferences\Tools\Terminal\Shell Path`

Bash/zsh comment is the same as python: `#`

```zsh
# To open Pycharm from terminal:
open -na "PyCharm.app" .
# To open a finder from terminal:
open .
```

To open terminal from folder I added a shortcut:
`Control + Alt + Shift + T`

To see hidden files on Mac in finder: `Command + Shift + .`

## Count files

To [count files](https://devconnected.com/how-to-count-files-in-directory-on-linux/) in a folder from terminal:
```zsh
ls /etc | wc -l
```
recursively:
```
find <directory> -type f | wc -l
```

for example:
```
ls '/Users/nenad.bozinovic/work/Frame/elasticity_logs' | head -4
```

## Zip/Unzip

To [zip/unzip gz](https://www.cyberciti.biz/faq/unpacking-or-uncompressing-gz-files/):

```zsh
zip -d filename.gz  # unzip filename
gzip filename  # zip it back
gzip -k filename  # to zip it and keep original
```

## Download

To download a file from URL:
```zsh
!curl -OL <URL>
```

## Paths

Print path:

```zsh
echo "${PATH//:/$'\n'}"
```

[To add folder to PATH](https://www.cyberciti.biz/faq/appleosx-bash-unix-change-set-path-environment-variable/)


## Homebrew

[Homebrew](https://brew.sh/) is a package manager for macOS, it might have some unique packages that pip doesn't have, to install `wget` for example:

```zsh
brew install wget
wget https://your.link.png
```

## pip

To install package:
```zsh
pip install torch torchvision tensorboard
```

When using `[]` with `pip` it is important to use `""` to avoid shell parsing for example:
```zsh
pip install "mpl_interactions[jupyter]"
```

## vim


| Command | Explanation |
| -| - | 
| `i`  |      insert mode |
| `:w`  |   Saves the file you are working on | 
| `:w [filename]` | Allows you to save your file with the name you've defined |
| `:wq` | Save your file and close Vim |
| `:q!` | Quit without first saving the file you were working on |

## Conda

```
yes | conda create -n $repo_name python=$python_ver  # notice there is no keyword env
conda env list
conda env remove -n ENV_NAME
conda env export > env.yml
conda env create -n ENVNAME --file ENV.yml
```


## if statement in zsh

```zsh
if ! [[ -n $repo_name ]] || ! [[ -n $python_ver ]]; then  
  echo "you didn't enter repo name and/or python version"  
  exit 0  
fi
```
