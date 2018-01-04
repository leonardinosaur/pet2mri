# pet2mri
Processing and semi-quantification of positron emission tomography data

## Requirements
FreeSurfer, Python 2.7, Pandas, NumPy, Matplotlib, and Nibabel.

## Usage
After downloaded the script, put it in a directory that is in your path. Then go to the directory and type
the following to make it executable:

'chmod +x pet2mri'

Then you can use the script with:

'pet2mri -i INPUT -s SUBJID -r REGTYPE -c CONTRAST'

## Outputs
Running the pet2mri script creates a folder in the subject's FreeSurfer directory called 'pet/XXX/' where XXX is a three-digit number. Within this directory, the following subdirectories will also be created:

### vols
Contains the input PET volume (renamed as PET_prereg.nii.gz) and the output PET volume (PET_coreg.nii.gz, PET_coreg.mgz) after coregistering the input to the structural MRI.

### regfiles
Contains registration file (regfile.dat) and other output files from the registration procedure.

### stats
Contains the aparc+aseg.mgz and orig.mgz from the subject's recon-all output, converted to Nifti format. Also contains a text file with the mean SUVr from each Desikan-Killiany ROI, using the mean cerebellar gray matter as the reference region.

### pngs
This folder contains 256 png files. They are snapshots of coronal slices of the coregistered PET volume overlaid onto the subjects structural volume (orig.mgz).
