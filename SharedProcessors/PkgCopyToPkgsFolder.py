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

from autopkglib import Processor, ProcessorError


__all__ = ["PkgCopyToPkgsFolder"]


class PkgCopyToPkgsFolder(Processor):
    description = "Simply copies all Pkgs to Pkgs folder in Cache Folder'"
    input_variables = {
    }
    output_variables = {
    }

    __doc__ = description

    def main(self):

        pathname = self.env.get('pathname')
        filename = self.env.get('filename')
        RECIPE_CACHE_DIR = self.env.get('RECIPE_CACHE_DIR')
        CACHE_DIR = os.path.abspath(os.path.join(RECIPE_CACHE_DIR, os.pardir))
        PkgsFolder = os.path.join(CACHE_DIR, 'Pkgs')
#        pkg_path = os.path.join(PkgsFolder, filename)

        if os.path.exists(pkg_path):
            pass
        else:
            shutil.copyfile(pathname, PkgsFolder)

if __name__ == '__main__':
    processor = PkgCopyToPkgsFolder()
    processor.execute_shell()
