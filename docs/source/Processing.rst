.. _Processing:

**********
Processing
**********
This page contains additional information regarding pet2mri processing and the additional options.


Subject
=======
Before a PET image can be processed with pet2mri, the subject must have an anatomical (e.g. 3D-T1) volume that has been
processing with FreeSurfer's 'recon-all' processing stream.

Input
=====
The input PET image must be a 3D volume in Nifti or MGH format. Support for DICOM and raw dynamic scans coming soon.

Registration
============
The registration type is specified by the -r flag and is required. Two types of registration procedures are supported by pet2mri:
- Boundary-based registration (bb)
- Normalized mutual information registration (mi)

Boundary-based registration uses the FreeSurfer bbregister command under the hood. In brief, it maximizes the gradient
across the grey white matter interface. Normalized mutual information registration performs similarly to spm_coreg in Matlab.

If using boundary-based registration, the contrast must also be specified with the -c flag. Possible values
are 't1', 't2', and 'bold'. If you are unsure about the constrast, you can instead try to specify the radiotracer with
the -t/--tracer flag. pet2mri will try to infer the contrast from the radiotracer.


Quantification
==============
By default, regional SUVr values are calculated for all grey matter regions from the Desikan-Killiany atlas and saved to a text file.
These values are calculated as follows. First, the coregistered PET volume is normazled by dividing each voxel value by the mean
uptake in the cerebellar grey matter to generate an SUVr volume. Then regional SUVr values are calculated by taking the average SUVr
within each region.

Screenshots
===========

