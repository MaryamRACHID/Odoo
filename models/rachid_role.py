# -*- coding: utf-8 -*-
from odoo import api, models, fields


class Role(models.Model):
    _name = 'rachid.role'
    _rec_name = "titre"
    _description = 'Role'

    id_role = fields.Char('Code identifiant')
    titre = fields.Char('Role')
    description = fields.Text('Description')
    date_creation = fields.Date('Date de création')
 