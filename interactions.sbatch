#!/bin/bash
#SBATCH --job-name=interact_proteins
#SBATCH --output=interact_proteins_%j.out
#SBATCH --error=interact_proteins_%j.err
#SBATCH --nodes=1
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:a100:1
#SBATCH --mem=64GB
#SBATCH --time=20:00:00

singularity run --nv --bind $(pwd):/app:rw chai-container.sif
