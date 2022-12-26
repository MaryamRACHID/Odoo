# -*- coding: utf-8 -*-
from odoo import api, models, fields


class ResponsableStock(models.Model):
    _name = 'rachid.responsable.stock'
    _rec_name = "employee_nom"
    _description = 'Responsable de stock'
    _inherit = 'rachid.employee'

    Id_code = fields.Integer('ID')

                 
    @api.model
    def create(self, values):
       thisTable=self.env['rachid.responsable.stock'].search([('id','<>',0)])
       values["Id_code"] = len(thisTable)+1
       _object = super(ResponsableStock, self).create(values)
       return _object