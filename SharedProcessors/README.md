# PkgCreator7z.py

## Description
Adds a packing function using the 7zip library for windows software.  It can be used to automatically create silent installers from downloaded exe,msi,msp files.  It is currently fully functional, please report any bugs.

## Input Variables
- **install\_flags:**
    - **required:** False
    - **description:** install arguments passed to the end of an installer
- **pkgroot:**
    - **required:** False
    - **description:** where package will be created, defaults to RECIPE_CACHE_DIR
- **pkg\_name:**
    - **required:** False
    - **description:** name of generated package, make sure it ends with exe, defaults to source filename with exe extension
- **input\_bat\_path:**
    - **required:** False
    - **description:** file path to an install.bat file that the install and flags get appended to and runs after package is extracted; defaults to PkgCreator7z supplied
- **source\_path:**
    - **required:** False
    - **description:** name of source installer path, defaults to pathname
- **extra\_files:**
    - **required:** False
    - **description:** path of a directory or file to include with archive

## Output Variables
- **pkg\_path:**
    - **description:** The created package.

# Unarchiver7z.py

## Description
Extract archives using 7z

## Input Variables
- **archive\_path:**
    - **required:** False
    - **description:** Path to a archive file, defaults to pathname
- **extract\_path:**
    - **required:** False
    - **description:** where archive will be unpacked, defaults to RECIPE_CACHE_DIR/NAME.
- **purge\_destination:**
    - **required:** False
    - **description:** Whether the contents of the destination directory will be removed before extracting.

## Output Variables

# CabExtractor.py

## Description
Extract CAB files using cabextract

## Input Variables
- **cab\_path:**
    - **required:** False
    - **description:** Path to a cab file, defaults to pathname
- **cab\_extract\_path:**
    - **required:** False
    - **description:** where cab will be extracted, defaults to RECIPE_CACHE_DIR/NAME.
- **purge\_destination:**
    - **required:** False
    - **description:** Whether the contents of the destination directory will be removed before extracting.

## Output Variables
