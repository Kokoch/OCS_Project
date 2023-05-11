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
for t in {1..3};
do  
    for s in {1..4};
    do
        for i in {1..5000}; 
        do  
            
            range=$((1 + $RANDOM % 1000));
    
            perf stat -a -e "power/energy-pkg/","power/energy-ram/","cpu/cache-misses/" -o ./python/outputs/perf_output${i}.txt  python ./python/matrix.py ${s} $range ${t}
            # python matrix_gen.py ${s} $range ${t} | perf stat -a -e "power/energy-pkg/","power/energy-ram/","cpu/cache-misses/" -o ./python/outputs/perf_output${i}.txt  python ./python/matrix_op.py -
            python data_write_unique.py ${s} $range ${t} $language ${i}
            
        done
        # Adds the parameter in the perf output files
        cd ./python/outputs/
        #python data_write.py $size $range $type 

        # Moves to the following directory to run the dataset composition
        python to_csv.py ${t} ${s}
        rm perf_output*.txt

        cd ..
        cd ..
    done
done

