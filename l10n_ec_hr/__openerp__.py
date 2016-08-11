# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015-Today Amanda Mafla VIRTUALSAMI CIA. LTDA. <amanda@virtualsami.com.ec>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'HR for Ecuador',
    'version': '0.1.0',
    'author': 'VIRTUALSAMI CIA LTDA',
    'website': 'http://www.virtualsami.com.ec',
    'license': 'AGPL-3',
    'category': 'Human Resources',
    'summary': 'HR for Ecuador',
    'depends': [
        'hr',
    ],
    'data': [
        'edi/hr_action_data.xml',
        'views/report_contract.xml',
        'views/employee_exit.xml',
        'hr_report.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
}