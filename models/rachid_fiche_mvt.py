# -*- coding: utf-8 -*-
from odoo import api, models, fields


class fiche_mvt(models.Model):
    _name = 'rachid.fiche.mvt'
    _description = 'Fiche de mouvement'

    Id_code = fields.Integer('ID')
    date_fiche_mvt = fields.Date('Date')
