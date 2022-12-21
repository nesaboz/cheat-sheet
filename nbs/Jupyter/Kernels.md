```
# list kernels
jupyter kernelspec list

# remove kernel
jupyter kernelspec remove <kernel-name>  

# install new kernel
ipython kernel install --name <local-venv> --user
```

To manipulate jupyter kernels (Note: I did experience an issue with `sys.path` was different in python env and jupyter kernel. The solution that worked is [here](https://stackoverflow.com/questions/34389029/cannot-import-modules-in-jupyter-notebook-wrong-sys-path), in short, one has to compare the `sys.executable` for both the environment AND jupyter kernel (this one is listed using `jupyter kernelspec list` and looking into relevant `kernel.json` file)
a must-read that I still need to go over is here [here](https://stackoverflow.com/questions/897792/where-is-pythons-sys-path-initialized-from).
