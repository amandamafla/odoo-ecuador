# -*- coding: utf-8 -*-

from openerp import models, fields

class AccountAssetAsset(models.Model):

    _inherit = 'account.asset.asset'

    employee_id = fields.Many2one(
        'hr.employee', 
        'Empleado',
    )
