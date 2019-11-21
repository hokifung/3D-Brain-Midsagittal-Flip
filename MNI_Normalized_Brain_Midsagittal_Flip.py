import os
import copy
import numpy as np
import nibabel as nib
from nibabel.testing import data_path

path = './Images'
files = os.listdir(path=path)
print(len(files))

##
# Mirror Voxel Data by Defined Axis
##
def MirrorVoxels(axis_value, original_data):
    for slice_number in range(0, int(original_data.shape[0] / 2)):
            # Copy Data from Memory (Incase Numpy Uses Shallow Copy)
            temporary_slice = copy.deepcopy(original_data[slice_number, :, :])
            # Calculate Mirror Index
            mirror_idx = original_data.shape[0] - 1 - slice_number
            # Offset Additional 1 from Indexing
            original_data[slice_number,:,:] = copy.deepcopy(original_data[mirror_idx,:,: ])
            # Return Temporary Slice Data to Right Side
            original_data[mirror_idx,:,:] = copy.deepcopy(temporary_slice)


for nfile in range(0,len(files)):
    output_name = path+"/flipped_"+files[nfile]
    filepath = path+"/"+files[nfile]
    main = nib.load(filepath)
    header = main.header
    print(files[nfile])
    print(header.get_data_shape())
    print(header.get_zooms())
    main_data = main.get_fdata() 
    edited_data = copy.deepcopy(main_data)
    MirrorVoxels(26, edited_data) 
    mirror = nib.Nifti1Image(edited_data, main.affine, main.header)
    nib.save(mirror, output_name)
