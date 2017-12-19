import os, sys
import shutil
from glob import glob
import argparse

import pandas as pd
import nibabel as ni

from datetime import datetime

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
os.system(cmd)

# If we made it this far, everything is a go.
# Burn baby burn.

# Register PET to MRI
if args.regtype == 'bb':
	if args.contrast == 't1':

		# Create random_id for job

		# Creat register file
		cmd = 'bbregister --s %s --mov %s --reg %s --t1'  % (args.subject, args.input, args.)

		# Apply registration file
		cmd = 'mri_vol2vol --mov %s --targ fsurf/%s/mri/orig.mgz --reg regfiles/%s --o %s' % (pv, fs_pid, regfile, outfname)

		# Convert to nifti
		cmd = 'mri_convert %s %s'


# Calculate SUVrs

# make stats directory

# copy aseg to PET folder in nifti format

# Read recon-all stats


# Load aseg and pet data
aseg_data, pet_data = ni.load().get_data(), ni.load().get_data()
labels = set(aseg_data.flatten())

mus, stds, vols = [], [], []
for label in labels:

	# Get region name


# Write out to .csv file



# Screen capture for QCing purposes
if args.visqc:
	print ''
