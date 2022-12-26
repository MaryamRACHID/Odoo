# -*- coding: utf-8 -*-
from odoo import api, models, fields
from datetime import date
from odoo.exceptions import ValidationError

class Demande(models.Model):
    _name = 'rachid.demande'
    _rec_name = "reference"
    _description = 'Demande'

    id_int = fields.Integer('ID')
    Id_code = fields.Char('Code')
    reference= fields.Char('Référence')
    qty_demande = fields.Integer('Quantité')
    client_name = fields.Char('Nom')
    client_adresse = fields.Char('Adresse')
    client_email = fields.Char('Courriel')
    client_telephone = fields.Char('Téléphone')
    date_recp_demande = fields.Date('Date de reception',required=True)
    date_verif_demande = fields.Date('Date de vérification',required=True) 
    description_demande = fields.Text('Description')  
    bons = fields.One2many('rachid.bon', 'demande_bon', string="Bons")
    product_id = fields.Many2one('rachid.product', string="Produit")
    date_diff = fields.Integer(compute='_get_difference', string='N° jours', store=True)
    state = fields.Selection([('recu','Reçue'),
                              ('enc','En cours'),
                              ('realisee','Réalisée')],'Etat', default="recu")


    @api.model
    def create(self, values):
       thisTable=self.env['rachid.demande'].search([('id','<>',0)])
       values["id_int"] = len(thisTable)+1
       _object = super(Demande, self).create(values)
       return _object


    @api.constrains('date_bon')
    def validation_constrains(self):
        for rec in self:
            if rec.date_recp_demande > date_verif_demande:
                raise ValidationError("Date invalide")

    
    @api.constrains('date_recp_demande','date_verif_demande')
    def _get_difference(self):
        for rec in self:
            if rec.date_verif_demande and rec.date_recp_demande:
                delta = rec.date_verif_demande - rec.date_recp_demande
                rec.date_diff = delta.days
            else:
                rec.date_diff = 0

    def make_recu(self):
        self.ensure_one()
        self.state = 'recu'

    def make_enc(self):
        self.ensure_one()
        self.state = 'enc'

    def make_realisee(self):
        self.ensure_one()
        self.state = 'realisee'