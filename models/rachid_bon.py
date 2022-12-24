# -*- coding: utf-8 -*-
from odoo import api, models, fields
from datetime import date
from odoo.exceptions import ValidationError


class Bon(models.Model):
    _name = 'rachid.bon'
    _rec_name = "Id_code"
    _description = 'Bon Rédigé'

    Id_code = fields.Char('Référence')
    qty_bon = fields.Integer('Quantité')
    date_bon = fields.Date('Date')
    type_bon_id = fields.Selection([
        ('sortie', 'Sortie'),
        ('entree', 'Entrée')], string='Type', required=True)
    stock = fields.Many2one('rachid.stock', string="Stock") 
    demande_bon = fields.Many2one('rachid.demande', string="Demande")  
    fiche_mvt = fields.Many2one('rachid.fiche.mvt', string="Fiche de mouvement")  


    @api.constrains('date_bon')
    def validation_constrains(self):
        today = fields.date.today()
        for rec in self:
            if rec.date_bon > today:
                raise ValidationError("Date invalide")

    
 
    @api.onchange('fiche_mvt')
    def update_product(self):
        self.Id_code = self.fiche_mvt.reference
        self.date_bon = self.fiche_mvt.date_verif
        self.stock = self.fiche_mvt.stock_id
        self.type_bon_id = self.fiche_mvt.type_mvt
        self.qty_bon = self.fiche_mvt.demande.qty_demande