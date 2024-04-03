The main algorithm is in the 'code/Goal-directed WGAN-GP.py' line 536-609.

The vanilla WGAN-GP is in the 'code/WGAN-GP.py'

Under code folder,

run Goal-directed WGAN-GP.py will train our goal-directed WGAN-GP. 

run WGAN-GP.py will train our the vanilla WGAN-GP. 

To train with different epoch, please change the value on the right hand side of 'num_epochs =' at line 460. (line 628 in WGAN-GP.py). The model will be saved in result\Goal-directed_WGAN-GP\epoch{num_epochs}

To produce most of the figures, the two models need to train with 0,20,40,60,80,100,1000 epochs and run the code labeled with 1 to 10 in the code folder.

For IC50 comparison, the user needs to manually put the generated peptides to the NetMHCpan website, put the IC50 prediction result in an excell file, and run 6. IC50_compare.py. An example excell file can be found in Results_in_manuscript\Goal-directed_WGAN-GP\epoch100\NetMHCpan_prediction_epoch100.csv.

The Results_in_manuscript has the two models trained by the two different methods.

--------------------Update 4/2/2024--------------------------------

1. The new results for the brain neoepitopes are in the folder "result_for_brain". The corresponding codes are in "code_for_brain".
2. The new results (box plots) of the immunogenicity score predicted by DeepHLApan and IEDB are in the folder "Evaluate_DeepHLApan" and "Evaluate_IEDB", respectively.
