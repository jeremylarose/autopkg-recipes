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
import stat

from autopkglib import Processor, ProcessorError


__all__ = ["Unarchiver7z"]


class Unarchiver7z(Processor):
    description = "Archive decompressor using 7z.'"
    input_variables = {
        "archive_path": {
            "required": False,
            "description": "name of source installer path, defaults to pathname"
        },
        "extract_path": {
            "required": False,
            "description": "where archive will be unpacked, defaults to RECIPE_CACHE_DIR/NAME"
        },
        "purge_destination": {
            "required": False,
            "description": "Whether the contents of the destination directory "
                           "will be removed before unpacking.",
        },
    }
    output_variables = {
    }

    __doc__ = description

    def main(self):

        pathname = self.env.get('pathname')
        RECIPE_CACHE_DIR = self.env.get('RECIPE_CACHE_DIR')
        NAME = self.env.get('NAME')
        purge_destination = self.env.get('purge_destination', False)
        archive_path = self.env.get('archive_path', pathname)
        default_path = os.path.join(RECIPE_CACHE_DIR, NAME)
        extract_path = self.env.get('extract_path', default_path)
        source_7z = os.path.join(os.path.dirname(os.path.abspath(__file__)), '7z')
        dir_7z = os.path.join(RECIPE_CACHE_DIR, '7z')
        file_7z = os.path.join(dir_7z, '7z')

        if os.path.exists(extract_path) and purge_destination == True:
            shutil.rmtree(extract_path)
        else:
            pass

#        os.makedirs(extract_path)

        shutil.copytree(source_7z, dir_7z)
        os.chmod(file_7z, stat.S_IEXEC)

        cmd = [file_7z, 'e', '-y', '-ao', '-o' + extract_path, archive_path]

        proc = subprocess.Popen(cmd,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (stdout, stderr) = proc.communicate()

        shutil.rmtree(dir_7z)

if __name__ == '__main__':
    processor = Unarchiver7z()
    processor.execute_shell()
