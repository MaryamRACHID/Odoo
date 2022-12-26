# -*- coding: utf-8 -*-
from odoo import api, models, fields


class Role(models.Model):
    _name = 'rachid.role'
    _rec_name = "titre"
    _description = 'Role'

    id_int = fields.Integer('ID')
    id_role = fields.Char('Code identifiant')
    titre = fields.Char('Role')
    description = fields.Text('Description')
    date_creation = fields.Date('Date de création')
               
    @api.model
    def create(self, values):
       thisTable=self.env['rachid.role'].search([('id','<>',0)])
       values["id_int"] = len(thisTable)+1
       _object = super(Role, self).create(values)
       return _object