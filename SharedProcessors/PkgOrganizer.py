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
import shutil
import fnmatch

from autopkglib import Processor, ProcessorError


__all__ = ["PkgOrganizer"]


class PkgOrganizer(Processor):
    description = "Simply copies and organizes all Pkgs to PkgOrganizer folder within AutoPkg Cache Folder, intended use as a post processor'"
    input_variables = {
    }
    output_variables = {
    }

    __doc__ = description

    def main(self):

        pathname = self.env.get('pathname', 'NA')
        NAME = self.env.get('NAME')
        version = self.env.get('version')
        pkg_path = self.env.get('pkg_path', pathname)
        RECIPE_CACHE_DIR = self.env.get('RECIPE_CACHE_DIR')
        CACHE_DIR = os.path.abspath(os.path.join(RECIPE_CACHE_DIR, os.pardir))
        Pkgs_folder = os.path.join(CACHE_DIR, 'PkgOrganizer')
        pkg_name = os.path.basename(pkg_path)
        dest_foldername = ''
        dest_pkgname = (NAME + str(version))
        pkg_os = 'mac'

        if pkg_path.endswith('.exe'):
          pkg_os = 'win'
#          dest_pkgname = NAME + str(version) + '.exe'
        elif pkg_path.endswith('.pkg'):
#          dest_pkgname = [NAME, str(version), '.pkg']
           pass
        elif pkg_path.endswith('.dmg'):
          pass
#          dest_pkgname = NAME + str(version) + '.dmg'
        else:
            return

        if fnmatch.fnmatch(pkg_path, '*.download.Win.*'):
          dest_foldername = 'win.downloads'
        elif fnmatch.fnmatch(pkg_path, '*.BIOS-*'):
          dest_foldername = 'win.bios'
        elif fnmatch.fnmatch(pkg_path, '*.DriverPack-*'):
          dest_foldername = 'win.drivers'
        else:
          dest_foldername = pkg_os

        dest_folder_path = os.path.join(Pkgs_folder, dest_foldername)
        dest_path = os.path.join(dest_folder_path, dest_pkgname)

        if os.path.exists(dest_path):
            pass
        else:
            if not os.path.exists(dest_folder_path):
                os.makedirs(dest_folder_path)
            shutil.copy(pkg_path, dest_folder_path)

if __name__ == '__main__':
    processor = PkgOrganizer()
