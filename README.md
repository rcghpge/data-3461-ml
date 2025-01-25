# Machine Learning @ UTA
Machine Learning @ UTA. Dr. Jawad. Spring 2025

---
## Lab
Labs section of the course.

## Development Environment Setup
To run an initial Python development environment there are several methods via Jupyter notebooks, VS Code, PyCharm, Spyder, the Anaconda distribution, or on the command line in Bash. For beginner-friendly, Jupyter Notebooks or Anaconda is recommended for a seamless development and workflow environment.

---
## Getting Started
To get started see Github documentation to install this repository into your local machine: [Cloning a Repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository?platform=linux&tool=webui)

## Python Development Workflow in Bash
### Install Python
If not using Anaconda, install Python directly in Bash:
```bash
# Install Python
sudo apt install python3

# Install pip package manager
sudo apt install python3-pip
```

Run a Python Interactive Shell:
```bash
python3
```

You can run Python scripts directly in Bash:
```bash
# Create a Python script
nano hello.py

# Run Python script
python3 hello.py
```

For package management and virtual environments:
```bash
# Create a virtual environment
python3 -m venv ml-env

# Activate virtual environment
source ml-env/bin/activate

# Install Python libraries
pip install numpy pandas scikit-learn matplotlib seaborn jupyter
```

---
## Anaconda Development Workflow Setup
Anaconda is a distribution stack for Python and R, designed for data science and machine learning. It includes Spyder, Jupyter, and pre-installed libraries.

1.  Download and install Anaconda from [Anaconda Downloads](https://www.anaconda.com/download)
2.	Launch the Anaconda Navigator GUI for managing environments and tools.

### Create an Environment in Anaconda:
```bash
# Create interactive environment
conda create -n ml-env python=3.9

# Activate the environment
conda activate ml-env

# Install required packages
conda install numpy pandas scikit-learn matplotlib seaborn jupyter
```

### Run Spyder or Jupyter:
- Open Spyder: Launch from the Anaconda Navigator or run Spyder in the terminal.
- Run Jupyter Notebook: Launch from Navigator or run the following command in Bash:
```bash
jupyter notebook
```

---
## Resources and Documentation
- [Anaconda](https://www.anaconda.com): Python and R distribution for data science.
- [Spyder](https://www.spyder-ide.org): Scientific Python IDE.
- [Visual Studio Code](https://code.visualstudio.com): Interactive Development Environment.
- [PyCharm](https://www.jetbrains.com/pycharm/): IDE for Python development.
- [Jupyter Notebooks](https://jupyter.org): Interactive notebooks for Python.
- [Python](https://www.python.org): The official Python website.
- [NumPy](https://numpy.org): Library for numerical computing.
- [Pandas](https://pandas.pydata.org): Library for data manipulation and analysis.
- [Scikit-Learn](https://scikit-learn.org/stable/): Library for machine learning.
- [Matplotlib](https://matplotlib.org): Library for data visualization.
- [Seaborn](https://seaborn.pydata.org): Statistical data visualization library

---
