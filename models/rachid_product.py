# -*- coding: utf-8 -*-
from odoo import api, models, fields


class Product(models.Model):
    _name = 'rachid.product'
    _rec_name = "product_nom"
    _description = 'Produit'

    Id_code = fields.Integer('ID')
    product_nom = fields.Char('Nom de produit')
    description = fields.Text('Description')
    product_code = fields.Char('Code')
    sale_ok = fields.Boolean('peut être vendu', default=False)
    purchase_ok = fields.Boolean('peut être acheté', default=False)
    sale_prix = fields.Char('Prix de vente')
    customer_taxes = fields.Char('Taxes client')
    cout_product = fields.Char('Coût')
    image = fields.Image("Image")

    type_product = fields.Selection([
        ('consu', 'Sortie'),
        ('service', 'Service'),
        ('stock', 'produit stockable')], default="stock", string='Type', required=True)

    bons = fields.One2many('rachid.bon', 'stock', string="Bons")
    fournisseur_id = fields.Many2many('rachid.fournisseur', string="Fournisseurs")
