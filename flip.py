import os
import sys
import copy
from tqdm import tqdm
import nibabel as nib
from nibabel.testing import data_path


##
# Support Filetype / Images
##
supported_extensions = ('nii', 'gz', 'img', 'gii', 'mnc', 'mgh', 'REC')

##
# Mirror Voxel Data by Defined Axis
##
def MirrorVoxels(original_data):
    for slice_number in range(0, int(original_data.shape[0] / 2)):
            # Copy Data from Memory (Incase Numpy Uses Shallow Copy)
            temporary_slice = copy.deepcopy(original_data[slice_number, :, :])
            # Calculate Mirror Index
            mirror_idx = original_data.shape[0] - 1 - slice_number
            # Offset Additional 1 from Indexing
            original_data[slice_number,:,:] = copy.deepcopy(original_data[mirror_idx,:,: ])
            # Return Temporary Slice Data to Right Side
            original_data[mirror_idx,:,:] = copy.deepcopy(temporary_slice)


if __name__ == "__main__":
    input_path  = sys.argv[1]
    output_path = sys.argv[2]

    print("Retrieving Files from {}".format(input_path))

    # Open OS Directory
    files = os.listdir(path=input_path)

    # Iterate Through Filelist
    for nfile in tqdm(range(len(files))):
        ## Sanity Check
        if files[nfile].lower().endswith(supported_extensions) == False:
            continue

        output_name = output_path + "/flipped_" + files[nfile]
        filepath = input_path + "/" + files[nfile]
        main = nib.load(filepath)
        header = main.header
        main_data = main.get_fdata() 
        edited_data = copy.deepcopy(main_data)
        MirrorVoxels(edited_data) 
        mirror = nib.Nifti1Image(edited_data, main.affine, main.header)
        nib.save(mirror, output_name)
 
    # Announce
    print("Completed : Files Exported to /{}".format(output_path))
