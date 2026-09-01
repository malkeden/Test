# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2026-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': 'Bill Digitization',
    'version': '19.0.2.0.0',
    'category': 'Accounting',
    'summary': """Converting traditional paper-based bills into digital 
     formats with tax detection, vendor matching, and batch processing.""",
    'description': """Enhanced bill digitization module that reads scanned 
    documents (PDF, JPG, JPEG, PNG) using OCR technology and converts them 
    into accurate vendor bills in Odoo. Features include:
    - Automatic tax rate detection and matching
    - Vendor/supplier auto-detection and partner matching
    - Intelligent table structure parsing
    - Number cross-validation (qty × price = subtotal)
    - Multi-file batch upload and processing
    - Smart OCR text cleaning and error correction""",
    'author': "Cybrosys Techno Solutions",
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'depends': ['base', 'base_accounting_kit', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
        'wizard/digitize_bill_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'bill_digitization/static/src/js/list_controller.js',
            'bill_digitization/static/src/xml/list_controller.xml',
        ],
    },
    'external_dependencies': {
        'python': ['PIL', 'pytesseract', 'pdf2image']
    },
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False
}
