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
