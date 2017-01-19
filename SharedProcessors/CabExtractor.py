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


__all__ = ["CabExtractor"]


class CabExtractor(Processor):
    description = "Extract CAB files'"
    input_variables = {
        "cab_path": {
            "required": False,
            "description": "Path to a cab file, defaults to pathname",
        },
        "cab_extract_path": {
            "required": False,
            "description": ("where cab will be extracted, defaults to RECIPE_CACHE_DIR/NAME.")
        },
        "purge_destination": {
            "required": False,
            "description": "Whether the contents of the destination directory "
                           "will be removed before unpacking.",
        }
    }
    output_variables = {
        "cab_path": {
            "description": "Path to a cab file, defaults to pathname",
        },
        "cab_extract_path": {
            "description": "where cab will be extracted, defaults to RECIPE_CACHE_DIR/NAME.",
        },
    }

    __doc__ = description

    def main(self):

        pathname = self.env.get('pathname')
        RECIPE_CACHE_DIR = self.env.get('RECIPE_CACHE_DIR')
        filename = self.env.get('filename')
        NAME = self.env.get('NAME')
        cab_path = self.env.get('cab_path', pathname)
        default_path = os.path.join(RECIPE_CACHE_DIR, NAME)
        cab_extract_path = self.env.get('cab_extract_path', default_path)
        purge_destination = self.env.get('purge_destination', False)
        cabextract_git = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'CabExtractor/cabextract')
        cabextract = os.path.join(cab_extract_path, cabextract)

        if os.path.exists(cab_extract_path) and purge_destination == False:
            sys.exit(0)
        elif os.path.exists(cab_extract_path) and purge_destination == True:
            shutil.rmtree(cab_extract_path)
        else:
            pass

        if cab_path.endswith('.CAB'):
            pass
        elif cab_path.endswith('.cab'):
            pass
        else:
            self.output('cab_path does not have a cab or CAB extension')
            sys.exit(1)

        if not os.path.exists(cabextract):
          shutil.copyfile(cabextract_git, cabextract)

        os.chmod(cabextract, stat.S_IEXEC)

        cmd = [cabextract, cab_path, '-d', cab_extract_path]

        proc = subprocess.Popen(cmd,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (stdout, stderr) = proc.communicate()

if __name__ == '__main__':
    processor = CabExtractor()
    processor.execute_shell()
