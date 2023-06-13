# LocalColabFold (Based on [official instruction](https://github.com/YoshitakaMo/localcolabfold))

[ColabFold](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb) on your local server. See also [ColabFold repository](https://github.com/sokrypton/ColabFold).

## System requirements & Runtime Environment(RE)
* Ubuntu 18.04 or later (Tested on Ubuntu 18.04.5 LTS)
* NVIDIA driver 525.60.11, CUDA Version: 12.0, CuDNN 8.8.0.121
* Anaconda3 (Python 3.10.11)
* tensorflow 2.12.0

## Installation

### On Linux

1. Make sure `curl`, `git`, and `wget` commands are already installed on your PC. If not present, you need install them at first. For Ubuntu, type :<pre>`sudo apt -y install curl git wget`</pre>

2. Make sure your Cuda compiler driver is **11.1 or later** (If you don't have a GPU or don't plan to use a GPU, you can skip this section) :<pre>$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2022 NVIDIA Corporation
Built on Wed_Sep_21_10:33:58_PDT_2022
Cuda compilation tools, release 11.8, V11.8.89
Build cuda_11.8.r11.8/compiler.31833905_0
Build cuda_11.1.TC455_06.29190527_0 </pre> Please type the following command if you haven't installed it :<pre> conda install -c nvidia cuda-toolkit</pre>  (Chose the [specific version of cuda-toolkit](https://anaconda.org/nvidia/cuda-toolkit) based on your system environment.)

3. Make sure your GNU compiler version is **4.9 or later** because `GLIBCXX_3.4.20` is required:<pre>$ gcc --version
gcc (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0
Copyright (C) 2017 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</pre>If the version is 4.8.5 or older (e.g. CentOS 7), install a new one and add `PATH` to it.
4. Download `install_colabbatch_linux.sh` from this repository:<pre>$ wget https://raw.githubusercontent.com/YoshitakaMo/localcolabfold/main/install_colabbatch_linux.sh </pre> and run it in the directory where you want to install:<pre>$ bash install_colabbatch_linux.sh</pre>About 5 minutes later, `colabfold_batch` directory will be created. Do not move this directory after the installation.

    Keep the network unblocked. And **check the log** output to see if there are any errors.

    If you find errors in the output log, the easiest way is to check the network and delete the colabfold_batch directory, then re-run the installation script.

5. Add environment variable PATH:<pre># For bash or zsh<br># export PATH="/path/to/your/localcolabfold/colabfold-conda/bin:\$PATH" export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/root/AlphaFold/localcolabfold/colabfold-conda/lib
export PATH=$PATH:/root/AlphaFold/localcolabfold/colabfold-conda/bin
export CUDA_HOME=$CUDA_HOME:/root/AlphaFold/localcolabfold/colabfold-conda</pre>
It is recommended to add this export command to `~/.bashrc` and restart bash (`~/.bashrc` will be executed every time bash is started)

6. To run the prediction, type <pre>colabfold_batch input/Q5VSL9.fasta output/</pre>The result files will be created in the `outputdir`. This command will execute the prediction without templates and relaxation (energy minimization). If you want to use templates and relaxation, add `--templates` and `--amber` flags, respectively. For example,

    <pre>colabfold_batch --templates --amber input/Q5VSL9.fasta output/</pre>

    To run the AlphaFold2-multimer with the versioned AF2-multimer weights, add `--model-type alphafold2_multimer_v3` in the arguments. e.g. <pre>colabfold_batch --templates --amber --model-type alphafold2_multimer_v3 input/Q5VSL9.fasta output/</pre>`alphafold2_multimer_v1, alphafold2_multimer_v2` are also available. Default is `auto` (use `alphafold2_ptm` for monomers and `alphafold2_multimer_v3` for complexes.)

For more details, see [Flags](#flags) and `colabfold_batch --help`.

#### For WSL2 (in windows)

Before running the prediction:

```
export TF_FORCE_UNIFIED_MEMORY="1"
export XLA_PYTHON_CLIENT_MEM_FRACTION="4.0"
export XLA_PYTHON_CLIENT_ALLOCATOR="platform"
export TF_FORCE_GPU_ALLOW_GROWTH="true"
```

It is recommended to add these export commands to `~/.bashrc` and restart bash (`~/.bashrc` will be executed every time bash is started)
* The complete installation (by checking the command `colabfold_batch`):
> <div align=center><img src='/pics/install_finish.PNG'/></div>


### Input Examples

ColabFold can accept multiple file formats or directory.

```
positional arguments:
  input                 Can be one of the following: Directory with fasta/a3m
                        files, a csv/tsv file, a fasta file or an a3m file
  results               Directory to write the results to
```

#### fasta format

It is recommended that the header line starting with `>` be short since the description will be the prefix of the output file. It is acceptable to insert line breaks in the amino acid sequence.
* Q5VSL9 (837 Amino acids)
```:Q5VSL9.fasta
>sp|Q5VSL9|STRP1_HUMAN Striatin-interacting protein 1 OS=Homo sapiens OX=9606 GN=STRIP1 PE=1 SV=1
MEPAVGGPGPLIVNNKQPQPPPPPPPAAAQPPPGAPRAAAGLLPGGKAREFNRNQRKDSE
GYSESPDLEFEYADTDKWAAELSELYSYTEGPEFLMNRKCFEEDFRIHVTDKKWTELDTN
QHRTHAMRLLDGLEVTAREKRLKVARAILYVAQGTFGECSSEAEVQSWMRYNIFLLLEVG
TFNALVELLNMEIDNSAACSSAVRKPAISLADSTDLRVLLNIMYLIVETVHQECEGDKAE
WRTMRQTFRAELGSPLYNNEPFAIMLFGMVTKFCSGHAPHFPMKKVLLLLWKTVLCTLGG
FEELQSMKAEKRSILGLPPLPEDSIKVIRNMRAASPPASASDLIEQQQKRGRREHKALIK
QDNLDAFNERDPYKADDSREEEEENDDDNSLEGETFPLERDEVMPPPLQHPQTDRLTCPK
GLPWAPKVREKDIEMFLESSRSKFIGYTLGSDTNTVVGLPRPIHESIKTLKQHKYTSIAE
VQAQMEEEYLRSPLSGGEEEVEQVPAETLYQGLLPSLPQYMIALLKILLAAAPTSKAKTD
SINILADVLPEEMPTTVLQSMKLGVDVNRHKEVIVKAISAVLLLLLKHFKLNHVYQFEYM
AQHLVFANCIPLILKFFNQNIMSYITAKNSISVLDYPHCVVHELPELTAESLEAGDSNQF
CWRNLFSCINLLRILNKLTKWKHSRTMMLVVFKSAPILKRALKVKQAMMQLYVLKLLKVQ
TKYLGRQWRKSNMKTMSAIYQKVRHRLNDDWAYGNDLDARPWDFQAEECALRANIERFNA
RRYDRAHSNPDFLPVDNCLQSVLGQRVDLPEDFQMNYDLWLEREVFSKPISWEELLQ
```

**For prediction of multimers, insert `:` between the protein sequences.**
* P01308 (Insulin complex with chian A and B, A chain: 21 Amino acids, B chain: 30 Amino acids)
```
>insulin_AB_complex
GIVEQCCTSICSLYQLENYCN:
FVNQHLCGSHLVEALYLVCGERGFFYTPKT
```

Multiple `>` header lines with sequences in a FASTA format file yield multiple predictions at once in the specified output directory.

#### csv format

In a csv format, `id` and `sequence` should be separated by `,`.

```:test.csv
id,sequence
5AWL_1,YYDPETGTWY
3G5O_A_3G5O_B,MRILPISTIKGKLNEFVDAVSSTQDQITITKNGAPAAVLVGADEWESLQETLYWLAQPGIRESIAEADADIASGRTYGEDEIRAEFGVPRRPH:MPYTVRFTTTARRDLHKLPPRILAAVVEFAFGDLSREPLRVGKPLRRELAGTFSARRGTYRLLYRIDDEHTTVVILRVDHRADIYRR
```

#### a3m format

You can input your a3m format MSA file. For multimer predictions, the a3m file should be compatible with colabfold format.

### Flags

These flags are useful for the predictions.

- **`--amber`** : Use amber for structure refinement (relaxation / energy minimization). To control number of top ranked structures are relaxed set `--num-relax`.
- **`--templates`** : Use templates from pdb.
- **`--use-gpu-relax`** : Run amber on NVidia GPU instead of CPU. This feature is only available on a machine with Nvidia GPUs.
- **`--num-recycle <int>`** : Number of prediction recycles. Increasing recycles can improve the quality but slows down the prediction. Default is `3`. (e.g. `--num-recycle 10`)
- `--custom-template-path <directory>` : Restrict template files used for `--template` to only those contained in the specified directory. This flag enables us to use non-public pdb files for the prediction. See also https://github.com/sokrypton/ColabFold/issues/177 .
- `--random-seed <int>` **Changing the seed for the random number generator can result in different structure predictions.** (e.g. `--random-seed 42`)
- `--num-seeds <int>` Number of seeds to try. Will iterate from range(random_seed, random_seed+num_seeds). (e.g. `--num-seed 5`)
- `--max-msa` : Defines: `max-seq:max-extra-seq` number of sequences to use (e.g. `--max-msa 512:1024`). `--max-seq` and `--max-extra-seq` arguments are also available if you want to specify separately. This is a reimplementation of the paper of [Sampling alternative conformational states of transporters and receptors with AlphaFold2](https://elifesciences.org/articles/75751) demonstrated by del Alamo *et al*.
- `--use-dropout` : activate dropouts during inference to sample from uncertainity of the models.
- `--overwrite-existing-results` : Overwrite the result files.
- For more information, `colabfold_batch --help`.
## Post-processing of the prediction results
### PyMOL

## Testing and Validation
1) Q5VSL9 (Striatin-interacting protein 1)
* Presentation on PyMOL (rank 1 of 5 models is shown):
> <div align=center><img src='/pics/Q5VSL9_pymol.PNG'/></div>
> <div align=center><img src='/pics/sp_Q5VSL9_STRP1_HUMAN_Striatin-interacting_protein_1_OS_Homo_sapiens_OX_9606_GN_STRIP1_PE_1_SV_1_pae.png'/></div>
> <div align=center><img src='/pics/sp_Q5VSL9_STRP1_HUMAN_Striatin-interacting_protein_1_OS_Homo_sapiens_OX_9606_GN_STRIP1_PE_1_SV_1_plddt.png'/></div>
* Presentation on Database of AlphaFold :
> <div align=center><img src='/pics/Q5VSL9_database.PNG'/></div>

2) Insulin (P01308, complex with chain A and B)
* Presentation on PyMOL (rank 1 of 5 models is shown):
> <div align=center><img src='/pics/insulin_pymol.PNG'/></div>
> <div align=center><img src='/pics/insulin_AB_pae.png'/></div>
> <div align=center><img src='/pics/insulin_AB_plddt.png'/></div>
* Presentation on Database of AlphaFold :
> <div align=center><img src='/pics/insulin_databse.PNG'/></div>


