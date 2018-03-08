# pet2mri
Processing and semi-quantification of positron emission tomography data. There is documentation available [here](http://pet2mri.readthedocs.io/en/latest/). Both the code and the documentation are underconstruction.

## Requirements
FreeSurfer, Python 2.7, Pandas, NumPy, Matplotlib, and Nibabel.

## Usage
After downloaded the script, put it and the fs_gm.csv file in a directory that is in your path. Then go to that directory and type
the following to make it executable:

`> chmod +x pet2mri`

Then you can use the script with:

`> pet2mri -i INPUT -s SUBJID -r REGTYPE -c CONTRAST`

For more information please see the [documentation](http://pet2mri.readthedocs.io/en/latest/).
