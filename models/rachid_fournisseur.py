from odoo import models, fields, api

class Fournisseur(models.Model):
    _name = 'rachid.fournisseur'

    Id_code = fields.Integer('ID')
    code = fields.Char('Code')
    nom_resp = fields.Char('Nom du responsable')
    adresse = fields.Char('Adresse')
    courriel= fields.Char('Courriel')
    prenom_resp = fields.Char('Prénom du responsable')
    fax = fields.Char('fax')
    gsm1 = fields.Char('Téléphone professionnel')
    gsm2 = fields.Char('Téléphone personnel')

    product_ids = fields.One2many('rachid.product','fournisseur_id',string='Produit')
    