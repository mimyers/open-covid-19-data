#!/usr/bin/python
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--whitelist', '-w', dest='whitelist', action='store_true',
                        help='Filter configs against whitelist.yaml.')
    parser.add_argument('--no-whitelist', dest='whitelist', action='store_false',
                        help='Disable filtering of configs against whitelist.yaml.')
    parser.set_defaults(whitelist=True)
    return parser