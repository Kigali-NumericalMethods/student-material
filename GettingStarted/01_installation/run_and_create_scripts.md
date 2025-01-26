## Run and Create a Python Script

### 1. Start the Anaconda environment

- Within Anaconda Navigator select "Environment" (on the left panel)
- Select the environment nummeth_2025
- Click the "play" button
- Select "Open Terminal"

A terminal will pop up. The terminal may display something looking like this

#### Apple

```
. /opt/anaconda3/bin/activate && conda activate /opt/anaconda3/envs/nummeth_2025; 
(base) symgrad:~ % . /opt/anaconda3/bin/activate && conda activate /opt/anaconda3/envs/nummeth_2025; 
(nummeth_2025) symgrad:~ % 
```

Your may see something slightly different on your computer - that is normal. 

* The first item shown in parenthesis is the name of the environment. 
* `symgrad` is the name of my computer. 
* The directory you are located in by default should be `/Users/YOUR_USER_NAME`.


#### Windows

```
(nummeth_2025) C:\Users\dmay>
```

Your may see something slightly different on your computer - that is normal. 

* The first item shown in parenthesis is the name of the environment. 
* `dmay` is the name of my user account. 
* The directory you are located in by default should be `Users\YOUR_USER_NAME`.

--

Now you will need to navigate to your course work directory. 
You should have created this within the `Documents` directory.
To learn how to change directories to where you work is located, read Section 2.


### 2. Terminal basics and navigation

We have learnt to navigate the file system using `Finder` or `Explorer` (Windows). Now we have to learn how to move around the file system within the terminal.

Below is a table to basic commands you will require.

#### Apple

* `pwd` - Displays the name of the current directory
* `ls` - Lists the contents of the current directory (files and sub-directories)
* `cd DIRECTORY_NAME ` - Moves into the directory called `DIRECTORY_NAME`. An error will occur if a directory called `DIRECTORY_NAME` does not exist.
* `cd DIR1/DIR2 ` - Moves into the directory called `DIR1` and then moves again into directory `DIR2`. An error will occur if either `DIR1` or `DIR2` does not exist. You can also do `cd PATH` where path contains many sub-directory names seperated by a `/`. As before all sub-directories must exist.
* `cd ..` - Moves up a directory.
* `mkdir DIR_NAME` - Creates a new directory called `DIR_NAME`.


#### Windows
* `cd` - Displays the name of the current directory
* `dir` - Lists the contents of the current directory (files and sub-directories)
* `cd DIRECTORY_NAME` - Moves into the directory called `DIRECTORY_NAME`. An error will occur if a directory called `DIRECTORY_NAME` does not exist.
* `cd DIR1/DIR2 ` - Moves into the directory called `DIR1` and then moves again into directory `DIR2`. An error will occur if either `DIR1` or `DIR2` does not exist. You can also do `cd PATH` where path contains many sub-directory names seperated by a `\`. As before all sub-directories must exist.
* `cd ..` - Moves up a directory.
* `mkdir DIR_NAME` - Creates a new directory called `DIR_NAME`.


### 3. Execute a script

A Python script is any file which has the extension (`.py`). We will run a sample code I've provided called `welcome.py`. You can find this on GitHub.

Before trying to run `welcome.py`, check it is located in the current directory. Do this using the terminal command `ls` (Apple) or `dir` (Windows).

If the file `welcome.py` is displayed, you can run it by typing the following 

#### Apple

```
python3 welcome.py
```

#### Windows

```
Python welcome.py
```

In both cases, if the execution is successful you will see the following message displayed

```
Welcome to Python3. You have successfully ran your first Python script!
```

To run any other Python file, the process is the same.
Either do 
`python3 some_file.py`
or
`Python some_file.py` depending if you are on Apple or Windows.

 
 
### 5. Check your environment is working
Execute

```
python3 test_packages.py
```

or

```
Python test_packages.py
``` 
depending if you are on Apple or Windows.

Please note running this script may take several minutes.

Please verify that when you run the script windows pop up with graphs (you will need to close them for the test to continue) and that two PDF files are created. Inspect the PDFs created, you should see a 2D plot in `mplib_ex1.pdf` and a 3D plot in `mplot3d_ex1.pdf`.

### 6. Create and edit a new Python file
- Within Anaconda Navigator select "Home".
- Make sure the environment nummeth_2025 is selected.
- Launch the application "JupyterLab".
- Note that JupyterLab actually runs within your web browser.

To create a new Python file, do the following

1. Using the file viewer within JupyterLab, first navigate to the directory where you wish to create your file.
2. Click "File" from the top tool bar, and select "New Launcher".
3. On the right, under "Other", select "Python file".
4. Click "File" from the top tool bar, and select "Rename Python File". Enter the desired file name, make sure it ends with `.py`.
5. On the right you will see a text editer where you can enter your Python code. Save your work regularly.
