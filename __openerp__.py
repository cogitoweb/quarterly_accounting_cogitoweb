# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
    'name': 'Quarterly Accounting',
    'version': '1.0',
    'author': 'Cogito srl',
    'description': 'enables quarterly accounting on Odoo l10n_it',
    'category': 'Reporting',
    'depends': ['l10n_it_vat_registries', 'account_vat_period_end_statement'],
    'data': [
        'report/internal_layout.xml',
        'report/registro_iva.xml',
        'report/vatperiodendstatement.xml',
        'view/company_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}

