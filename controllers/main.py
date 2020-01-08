# -*- coding: utf-8 -*-
# Copyright 2020 
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.addons.base_rest.controllers import main



class ProjectApiController(main.RestController):
    _root_path = "/project/private/"
    _collection_name = "project.private.services"
    _default_auth = "user"
