#!/bin/bash

#SBATCH --nodes=1
#SBATCH --partition=photonq-GPU
#SBATCH --ntasks=8
#SBATCH --mem 48G
#SBATCH --time=08:00:00
#SBATCH --output=output.tf2_test.o
#SBATCH --error=error.tf2_test.e
#SBATCH --gres=gpu:1


### Load any modules needed to be run here ### 

module load shared
module load miniconda3/3.9.1

### Your code here ###
free -h

# Miniconda setup
source /cm/shared/apps/miniconda/miniconda3/etc/profile.d/conda.sh

# Activate the specific environment you want to use
conda activate my_python3_env

# The code you wish to run. In this case, 
# use python3 to run the script called "Tensorflow2.py"
python3 Tensorflow2.py