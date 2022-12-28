
from tqdm import tqdm 
from  time import sleep


def ft_progress(lst):
    for i in tqdm(lst):
        yield i





isty = range(1000000000)
ret = 0
for elem in ft_progress(isty):
    ret += (elem + 3) % 5
    # sleep(0.001)
print()
print(ret)


# MYPATH="/goinfre/$USER/miniconda3"
# curl -LO "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"
# sh Miniconda3-latest-MacOSX-x86_64.sh -b -p $MYPATH
# $MYPATH/bin/conda init zsh
# $MYPATH/bin/conda config --set auto_activate_base false
# source ~/.zshrc
# conda create --name 42AI-$USER python=3.7 jupyter pandas pycodestyle numpy; y
