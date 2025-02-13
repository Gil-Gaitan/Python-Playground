# Setup Kaggle API
# pip install kaggle                        install kaggle
# kaggle --version                          check if installed
# GET YOUR API KEY FROM KAGGLE - go to profile -> account -> create new API token
# mkdir ~/.kaggle                           create a directory for the API key
# mv ~/Downloads/kaggle.json ~/.kaggle/     move the API key to the directory
# chmod 600 ~/.kaggle/kaggle.json           change permissions
# kaggle datasets list                      list all datasets
# kaggle datasets download -d uciml/iris    download dataset
# unzip iris.zip                            unzip the dataset
# GET PANDAS AND MATPLOTLIB - pandas is not installing on my mabcook so trying a vm here:
# python3 -m venv kaggle_env                create a virtual environment
# source kaggle_env/bin/activate            activate the virtual environment
# pip install pandas matplotlib            install pandas and matplotlib
# python -c "import pandas as pd; import matplotlib.pyplot as plt; print('Ready')"  check if installed