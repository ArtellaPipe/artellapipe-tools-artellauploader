#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool to easily upload files into Artella server
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import artellapipe

# Defines ID of the tool
TOOL_ID = 'artellapipe-tools-artellauploader'

# We skip the reloading of this module when launching the tool
no_reload = True


class ArtellUploaderTool(artellapipe.Tool, object):
    def __init__(self, *args, **kwargs):
        super(ArtellUploaderTool, self).__init__(*args, **kwargs)


class ArtellaUploaderToolset(artellapipe.Toolset, object):
    ID = TOOL_ID

    def __init__(self, *args, **kwargs):
        super(ArtellaUploaderToolset, self).__init__(*args, **kwargs)

    def contents(self):
        from artellapipe.tools.artellauploader.widgets import artellauploadertool

        artella_uploader = artellauploadertool.ArtellaUploader(project=self._project, config=self._config)
        return [artella_uploader]
