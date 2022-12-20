# -*- coding: utf-8 -*-
from odoo import api, models, fields


class Product(models.Model):
    _name = 'rachid.type.produit'
    _description = 'Produit'

    Id_code = fields.Integer('ID')
    product_type= fields.Char('Type de produit')
