#!/usr/bin/python
#
# Copyright 2017 Jeremy Larose
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import subprocess
import shutil
import sys

from autopkglib import Processor, ProcessorError


__all__ = ["PkgCreator7z"]


class PkgCreator7z(Processor):
    description = "Creates a 7zip self extracting Windows package.'"
    input_variables = {
        "install_flags": {
            "required": False,
            "description": "install arguments passed to the end of an installer",
        },
        "source_path": {
            "required": False,
            "description": "name of source installer path, defaults to pathname"
        },
        "pkgroot": {
            "required": False,
            "description": "where package will be created, defaults to RECIPE_CACHE_DIR"
        },
        "pkg_name": {
            "required": False,
            "description": "name of generated package, make sure it ends with exe, defaults to source filename with exe extension"
        },
        "input_bat_path": {
            "required": False,
            "description": "file path to an install.bat file that the installer and flags get appended to and runs after package is extracted; defaults to PkgCreator7z supplied"
        },
        "extra_files": {
            "required": False,
            "description": "path of a directory or file to include with archive"
        },
    }
    output_variables = {
    }

    __doc__ = description

    def main(self):

        install_flags = self.env.get('install_flags', '')
        extra_files = self.env.get('extra_files', '')
        pathname = self.env.get('pathname')
        RECIPE_CACHE_DIR = self.env.get('RECIPE_CACHE_DIR')
        filename = self.env.get('filename')
        source_path = self.env.get('source_path', pathname)
        source_filename = os.path.basename(source_path)
        (prefix, sep, suffix) = source_filename.rpartition('.')
        pkg_name = self.env.get('pkg_name', prefix + sep +'exe')
        pkgroot = self.env.get('pkgroot', RECIPE_CACHE_DIR)
        pkg_path = os.path.join(pkgroot, pkg_name)

        PkgCreator7z = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'PkgCreator7z')
        PkgCreator7z_dir = os.path.join(pkgroot, 'PkgCreator7z')
        PkgCreator7zr = os.path.join(PkgCreator7z_dir, '7zr')
        PkgCreator7z_Sfx = os.path.join(PkgCreator7z_dir, '7zSD.sfx')
        PkgCreator7z_config = os.path.join(PkgCreator7z_dir, '7zconfig.txt')
        PkgCreator7z_bat = os.path.join(PkgCreator7z_dir, 'install.bat')
        PkgCreator7z_archive = os.path.join(PkgCreator7z_dir, 'archive.7z')

        bat_path = self.env.get('input_bat_path', PkgCreator7z_bat)

        if os.path.exists(pkg_path):
            sys.exit(0)

        if source_filename.endswith('.msi'):
            install = 'msiexec /i ' + source_filename
        elif source_filename.endswith('.msp'):
            install = 'msiexec /p ' + source_filename
        elif source_filename.endswith('.exe'):
            install = source_filename
        else:
            self.output('source_filename does not have a currently supported extension... msi, exe, or msp')
            sys.exit(1)

        if not os.path.exists(pkgroot):
            os.makedirs(pkgroot)

        shutil.copytree(PkgCreator7z, PkgCreator7z_dir, symlinks=True)

        bat_append = ['\npushd "%~dp0"\n', install, ' ', install_flags, '\npopd\n']
        with open(bat_path, 'a') as myfile:
            for batarg in bat_append:
                myfile.write(str(batarg))

        cmd = [PkgCreator7zr, 'a', '-t7z', PkgCreator7z_archive, bat_path, source_path, extra_files, '-r']

        proc = subprocess.Popen(cmd,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (stdout, stderr) = proc.communicate()

        PkgCreator7z_files = [PkgCreator7z_Sfx, PkgCreator7z_config, PkgCreator7z_archive]
        with open(pkg_path, 'w') as outfile:
            for fname in PkgCreator7z_files:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)

        shutil.rmtree(PkgCreator7z_dir)

if __name__ == '__main__':
    processor = PkgCreator7z()
    processor.execute_shell()
