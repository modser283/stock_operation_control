{
    'name': "stock_control_operation",
    'author': "",
    'category': '',
    'version': '15.0',
    'depends': ['base', 'sale_management', 'account', 'mail','contacts'
                ],
    'data': [
        'security/security.xml',
        'views/stock_picking_type_view.xml',
    ],
    'application': False,
}