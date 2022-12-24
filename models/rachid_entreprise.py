# -*- coding: utf-8 -*-
from odoo import api, models, fields


class Entreprise(models.Model):
    _name = 'rachid.entreprise'
    _rec_name = "entreprise_nom"
    _description = 'Entreprise'

    image = fields.Image(string="Image")
    Id_code = fields.Char('Identifiant')
    entreprise_nom = fields.Char('Nom')
    entreprise_adresse = fields.Char('Adresse')
    entreprise_website= fields.Char('Site web')
    entreprise_tel= fields.Char('Téléphone') 
    entreprise_courriel= fields.Char('Courriel')
    description = fields.Text('Informations supplimentaires')

    fournisseurs = fields.One2many('rachid.fournisseur','entreprise_id',string="Responsable d'approvisionnement")



 
