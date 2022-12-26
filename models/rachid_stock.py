# -*- coding: utf-8 -*-
from odoo import api, models, fields
from datetime import date
from odoo.exceptions import ValidationError




class Stock(models.Model):
    _name = 'rachid.stock'
    _rec_name = "label" 
    _description = 'Stock'

    id_int = fields.Integer('ID')
    Id_code = fields.Char('Code')
    qty_produit = fields.Integer('Quantité')
    label = fields.Char('Label')
    bons = fields.One2many('rachid.bon', 'stock', string="Bons")
 
    product_id = fields.Many2one('rachid.product', string="Produits")

                   
    @api.model
    def create(self, values):
       thisTable=self.env['rachid.stock'].search([('id','<>',0)])
       values["id_int"] = len(thisTable)+1
       _object = super(Stock, self).create(values)
       return _object

    @api.constrains('product_id','type_stock_id','qty_produit')
    def validation_constraints(self):
        res = []

        modelObj = self.env['rachid.stock']        
        for record in self:
            res = modelObj.search([('product_id.product_nom', '=', record.product_id.product_nom),('id', 'not in', self.ids), ('type_stock_id', '=', record.type_stock_id)])
            if res:
                raise ValidationError("Stock deja existe, verifier la liste des stock")
 