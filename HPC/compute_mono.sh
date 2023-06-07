#! /bin/bash -l
#SBATCH --ntasks-per-node=1
#SBATCH -N 1
#SBATCH -c 1
#SBATCH --time=0-00:15:00
#SBATCH -p batch
#SBATCH --reservation=opti_project

# Variables
language=python;
size=10000;
range=1000;
type=3;

perf stat -a -e "power/energy-pkg/","power/energy-ram/","cpu/cache-misses/" -o ./python/outputs/perf_output${i}.txt  python ./python/matrix.py $size $range $type
