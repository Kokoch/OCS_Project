#! /bin/bash -l
#SBATCH --ntasks-per-node=1
#SBATCH -N 1
#SBATCH -c 1
#SBATCH --time=0-01:55:00
#SBATCH -p batch
#SBATCH --reservation=opti_project

# Begins a timer
start=`date +%s`

# Computes the energy consumed during the NN training
source venv/bin/activate

# Variables
filenumber=0;
# range=10;
# type=int;

# Iterates through the parameters and computes for each the energy cost.

# For each Epochs
for t in {1..4};
do  
    # This gives a value of 5, 10, 25, 50 
    epochs=$((5*$t))

    # For each Batch Size
    for s in {1..4}; 
    do
        # This gives S, which represents the batch size, a value of 32, 64, 128, 256.
        s=$(($s+4))
        batch_size=$((2**$s))

        # For each PARAM 3
        for i in {1..4}; 
        do  
            # This gives S, which represents the learning rate, a value of 10, 100, 1000 or 10000.
            learning_rate=$((10**$i))
	    filenumber=$(($filenumber+1))
            perf stat -a -e "power/energy-pkg/","power/energy-ram/","cpu/cache-misses/" -o ./NNergy/outputs/perf_output${filenumber}.txt  python3 ocs_project_NN_optimization.py ${epochs} ${batch_size} ${learning_rate} ${filenumber}
            python3 data_write_NN.py ${epochs} ${batch_size} ${learning_rate} ${filenumber} 
            
        done

        # Adds the parameter in the perf output files
        cd ./NNergy/outputs/
        #python data_write.py $size $range $type 

        # Moves to the following directory to run the dataset composition
        python3 NN_to_csv.py
        rm perf_output*.txt
	rm NN_loss*
        cd ..
        cd ..
    done
done


# Ends the timer measurement
end=`date +%s`
runtime=$((end-start))
echo "Execution time (in seconds)"
echo $runtime
