from pathlib import Path

import numpy as np
import torch

from chai_lab.chai1 import run_inference

# We use fasta-like format for inputs.
# - each entity encodes protein, ligand, RNA or DNA
# - each entity is labeled with unique name;
# - ligands are encoded with SMILES; modified residues encoded like AAA(SEP)AAA

# Example given below, just modify it

# example_fasta = """
# >protein|name=example-of-long-protein
# AGSHSMRYFSTSVSRPGRGEPRFIAVGYVDDTQFVRFDSDAASPRGEPRAPWVEQEGPEYWDRETQKYKRQAQTDRVSLRNLRGYYNQSEAGSHTLQWMFGCDLGPDGRLLRGYDQSAYDGKDYIALNEDLRSWTAADTAAQITQRKWEAAREAEQRRAYLEGTCVEWLRRYLENGKETLQRAEHPKTHVTHHPVSDHEATLRCWALGFYPAEITLTWQWDGEDQTQDTELVETRPAGDGTFQKWAAVVVPSGEEQRYTCHVQHEGLPEPLTLRWEP
# >protein|name=example-of-short-protein
# AIQRTPKIQVYSRHPAENGKSNFLNCYVSGFHPSDIEVDLLKNGERIEKVEHSDLSFSKDWSFYLLYYTEFTPTEKDEYACRVNHVTLSQPKIVKWDRDM
# >protein|name=example-peptide
# GAAL
# >ligand|name=example-ligand-as-smiles
# CCCCCCCCCCCCCC(=O)O
# """.strip()

def infer(fasta_path):
    return run_inference(
        fasta_file=fasta_path,
        output_dir=output_dir,
        # 'default' setup
        num_trunk_recycles=3,
        num_diffn_timesteps=200,
        seed=42,
        device=torch.device("cuda:0"),
        use_esm_embeddings=True,
    )

input_dir = Path("/app/fastas")
output_dir = Path("/app/structures")

fasta_files = list(input_dir.glob("*.fasta"))

# Example usage: print all fasta file paths
for fasta_file in fasta_files:
    candidates = infer(fasta_file)
    cif_paths = candidates.cif_paths
    scores = [rd.aggregate_score for rd in candidates.ranking_data]
    # Load pTM, ipTM, pLDDTs and clash scores for sample 2
    # need to get the structures out
    scores = np.load(output_dir.joinpath("scores.model_idx_2.npz"))
