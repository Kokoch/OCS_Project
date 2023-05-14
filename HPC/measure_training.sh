#! /bin/bash -l
#SBATCH --ntasks-per-node=1
#SBATCH -N 1
#SBATCH -c 1
#SBATCH --time=0-01:30:00
#SBATCH -p batch
#SBATCH --reservation=opti_project

# Computes the energy consumed during the NN training
perf stat -a -e "power/energy-pkg/","power/energy-ram/","cpu/cache-misses/" -o ./python/perf_mearsurement_NN.txt  python ./python/ocs_project_NN.py