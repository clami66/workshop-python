# Setting up your system for the course

You need to have done the following setup on your laptop before the course starts.
Given the prerequisites, you should typically be fine doing this by yourself,
but if you run into unexpected problems, send me an e-mail or come by the office.

**NB:** If you don't have the permissions to install software on your laptop,
you must ask your system administrator to either give you such premissions or
install the software for you. This will require extra time so please plan ahead for this!

## Terminal setup

* Unix, Linux and MacOSX already have a terminal app installed:
  on MacOSX, you can find it by searching for "Terminal" in the launch pad.
* On Windows, you may use, e.g., PowerShell or cmd.
  In general, I am not good at using Windows, so my support there might be lacking.


## Conda setup

### 1. Download and install Conda and Mamba

Start by installing Miniconda..

<details>
  <summary>On Mac OS X</summary>

First, make sure you have Xcode and CommandLineTools installed
and updated to latest version (in AppStore). If you have not already
installed CommadLineTools, go to a terminal window and run:

`$ xcode-select --install`

Second, download the latest version of Miniconda3 and run it to install.

`$ curl -o Miniconda3-latest-MacOSX-x86_64.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh`

`$ sh Miniconda3-latest-MacOSX-x86_64.sh`

Follow the instructions on screen, scrolling down,
pressing ENTER and replying yes when necessary.
Install it in the default directory. Restart your terminal
window to apply modifications. After restarting, you can type
the command below to install Mamba:

`$ conda init`

`$ conda install -n base -c conda-forge mamba`
    
</details>

<details>
  <summary>On Ubuntu</summary>

First download the latest version of Miniconda3 and run it to install.

`$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`

`$ sh Miniconda3-latest-Linux-x86_64.sh`

Follow the instructions on screen replying yes when necessary.
Restart your terminal window to apply modifications.
After restarting, you can type the command below to install Mamba:

`$ conda init`

`$ conda install -n base -c conda-forge mamba`

</details>

<details>
  <summary>On Windows 10</summary>

Unfortunately, not all packages available on conda are compatible
with windows machines. The good news is that Windows 10 offers
native linux support via the Windows Subsystem for Linux (WSL2).
This allows you to run linux/bash commands from within windows without
the need of a virtual machine nor a dual-boot setup (i.e. having
2 operating systems). However, WSL does not offer a complete support
for graphical interfaces, so we need additional steps to make that happen.

On Windows 10, install the WSL if you don’t have it.
Follow the instructions [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10)


Once you have that installed, you can [download and install MobaXterm](https://mobaxterm.mobatek.net)
(which is the enhanced terminal with graphical capacity).
It is recommended that you INSTALL the program and not use the portable version.

Inside MobaXterm, you will probably will see that your WSL
is already listed on the left panel as an available connection.
Just double-click it and you will be accessing it via MobaXterm.
If by any chance you don’t see it there, close MobaXterm and go
to the WSL terminal, because probably the WSL is not allowing
SSH connections. You can follow this link for the instructions
on how to do it. You need to complete until the step Start or
restart the SSH service, while the further steps are optional,
but might be useful.

Inside MobaXterm, download Conda with the command:

`$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`

Inside MobaXterm, type the commands below to install Conda.
Follow the instructions for the installation there.

`$ cd ~/Downloads`

`$ sh Miniconda3-latest-Linux-x86_64.sh`

Inside MobaXterm, Follow the instructions on screen replying
yes when necessary. Restart your terminal window to apply modifications.
After restarting, you can type the command below to install Mamba:

`$ conda init`

`$ conda install -n base -c conda-forge mamba`

Inside MobaXterm, type the commands below to install the
X-server graphical [packages that are needed](https://docs.anaconda.com/anaconda/install/linux/).

`$ sudo apt-get update`

`$ sudo apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6`

Close and open all application and Inside MobaXterm,
you will probably will see that your WSL is already listed
on the left panel as an available connection.
Just double-click it and you will be accessing it via MobaXterm.
    
</details>

### 2. Create a conda environment from file

To download the your_environment.yml file using the command on Terminal:

<details>
  <summary>On Mac OS or Linux</summary>
  
  `$ curl -o environment.yaml https://raw.githubusercontent.com/clami66/workshop-python/1ac6e4db2764551671e363763dd47d97d06fa821/precourse/environment-mac.yml`

</details>

<details>
  <summary>On Windows</summary>
  
`$ curl -o environment.yaml https://raw.githubusercontent.com/clami66/workshop-python/0422/precourse/environment-win.yml`

</details>

After this, you should have a file named `environment.yaml`
in your directory (it does not matter where). Next, type:

`$ mamba env create -f environment.yaml`

This will install an environment called `workshop`
containing all the necessary packages and tools.

Several messages will show up on your screen and will tell you about
the installation process. This may take a few minutes depending
on how many packages are to be installed.

```
##...
##Downloading and Extracting Packages
##cachetools-4.2.4     | 12 KB     | ############################################## | 100%
##pydot-1.4.2          | 43 KB     | ############################################## | 100%
##argcomplete-1.12.3   | 34 KB     | ############################################## | 100%
##...
##Preparing transaction: done
##Verifying transaction: done
##Executing transaction: done
##...
##done
#
# To activate this environment, use
#
#     $ conda activate workshop
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

### 3. Activate the environment

Once the environment is created, we need to activate it in order to use
the softwares and packages inside it. To activate an environment type:

`$ conda activate workshop`

From this point on you can run any of the contents from the workshop.
For instance, you can directly launch Jupyter Notebooks by typing

`$ jupyter-notebook`
