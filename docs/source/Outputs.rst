.. _Outputs:

*******
Outputs
*******

The results from pet2mri processing will be in the following directory::

	$SUBJECTS_DIR/SUBJID/pet/001/

Where $SUBJECTS_DIR is the directory where all of your FreeSurfer processing was outputted to and SUBJID is
the subject ID. This directory will contain several subdirectories that are described below.

vols
====
This folder contains the PET volumes in Nifti format and a single text file. They are named as follows:

- PET_prereg.nii.gz : This is the input PET volume in Nifti format.
- PET_coreg.nii.gz : PET volume registered to the subject's structural 3D-T1 image.
- input.txt : This is file contains the path of the input PET volume

regfiles
========
Contains registration file (regfile.dat) and other output files (logs) from the registration procedure.

stats
=====
Several files relevant to qunatification of the PET volume are stored here:

- aseg.nii.gz : Volume with ROI labels. This is actually the same volume as the aparc+aseg.mgz output from recon-all, except it is converted to Nifti format.
- orig.nii.gz : A copy of the subject's preprocessed structural scan. The same volume as orig.mgz from recon-all, except converted to Nifti.
- suvr_data.csv : The first column lists region names and the second column is the average SUVr from each region. 

pngs
====
This folder contains 256 .png files. They are snapshots of coronal slices of the coregistered PET volume (vols/PET_coreg.nii.gz) overlaid oto the subjects structural volume (stats/orig.mgz)


