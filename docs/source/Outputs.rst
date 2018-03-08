.. _Outputs:

*******
Outputs
*******

The results from pet2mri processing will be in the following output directory::

	$SUBJECTS_DIR/SUBJID/pet/001/

Where $SUBJECTS_DIR is the directory where all of your FreeSurfer processing was outputted to and SUBJID is
the subject ID. The numerical portion of the output directory (e.g. 001/). Will depend on the number of PET
images you've processed with that specific structural scan. For example, if you process another PET image with
this structural scan, it will be saved in 002 instead of 001. The output directory will contain several
subdirectories that are described below.

vols
====
This folder contains the PET volumes in Nifti format and a single text file. They are named as follows:

- PET_prereg.nii.gz : This is the input PET volume in Nifti format.
- PET_coreg.nii.gz : PET volume registered to the subject's structural 3D-T1 image.
- PET_suvr.nii.gz: An SUVr image.
- input_vol.txt : This is file contains the path of the input PET volume

regfiles
========
Contains registration file (regfile.dat) and other output files (e.g. logs) from the registration procedure.

stats
=====
Several files relevant to qunatification of the PET volume are stored here:

- aparc+aseg.nii.gz : Volume with ROI labels. This is actually the same volume as the aparc+aseg.mgz output from recon-all, except it is converted to Nifti format.
- aseg.nii.gz: Converted version of aseg.mgz from recon-all.
- suvr_data.csv : The first column lists region names and the second column is the average SUVr from each region. 

pngs
====
This folder contains 256 .png files. They are snapshots of coronal slices of the coregistered PET volume (vols/PET_coreg.nii.gz) overlaid 
onto the subjects structural volume (pngs/orig.nii.gz)


