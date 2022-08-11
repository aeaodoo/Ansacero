# -*- coding: utf-8 -*-

from odoo import models, fields, api


options = [('Redes Sociales', 'Redes Sociales'),('Búsqueda en Linea', 'Búsqueda en Linea'),('Recomendación de familiar ó amigo', 'Recomendación de familiar ó amigo'),
           ('Publicidad de Camionetas', 'Publicidad de Camionetas'),('Pasó por una Sucursal', 'Pasó por una Sucursal'),('Por un espectacular', 'Por un espectacular')]
class resPartner(models.Model):
    _inherit = 'res.partner'

    How_do_you_know_us = fields.Selection(options, string="How do you know us?") #¿Cómo nos conoce?
    code_plus = fields.Char(string="Code plus")#Codigo Plus
    purchasing_manager = fields.Many2one('res.partner', string="Purchasing manager")#Responsable de compras

    l10n_mx_edi_colony = fields.Many2one('colony.catalogues', string="Nombre de Colonia")

class productTemplate(models.Model):
    _inherit = 'product.template'

    product_level = fields.Char(string="Product level") #Nivel producto
    physical_Inventory = fields.Integer(string="Physical Inventory ") #Inv. Fisico  #
    line = fields.Char(string="Line")  # Línea
    #line = fields.Char(compute="generaLinea", inverse="generaLinea", string="Line")#Línea

    #def generaLinea(self):
    #    for record in self:
    #        if record.categ_id:
    #            record.line = record.categ_id.name
    #        else:
    #            record.line = ""

class resCompany(models.Model):
    _inherit = 'res.company'

    #l10n_mx_edi_colony = fields.Many2one('colony.catalogues', string="Nombre de Colonia")