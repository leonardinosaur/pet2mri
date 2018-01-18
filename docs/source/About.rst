.. _About:

*****
About
*****

pet2mri is a suite of tools for processing and quantification of PET data. It is essentially a collection
of Python scripts that act as wrappers for FreeSurfer and SPM commands.

The script performs the following steps:

1. Computes registration between input PET volume and a subject's MRI.
2. Applies registration to input PET volume and saves result
3. Calculates regional SUVr values
4. Generates screenshots of PET overlaid onto MRI.


