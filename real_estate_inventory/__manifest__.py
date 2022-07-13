{
    'name': "Real Estate Inventory",

    'summary': """
        Add projects, Building and Units (Products)""",

    'description': """
        Managing Beta Egypt's inventory. This module is integrated with all other modules, such as CRM, Approvals, ... etc
    """,

    'author': "Beta Egypt",
    'website': "https://www.betaegypt.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': "Sales/CRM",
    'version': '1.0',
    # any module necessary for this one to work correctly
    'depends': ['product','web_dashboard'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/dashboard_views.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': ['account'],
}

