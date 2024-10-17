# SimpleMRI
SimpleMRI is a library attempting to treat MRIs as simple as possible.
At its center it treats MRI-images as a 3D-/4D-data array (if 4D, the three first indices are assumed to be related to space, and the fourth related to time), paired with an affine map from spatial indices to some real world coordinate space.
It is built upon `nibabel`, but avoids several of the mechanisms or properties included in Nibabel, such as arrayproxies and additional metadata.
While there are some functionality included for changing between different orientations of real space (RAS vs LPS etc.), the users are expected to know which coordinate space is used.

When reading MRI-data from file, the MRI data array is by default reoriented by reversing and permuting the axes such that the linear transform the index-order and direction is aligned with the coordinate axes.

Currently, only reading and writing MRI's of Nifti and FreeSurfer MGH-format.
