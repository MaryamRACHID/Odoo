# -*- coding: utf-8 -*-
from odoo import api, models, fields


class Compte(models.Model):
    _name = 'rachid.compte'
    _rec_name = "alias"
    _description = 'Compte'

    Id_code = fields.Integer('ID')
    alias = fields.Char('Alias')
    date_creation = fields.Date('Date de création')
    description = fields.Text('Description')

    entreprise_id = fields.Many2one('rachid.entreprise', string="Entreprise")
    
    @api.model
    def create(self, values):
       thisTable=self.env['rachid.compte'].search([('id','<>',0)])
       values["Id_code"] = len(thisTable)+1
       _object = super(Compte, self).create(values)
       return _object