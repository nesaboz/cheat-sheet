
To install fastai project on any linux machine (more [here](https://github.com/fastai/fastsetup), also see [docs](https://docs.fast.ai/)):

```zsh
sudo apt update && sudo apt -y install git
git clone https://github.com/fastai/fastsetup.git
cd fastsetup
sudo ./ubuntu-initial.sh
```

wait a couple of minutes for reboot, then ssh back in:

```zsh
mamba install -c fastchan fastai
conda install -c fastchan nbdev
conda install -c anaconda pillow
conda install jupyter
pip install gradio
```

