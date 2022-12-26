# -*- coding: utf-8 -*-
from odoo import api, models, fields


class Magasinier(models.Model):
    _name = 'rachid.magasinier'
    _rec_name = "employee_nom"
    _description = 'Magasinier'
    _inherit = 'rachid.employee' 

    Id_code = fields.Integer('ID') 
    
             
    @api.model
    def create(self, values):
       thisTable=self.env['rachid.magasinier'].search([('id','<>',0)])
       values["Id_code"] = len(thisTable)+1
       _object = super(Magasinier, self).create(values)
       return _object