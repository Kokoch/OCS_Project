#! /bin/bash -l
#SBATCH --ntasks-per-node=1
#SBATCH -N 1
#SBATCH -c 1
#SBATCH --time=0-00:05:00
#SBATCH -p batch
#SBATCH --reservation=opti_project

# Variables
language=python;
# size=10;
# range=10;
# type=int;

# Matrix generation, can pass arguments after
# matrix=python ./python/matrix_gen.py $size $range $type;

# Iterates 10 times through the program and computes for each the energy cost
for i in {1..10};
do  
    size=$((1 + $RANDOM % 100));
    range=$((1 + $RANDOM % 1000));
    type=$((1 + $RANDOM % 3));
    perf stat -a -e "power/energy-pkg/","power/energy-ram/","cpu/cache-misses/" -o ./python/outputs/perf_output${i}.txt  python ./python/matrix.py $size $range $type
    python data_write_unique.py $size $range $type $language ${i}
done

# Adds the parameter in the perf output files
cd ./python/outputs/
#python data_write.py $size $range $type 

# Moves to the following directory to run the dataset composition
python to_csv.py