# -*- coding: utf-8 -*-
{
    'name': "Account Payment Report",

    'summary': """
       Account Payment Report""",


    'author': "El-sayed Iraky",

    'category': 'accounting',
    'version': '0.1',
    'depends': ['base','account'],
    'data': [
        # 'security/ir.model.access.csv',
        'report/report_template.xml',
        'report/report_ref.xml',
        'views/views.xml',
    ]

}