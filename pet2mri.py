import os, sys
import shutil
from glob import glob
import argparse
import random

import pandas as pd
import nibabel as ni

from datetime import datetime



def gen_rand_id():
	alpha_num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
	return ''.join(random.choice(alpha_num) for i in range(16))




subj_dir = os.environ['SUBJECTS_DIR']
print subj_dir
if not subj_dir.endswith('/'):
	subj_dir += '/'


start = str(datetime.now())

parser = argparse.ArgumentParser()

# Get inputs
parser.add_argument('-i', '--input', help = 'Input PET volume - Nifi or MGH format')
parser.add_argument('-s', '--subject', help = 'Subjects FreeSurfer directory')
parser.add_argument('-r', '--regtype', help = 'Registration cost function - mi (normalized MI) or bb (boundary-based cost)')
parser.add_argument('-c', '--contrast', help = 'Contrast')


parser.add_argument('-v', '--visqc', help = 'Visual QC')
parser.add_argument('-ir', '--inputreg', help = 'Input registration file (e.g. regfile.dat)')



args = parser.parse_args()

# Check input existence
if not os.path.exists(args.input):
	sys.exit('Error: Input volume %s does not exist' % (args.input))

sdir = subj_dir += args.subject
if not os.path.exists(sdir):
	sys.exist('Error: Subject %s not found in SUBJECTS_DIR %s' % (args.subject, subj_dir))


# Make a PET directory
petdir = sdir + '/pet/'
if not os.path.exists(petdir):
	cmd = 'mkdir -p %s' % petdir
	os.system(cmd)

# Make a directory for this specific input
count = 1
currdir = petdir + "%03d"%count 
while os.path.exists(currdir):
	count += 1
	currdir = petdir + "%03d"%count
cmd = 'mkdir -p %s' % currdir


# Copy the input PET volume to the currdir
prereg_vol = currdir + '/PET_prereg.mgz'
shutil.copy(args.input, prereg_vol)


# If we made it this far, everything is a go.
# Burn baby burn.

# Register PET to MRI
if args.regtype == 'bb':

	# Create random id for job
	randid = gen_rand_id()
	regfile = currdir + '/regfile.dat'

	# Creat register file
	cmd = 'bbregister --s %s --mov %s --reg %s --%s'  % (args.subject, prereg_vol, regfile, args.contrast)

	# Apply registration file
	coreg_vol = petdir + '/PET_coreg.mgz'
	cmd = 'mri_vol2vol --mov %s --targ %s/mri/orig.mgz --reg %s --o %s' % (prereg_vol, sdir, regfile, coreg_vol)

	# Convert to nifti
	cmd = 'mri_convert %s %s' % (coreg_vol, coreg_vol.replace('.mgz', '.nii.gz'))



# Calculate SUVrs

# make stats directory
stat_dir = currdir + '/stats/'
cmd = 'mkdir -p %s' % stat_dir

# copy mri and aseg to PET folder in nifti format
src_aseg = sdir + '/mri/aparc+aseg.mgz'
targ_aseg = stat_dir + '/aseg.nii.gz'
cmd = 'mri_convert %s %s' % (src_aseg, targ_aseg)

# Read recon-all stats


# Load aseg and pet data
aseg_data, pet_data = ni.load(targ_aseg).get_data(), ni.load(coreg_vol.replace('.mgz', '.nii.gz')).get_data()
labels = set(aseg_data.flatten())

# Get mean uptake from reference
lmu, rmu = np.mean(pet_data[np.where(aseg_data == 8)]), np.mean(pet_data[np.where(aseg_data == 47)])
ref_val = 0.5 * (lmu + rmu)

regs, mus, stds, vols = [], [], [], []
for label in labels:
	mus.append(np.mean(pet_data[np.where(aseg_data == label)]/ref_val)
	# Get region name


# Write out to .csv file



# Screen capture for QCing purposes
if args.visqc:
	print ''
