# -*- coding: utf-8 -*-
from odoo import api, models, fields


class Demande(models.Model):
    _name = 'rachid.demande'
    _description = 'Demande'

    Id_code = fields.Integer('ID')
    qty_demande = fields.Char('Quantité')
    date_demande = fields.Date('Date')
