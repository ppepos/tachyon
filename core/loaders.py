# Tachyon - Fast Multi-Threaded Web Discovery Tool
# Copyright (c) 2011 Gabriel Tremblay - initnull hat gmail.com
#
# GNU General Public Licence (GPL)
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA  02111-1307  USA
#

import ast
import codecs
from . import textutils

def load_targets(file):
    """ Load the list of target paths """
    loaded = list()
    f = codecs.open(file, 'r', 'UTF-8')
    for path in f:
        path = path.strip()
        if len(path) > 0 and '#' not in path:
            try:
                # Add processing values
                parsed_path = ast.literal_eval(path)
                parsed_path['timeout_count'] = 0
                loaded.append(parsed_path)
            except SyntaxError as e:
                textutils.output_error('Path parsing error: ' + str(e.strerror))

    f.close()
    return loaded

