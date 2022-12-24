# -*- coding: utf-8 -*-
from odoo import api, models, fields


class Demande(models.Model):
    _name = 'rachid.demande'
    _rec_name = "reference"
    _description = 'Demande'

    Id_code = fields.Char('ID')
    reference= fields.Char('Référence')
    qty_demande = fields.Integer('Quantité')
    client_name = fields.Char('Nom')
    client_adresse = fields.Char('Adresse')
    client_email = fields.Char('Courriel')
    client_telephone = fields.Char('Téléphone')
    date_recp_demande = fields.Date('Date de reception') 
    date_verif_demande = fields.Date('Date de vérification') 
    description_demande = fields.Text('Description')  
    bons = fields.One2many('rachid.bon', 'demande_bon', string="Bons")
    product_id = fields.Many2one('rachid.product', string="Produit")
 

