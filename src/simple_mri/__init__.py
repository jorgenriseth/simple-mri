from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("simple_mri")
except PackageNotFoundError:
    __version__ = "0.0.0"  # Fallback if not installed


from simple_mri.simple_mri import *
