# -*- coding: utf-8 -*-
from odoo import api, models, fields


class Stock(models.Model):
    _name = 'rachid.stock'
    _description = 'Stock'

    Id_code = fields.Integer('Code')
    qty_produit = fields.Integer('Quantité')
    label = fields.Char('Label')
    type_stock_id = fields.Many2one('rachid.type.stock', string="Type")
    bons = fields.Many2one('rachid.bon', string="Bons")

    product_id = fields.Many2one('rachid.product', string="Produits")
