# -*- coding: utf-8 -*-
from odoo import api, models, fields


class TypeBon(models.Model):
    _name = 'rachid.type.stock'
    _description = 'Type de stock'

    Id_code = fields.Integer('ID')
    Titre_type_stock = fields.Char('Titre')
