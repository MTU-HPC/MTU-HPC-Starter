# MTU-HPC-Starter
Repository for tutorials, examples and starter scripts for using the MTU HPC cluster

## Connecting to the MTU HPC cluster

Within the college, access to the cluster is via SSH to the host: 

    com-gpu-cluster.cit.ie

On Windows the simplest way to get an SSH client is to use PuTTy. This is available on all lab PCs.

Linux machines usually have an SSH client on the terminal.

An account on the MTU HPC cluster is usually requested for you by your lecturer or supervisor. 

## Setup git 

### Get the Starter Repository using git:

This repository contains some useful sample code for running and submitting jobs on the MTU HPC cluster. This repo can be cloned into your home directory on the HPC cluster and used as a starting point for some your own work. 

Once logged into the cluster, use the command at the root of your home directory:

    git clone https://github.com/MTU-HPC/MTU-HPC-Starter.git

This will download some basic scripts for getting started with your own projects on thr MTU HPC. Git pull from this repo sometimes as it will be updated with new examples as needed.

---

## Using Miniconda for Python.

THe MTU HPC cluster has a number of versions of Python, Tensorflow and other libraries needed for ML scripts. However, it is dificult to maintain Python libraries and versions systemwide that suit everyone. 

To help with this and provide options for users, we have installed Miniconda systemwide. Miniconda allows users to install multiple Python versions and Python libraries in their own separate "environments". This can be done without needing administrator permissions. 


## Creating and activating conda environments for running python scripts 

To use Miniconda, you should have a ".condarc" file at the root of your Home directory. At a minimum it should have the text listed below. 

.condarc:

```
env_prompt: '({name})'
auto_activate_base: false
channels:
  - conda-forge
  - bioconda
  - defaults
```

The .condarc file tells Miniconda/conda to:

* env_prompt  --- put the name of your currently active conda environment at the front of your command prompt
* auto_activate_base --- When you login to your cluster account, it will **not** automatically put you in the base conda environment.
* channels --- The web repo/location **conda install <package>** will install Python and Python packages from. "conda-forge" has many ML/AI/Data Analytics packages available.  

To see if you already have the **.condarc** file, type at the commandline:

    ls -la

to get a list of files in your home directory. If **.condarc** is not there, it can be created using the "nano" text editor:

    nano .condarc

and copy and paste the text above into **.condarc**.

## One-time only: Initialise **conda** in your account

To use conda, it must be "initialised" once before it can be used. 

To initialise conda, run the following command:

    conda init

You will need to **exit** your SSH session and reconnect for **conda** to be ready for use. This does not need to be done again. 

## Create a conda environement for running code

To create a **conda** environment type the following at the commandline:

    conda create --name my_python3_env python=3.8

This create an environemnt called "my_python3_env" and it will install Python 3.8 into that environment. If you don't specify the version of Python, it will install the latest version it can find.

To see your environmensts type:

    conda env list

This will should show you 2 environemts now:

* the **base** environment
* **my_python3_env** - the one we just created. The name is whatever you wish it to be.

At this stage, we have *created* an envrionment, but we are not *using* it yet.

## Activating a **conda** environment

Before anything else, type: 
     
     python --version 

This should show you Python 2.7 or some such old Python. This is because the "system" Python is version 2.7. Running a Python script from the commandline now would need the Python script to be compatible with that old version. We cannot upgrade the **system** python because the operating system itself relies  on old Python scripts.

Activate your new conda environment with:
 
     conda activate my_python3_env

Now run python --version again. The version is now something like Python 3.8. After activating the conda environemnt, we are now using the version of Python you have installed. We are also using the Python packages that are *inside* this new environment.

## Adding packages to a conda enironment

When you are in a "conda" environemt (i.e. the environemnt is "active") the start of your command propmt should show the name of the environment:

    (my_python3_env) username@com-gpu-cluster ~]$

To install something like "matplotlib", use conda to **install** it:

     conda install matplotlib yaml 

That last command will try to install the 2 packages "matplotlib" and "yaml" into the current active conda environment.

## Managing conda environments

If you have 5 programs that use matplotlib and Python 3.8, they can all use the same conda environment. There is no need to create a new environment for every program or script. 

If, however, you need to run a library which only works on Python 3.6 or needs very different packages to your *main* environment, you could create a new conda environment for running those scripts:

    conda create --name biology_python_env python=3.6
    conda activate biology_python_env
    conda install <random biology python packages here>

## Deactivating conda environment

When you are finished, or you wish to use a different conda environment you can exit from the conda environemnt thus:

    conda deactivate


