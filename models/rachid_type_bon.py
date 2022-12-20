# -*- coding: utf-8 -*-
from odoo import api, models, fields


class TypeBon(models.Model):
    _name = 'rachid.type.bon'
    _description = 'Type de bon'

    Id_code = fields.Integer('ID')
    Titre_type_bon = fields.Char('Titre')
