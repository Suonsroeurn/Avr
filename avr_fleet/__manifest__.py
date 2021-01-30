# -*- coding: utf-8 -*-
{
    'name': "Avr Fleet Management",

    'summary': """
        To fit daily operation""",

    'description': """
        Customize to fit daily use of fleet rental.
    """,

    'author': "sroeurn suon",
    'website': "http://www.soupkophnomkhleng.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','fleet'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/avr_fleet_view.xml',
        'views/avr_fleet_vehicle_cost_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
