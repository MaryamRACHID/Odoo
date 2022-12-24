from odoo import models, fields, api

class Fournisseur(models.Model):
    _name = 'rachid.fournisseur'
    _rec_name = "entreprise_id"


    Id_code = fields.Integer('Identifiant')
    nom_resp = fields.Char('Nom')
    adresse = fields.Char('Adresse')
    courriel= fields.Char('Courriel')
    prenom_resp = fields.Char('Prénom')
    fax = fields.Char('Fax')
    gsm1 = fields.Char('Télé professionnel')
    gsm2 = fields.Char('Télé personnel')

    product_ids = fields.One2many('rachid.product','fournisseur_id',string='Produit')
    entreprise_id = fields.Many2one('rachid.entreprise',string='Entreprise')
     