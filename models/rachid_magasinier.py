# -*- coding: utf-8 -*-
from odoo import api, models, fields


class Magasinier(models.Model):
    _name = 'rachid.magasinier'
    _description = 'Magasinier'
    _inherit = 'rachid.employee'

    Id_code = fields.Integer('ID') 