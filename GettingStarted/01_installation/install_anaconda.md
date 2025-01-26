## Installing Python3

### 1. Anaconda Navigator
We will install Python3 via Anaconda Navigator.
To install Anaconda Navigator
Go here

[https://docs.anaconda.com/free/anaconda/install](https://docs.anaconda.com/free/anaconda/install)

Select your operating system by clicking one of

- Installing on Windows
- Installing on macOS

Select
"Download the Anaconda installer."


### 2. Create an environment for this course

We will use several Python packages.
We will bundle these into something called an "environment".

- Within Anaconda Navigator select "Environment" (on the left panel)
- Select "Create" 
- Name the environment `nummeth_2025`
- Use the default python version

When the environment has been created

- Click the "play" button
(looks like a solid / filled right pointing arrowhead)
- Select "Open Terminal"
- When the terminal pops up, type the following commands one-by-one.

```
conda install numpy
conda install scipy
conda install matplotlib
conda install sympy
```

Each `conda install` line may prompt you for a response. Answer `y` to all questions.

### 3. Install Anaconda applications

- Within Anaconda Navigator select "Home" (on the left panel)
- In the bar at the top, make sure it says
"All applications" on "nummeth_2025"
- Find the JupyterLab application, select "Install"
