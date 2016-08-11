#-*- coding:utf-8 -*-

##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015-Today Amanda Mafla VIRTUALSAMI CIA. LTDA. <amanda@virtualsami.com.ec>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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

from openerp.osv import osv
from openerp.report import report_sxw
import amount_to_text_es

class contract_report(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(contract_report, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'get_amount_to_text': self._get_amount_to_text,
        })

    def _get_amount_to_text(self, obj):
        # Currency complete name is not available in res.currency model
        # Exceptions done here (EUR, USD, BRL) cover 75% of cases
        # For other currencies, display the currency code
        #currency_id = obj.job_id.company_id.currency_id
        #currency = self.pool['res.currency'].browse(self.cr, self.uid, currency_id, context=None)
        #if currency.name.upper() == 'EUR':
        #    currency_name = 'Euro'
        #elif currency.name.upper() == 'USD':
        #    currency_name = 'DÓLAR'
        #elif currency.name.upper() == 'BRL':
        #    currency_name = 'reais'
        #else:
        #    currency_name = currency.name
        currency_name = 'DÓLAR'
        #TODO : generic amount_to_text is not ready yet, otherwise language (and country) and currency can be passed
        #amount_in_word = amount_to_text(amount, context=context)
        #return amount_to_text(amount, currency=currency_name)
        return amount_to_text_es.amount_to_text(obj.wage, 'es', currency=currency_name)

class wrapped_report_contract(osv.AbstractModel):
    _name = 'report.l10n_ec_hr.report_contract'
    _inherit = 'report.abstract_report'
    _template = 'l10n_ec_hr.report_contract'
    _wrapped_report_class = contract_report

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
