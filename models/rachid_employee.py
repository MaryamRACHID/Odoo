# -*- coding: utf-8 -*-
from odoo import api, models, fields


class Employee(models.Model):
    _name = 'rachid.employee'
    _rec_name = "employee_nom"
    _description = 'Employee'

    id_code = fields.Char('Code')
    id_c = fields.Integer('ID')
    image = fields.Image(string="Image")
    employee_nom = fields.Char('Nom')
    employee_prenom = fields.Char('Prenom')
    employee_adresse= fields.Char('Adresse')
    employee_courriel= fields.Char('Courriel professionnel')
    employee_courriel2= fields.Char('Courriel personnel')
    gsm1 = fields.Char('N° de travail')
    gsm2 = fields.Char('N° personnel')


    compte_id = fields.Many2one('rachid.compte', string="Compte")
    role_id = fields.Many2many('rachid.role',string='Role')