# -*- coding: utf-8 -*-
from odoo import api, models, fields


class Entreprise(models.Model):
    _name = 'rachid.entreprise'
    _rec_name = "entreprise_nom"
    _description = 'Entreprise'

    id_int = fields.Integer('ID')
    image = fields.Image(string="Image")
    Id_code = fields.Char('Identifiant')
    entreprise_nom = fields.Char('Nom')
    entreprise_adresse = fields.Char('Adresse')
    entreprise_website= fields.Char('Site web')
    entreprise_tel= fields.Char('Téléphone') 
    entreprise_courriel= fields.Char('Courriel')
    description = fields.Text('Informations supplimentaires')

    fournisseurs = fields.One2many('rachid.fournisseur','entreprise_id',string="Responsable d'approvisionnement")

    
    @api.model
    def create(self, values):
       thisTable=self.env['rachid.entreprise'].search([('id','<>',0)])
       values["id_int"] = len(thisTable)+1
       _object = super(Entreprise, self).create(values)
       return _object

 
