# easy-chai
in theory, this should make a useful container

## How to use

```
singularity pull docker://kamalasaurus/chai-container:latest
```

```
singularity pull docker://kamalasaurus/chai-container:latest
mkdir fastas structures
```

Move your interaction fastas to `$install_location/fastas`

```
singularity run --nv --bind $(pwd):/app:rw chai-container.sif
```

```
git clone $script location$
sbatch interactions.sbatch
```