If making shell file make sure it has correct line endings for the system, in PyCharm go to File -> File Properties -> Line Separators  
- go to GitHub and create a new repo with name 
- go to the PyCharmProject folder  
- update conda and init bash for new version of conda  
```zsh
conda update -n base -c conda-forge conda  
```

```zsh
conda init zsh  # Must restart terminal if running this one.
```

```zsh
$repo_name = <enter repo name here>
$python_ver = 3.10
yes | conda create -n $repo_name python=$python_ver
conda activate $repo_name  
```

```zsh
chmod +x utils/setup_new_project.sh check with ls -l 
./utils/setup_new_project.sh <repo_name> <python_version>
# for example ./setup_new_project.sh test_repo 3.10 
```

To create a folder:
```
mkdir $repo_name  
```

```zsh
cd $repo_name || exit  
```

Install packages:
```zsh
pip install -U numpy pandas matplotlib torchviz scikit-learn tensorboard torchvision torch tqdm torch-lr-finder  
yes | conda install -c conda-forge jupyter_contrib_nbextensions graphviz python-graphviz 
```

Add a kernel:
```zsh
ipython kernel install --name $repo_name --user  
```

Git:

```zsh
echo $repo_name >> README.md  
git config --global init.defaultBranch main  
git init 
git add .  
git commit -m "first commit"  
git branch -M main  
remote_name=git@github.com:nesaboz/$repo_name.git  
git remote add origin $remote_name  
git push -u origin main
```

```
jupyter notebook --generate-config  
```

Change the default kernel by modifying and uncommenting in jupyter config file following line:  `c.MultiKernelManager.default_kernel_name='newDefault' \n"`

Add jupyter notebook extensions `collapsable headings` and `table of context 2 (toc2)`