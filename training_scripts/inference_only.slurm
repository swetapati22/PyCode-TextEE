#!/bin/bash
#SBATCH --partition=gpuq                    # the DGX only belongs in the 'gpu'  partition
#SBATCH --qos=gpu                           # need to select 'gpu' QoS
#SBATCH --job-name=richere_test_without_guideline_wo_NS
## Separate output and error messages into 2 files.
## NOTE: %u=userID, %x=jobName, %N=nodeID, %j=jobID
#SBATCH --output=train_completion_output_richere_test_without_guideline_wo_NS.log  # Output file
#SBATCH --error=train_completion_output_richere_test_without_guideline_wo_NS.log   # Error file
## Slurm can send you updates via email
#SBATCH --mail-type=ALL         # ALL,NONE,BEGIN,END,FAIL,REQUEUE,..
#SBATCH --mail-user=spati@gmu.edu     # Put your GMU email address here
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1                 # up to 128; 
#SBATCH --gres=gpu:A100.80gb:1              # up to 8; only request what you need
#SBATCH --mem=200GB                 # memory per CORE; total memory is 1 TB (1,000,000 MB)
#SBATCH --export=ALL 
#SBATCH --time=4-23:59:59                   # set to 1hr; please choose carefully; 10hrs

source activate unsloth_env                     # Activate your Conda environment

# Navigate to the script directory
cd /scratch/spati/tmp/LLaMA

# Run the script
echo "Starting training at $(date) on $(hostname)"
python inference_only.py > output_richere_test_without_guideline_wo_NS.log 2>&1

echo "Training completed at $(date)"

