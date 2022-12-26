# -*- coding: utf-8 -*-
from odoo import api, models, fields
from datetime import date
from odoo.exceptions import ValidationError


class fiche_mvt(models.Model):
    _name = 'rachid.fiche.mvt'
    _rec_name = "reference"
    _description = 'Fiche de mouvement'
    
    id_int = fields.Integer('ID')
    Id_code = fields.Char('Identifiant')
    reference = fields.Char('Référence')
    stock_id = fields.Many2one('rachid.stock', string="Stock")
    demande = fields.Many2one('rachid.demande', string="Demande")
    product = fields.Char('Produit')
    date_verif = fields.Date('Date de mouvement')
    responsable = fields.Many2one('rachid.responsable.stock', string="Responsable du stock")
    description = fields.Text('Information supplimentaire')
    bons = fields.One2many('rachid.bon', 'fiche_mvt', string="Bons")
    type_mvt = fields.Selection([
        ('sortie', 'Sortie'),
        ('entree', 'Entrée')], string='Type', default='sortie',required=True)


    
    @api.model
    def create(self, values):
       thisTable=self.env['rachid.fiche.mvt'].search([('id','<>',0)])
       values["id_int"] = len(thisTable)+1
       _object = super(fiche_mvt, self).create(values)
       return _object

 
    @api.onchange('stock_id','demande')
    def update_quantity(self):
        if self.stock_id.qty_produit > self.demande.qty_demande and self.stock_id.product_id.id == self.demande.product_id.id:
            qty = self.stock_id.qty_produit - self.demande.qty_demande
            self.stock_id.qty_produit = qty
        

        if self.demande.qty_demande > self.stock_id.qty_produit:
            raise ValidationError("Le stock ne support pas la demande")

        
    @api.onchange('demande')
    def update_product(self):
        self.product = self.demande.product_id.product_nom
        if(self.bons):
            self.demande.state = 'realisee'

 