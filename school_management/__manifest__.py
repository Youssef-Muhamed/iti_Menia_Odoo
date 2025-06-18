# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'School Management',
    'summary': 'School Management',
    'description': """
          this module is for school management
    """,
    'depends': ['base','mail','sale_management','sale'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/create_track_wizard.xml',

        'views/iti_students_view.xml',
        'views/iti_skills_view.xml',
        'views/iti_track_view.xml',
        'views/sale_order_view.xml',
        'report/student_template.xml',
        'report/student_report.xml',
    ],
    'installable': True,
    'application': True,
    'sequence': 1
}
