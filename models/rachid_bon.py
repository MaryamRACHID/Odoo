# -*- coding: utf-8 -*-
from odoo import api, models, fields


class Bon(models.Model):
    _name = 'rachid.bon'
    _description = 'Bon Rédigé'

    Id_code = fields.Char('Référence')
    qty_bon = fields.Char('Quantité')
    date_bon = fields.Date('Date')
    type_bon_id = fields.Many2one('rachid.type.bon', string="Type")
