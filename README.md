# MTU-HPC-Starter
Repository for tutorials, examples and starter scripts for using the MTU HPC cluster


## Setup git 

### Get the Starter Repository using git:
This brings in some sample code for running scripts on the cluster

Once logged into the cluster, use the command:

    git clone https://github.com/MTU-HPC/MTU-HPC-Starter.git

## Using Miniconda for Python.

## Creating and activating conda environments for running python scripts 


.condarc:

```
env_prompt: '({name})'
auto_activate_base: false
channels:
  - conda-forge
  - bioconda
  - defaults
```
