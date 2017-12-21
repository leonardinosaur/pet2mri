# pet2mri
Processing and semi-quantification of positron emission tomography data

# Requirements
FreeSurfer, Python 2.7, Pandas, NumPy, Matplotlib, and Nibabel.

# Usage

# Outputs
Running the pet2mri script creates a folder in the subject's FreeSurfer directory called 'pet/XXX/'where XXX is a three-digit number.
Within this directory, additional subdirectories will also be created:

## vols

## regfiles

## stats

## pngs
This folder contains 256 png files. They are snapshots of coronal slices of the coregistered PET volume overlaid onto the subjects structural volume (orig.mgz)
