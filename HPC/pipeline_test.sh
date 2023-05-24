#! /bin/bash -l
#SBATCH --ntasks-per-node=1
#SBATCH -N 1
#SBATCH -c 1
#SBATCH --time=0-01:55:00
#SBATCH -p batch
#SBATCH --reservation=opti_project

# Times the total execution time of the script
start=`date +%s`

# Variables
language=python;
# size=10;
# range=10;
# type=int;

# Matrix generation, can pass arguments after
# matrix=python ./python/matrix_gen.py $size $range $type;

# Iterates and computes for each the energy cost

# For each type (int, neg, float)
for t in {1..3};
do  
    for s in {1..2};
    do
        for i in {1..10}; 
        do  
            # Chooses a random range of values
            range=$((1 + $RANDOM % 1000));
    
            #perf stat -a -e "power/energy-pkg/","power/energy-ram/","cpu/cache-misses/" -o ./python/outputs/perf_output${i}.txt  python ./python/matrix.py ${s} $range ${t}
            matrix=$(python ./python/matrix_gen.py ${s} $range ${t} | sed 's/[[:space:]]//g')
            perf stat -a -e "power/energy-pkg/","power/energy-ram/","cpu/cache-misses/" -o ./python/outputs/perf_output${i}.txt  python ./python/matrix_op.py $matrix
            python data_write_unique.py ${s} $range ${t} $language ${i}
            
        done
        # Adds the parameter in the perf output files
        cd ./python/outputs/
        #python data_write.py $size $range $type 

        # Moves to the following directory to run the dataset composition
        python3 to_csv.py ${t} $size
        rm perf_output*.txt

        cd ..
        cd ..
    done
done

end=`date +%s`
runtime=$((end-start))
echo "Execution time (in seconds)"
echo $runtime
