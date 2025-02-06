# megaAnalytics
Analytics at Mega

This repository is used for all exploratory analysis to be done at GetMega.

## Guidelines
In order to keep the repository clean, we utilize two major additions to our version control system.
1. DVC: Data Version Control
2. JupyText: Effective version control for `.ipynb` files

### DVC
DVC version controls the dataset that you working with along with the Git version controlling of the code that you are working on.
This helps a lot in reproducing models and model outputs from any point in time.
Please read the source materials provided by [DVC Website](https://dvc.org) to get accustomed to the philosophy of this product and how it should be used.

For any questions regarding this, check the internal StackOverflow or ask among the members of the data science chapter.

#### Setting up a new project folder
Steps:
1. Create a new folder for the project you want to start working on.
2. Navigate to the created folder in terminal and run the following command:
```
dvc init --subdir
```
3. `data-science-mega` is the bucket in which we store the data files on GCS. Add the name of the folder(or a similar name) you created in the command below and execute it:
```
dvc remote add -d myremote gs://data-science-mega/folder-name
```
4. Run the following commands to upload the data files on GCP:
```
dvc add file-path
dvc push
```

Note:
If you're unable to upload the files on GCP because of authentication error, run the following commands in a separate terminal:
```
gcloud auth login
gcloud auth application-default login
```

#### Protocol
The protocol we will follow with DVC is that we will have a single DVC for each project. Hence, all the relevant data is always in the same version tree. At the same time, all the data that is completely unrelated is not forcefully downloaded for every person.

### JupyText
Jupytext allows Jupyter to open and save notebooks(`.ipynb` files) as text files(`.py` files). Once we associate a notebook with a `.py` file, only the code blocks will be version controlled, not the output of the cells.
The generated python file needs to be committed and the notebook will be ignored by Git.
Read the source materials provided by [https://jupytext.readthedocs.io/en/latest/] to know how it should be used.

Steps:
1. Open the Jupyter Notebook you want to work on.
2. Navigate File -> Jupytext -> enable "Pair Notebook with Percent Script" 
3. A `.py` file will be generated(might take up to 30 seconds), close the `.ipynb` file and open the python file; make your changes in the same and commit it.

## Setup
All the work in this repository is done in *Python 3*. So make sure that you use the same.
For this guide, we will be using `python3` and `pip3` commands to signify the same. You can change the command names according to your system.

It is recommended that you work in a virtual environment. It will make it easier to update the `requirements.txt` when you add a new python library to the project.

Here is the command to install virtual environment:
```
pip3 install virtualenv
```

Here are the commands to get started after cloning this repository:
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

At this point, all your python dependencies will start getting installed.
Once that is done, navigate to folder corresponding to the project that you are working in.
Each such folder should contain a `.dvc` folder in it. Run the following command to download the data corresponding to the project:
```
dvc pull
```
