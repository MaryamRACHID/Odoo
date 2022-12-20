# -*- coding: utf-8 -*-
from odoo import api, models, fields


class Compte(models.Model):
    _name = 'rachid.compte'
    _description = 'Compte'

    Id_code = fields.Integer('ID')
    alias = fields.Char('Alias')
    date_creation = fields.Date('Date de création')
    description = fields.Text('Description')

    entreprise_id = fields.Many2one('rachid.entreprise', string="Entreprise")
    