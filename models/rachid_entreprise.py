# -*- coding: utf-8 -*-
from odoo import api, models, fields


class Entreprise(models.Model):
    _name = 'rachid.entreprise'
    _description = 'Entreprise'

    image = fields.Image(string="Image")
    Id_code = fields.Integer('ID')
    entreprise_website= fields.Char('Description')
    entreprise_nom = fields.Char('Nom')
    entreprise_adresse = fields.Char('Prenom')
    entreprise_website= fields.Char('Adresse')
    entreprise_tel= fields.Char('Téléphone') 
    entreprise_courriel= fields.Char('Courriel')

