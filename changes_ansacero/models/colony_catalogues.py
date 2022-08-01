# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ColonyCatalogues(models.Model):
    _name = "colony.catalogues"
    _description = "colony.catalogues"

    name = fields.Char(string="Name")