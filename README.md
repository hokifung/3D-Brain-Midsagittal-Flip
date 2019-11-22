# 3D-Brain-Midsagittal-Flip

## Background
Originally developed for a stroke research project, this program was used to flip 3D fMRI contrast images with lesions on the left side of the brain along the midline, so all lesions will be on the same side (right as the ipsilesional side in this case) for further analysis. 

The general idea of the program is to flip the left and right sides of an 3D image along the mid-plane on the x-axis. It was written in a way that can be directly applied in many scenarios, to brain or non-brain data. This support extends to batch processing as well as time series based (4D) data.

## Advantage and Extended Usage

### For fellow neuroscience researchers 

**1. It is fast and easy to use.**

* It runs entirely on Python and its dependencies. No installation of other software such as FSL, SPM, and ANTS is required.
    
**2. It supports common medical and neuroimaging file formats.**
    
* Some examples are ANALYZE, GIFTI, NIfTI1, NIfTI2, CIFTI-2, MINC1, MINC2, AFNI BRIK/HEAD, MGH and ECAT.

**3. It works well with different types of (spatially) normalized brain images.**

* Some examples are T1 images, T2 images, t-maps, masks, and fMRI images(coming soon).

### For other users
**1. It supports non-brain images.**

* It will work, without any modification, as long as the intended plane-to-flip sits on the mid-point of the x-axis.

**2. It can be easily modified to flip along the other axes.**

* With minimal modification of the python script, users can flip the image along the y-axis or z-axis. 

## Installation

Install Python3 and the following dependencies
```
pip install tqdm, nibabel
```

## Usage

The python script provides a CLI (Command Line Interface) usage for this program. To execute it:
```
python flip.py <input_folder> <output_folder>
```

## Questions, Issues, and Feedback

https://www.hokifung.com/contact-me/

## License
MIT-licensed.
