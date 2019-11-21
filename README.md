# Brain-Midsagittal-Flip 

This program flips normalized brain images (.nii in MNI space) on its midsagittal axis (left-right flip). 

It works well with 3D images including T1 images and contrast images from fMRI analysis.

This support extends to batch processing as well as time series based data.

## Installation
Install the following dependencies for Python3
```
pip install tqdm, nibabel
```

## Usage 
The python script provides a CLI (Command Line Interface) usage for this program. To execute it:
```
python flip.py <input_folder> <output_folder>
```
