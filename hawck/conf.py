# -*- coding: utf-8 -*-
##
## conf.py
## Login : <freyes@wampa>
## Started on  Sun Jul  5 13:17:38 2009 Felipe Reyes
## $Id$
##
## Copyright (C) 2009 Felipe Reyes
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os.path
import os
import logging
import logging.config
from pkg_resources import resource_filename

log = None

settings = {}

def load_config (cfgpath=None):

    if cfgpath is None:
        _cfgpath = os.path.join (os.environ['HOME'], ".hawck.py")
    else:
        _cfgpath = cfgpath

    if os.path.isfile(_cfgpath):
        execfile(_cfgpath, globals)
    else:
        log.error("%s is not a file" % _cfgpath)

def setup_log ():

    localconfig = os.path.join(os.environ['HOME'], ".hawck.logging")

    if os.path.isfile(localconfig):
        logging.config.fileConfig(localconfig)
    else:
        logging.config.fileConfig(resource_filename("hawck.data",
                                                    "logging.conf"))

    log = logging.getLogger("conf")
    log.debug("Log system ready!")
