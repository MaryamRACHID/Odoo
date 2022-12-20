# -*- coding: utf-8 -*-
from odoo import api, models, fields


class ResponsableStock(models.Model):
    _name = 'rachid.responsable.stock'
    _description = 'Responsable de stock'
    _inherit = 'rachid.employee'

    Id_code = fields.Integer('ID')