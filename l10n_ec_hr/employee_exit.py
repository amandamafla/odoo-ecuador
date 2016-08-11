# -*- coding: utf-8 -*-
# © <2016> <Amanda Mafla VIRTUALSAMI CIA LTDA>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields

class HrEmployeeExit(models.Model):

    _name = 'hr.employee_exit'
    _description = 'Employee Exit Process Management'

    name = fields.Char(
        'Número',
        size=64,
        required=True,
    )
    employee_id = fields.Many2one(
        'hr.employee',
        'Empleado',
    )
    request_date = fields.Date(
        'Fecha Solicitud',
        required=True,
    )
    last_day_work = fields.Date(
         'Último día Laborado',
         required=True,
    )
    contract_id = fields.Many2one(
          'hr.contract', 
          'Contract', 
          required=True, 
    )
    approved = fields.Boolean(
          '¿Salida aprobada?',
          default=True,
    )
    #confirm_date_employee, approved_date_department_manager approved_date_hr_manager approved_date_general_manager
    #department_manager department job_title user contact_interview
    #confirm_by approved_department_manager approved_hr_manager approved_general_manager
    #checklist

    reason_leaving = fields.Text(
         'Razón Salida',
         required=True,
    )
    notes = fields.Text(
         'Notas',
    )

    
