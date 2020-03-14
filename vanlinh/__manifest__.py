{
    'name': 'Inherit Sale',
    'version': '1.0',
    'summary': 'Inherit Sale Customer',
    'sequence': 1,
    'description': """

    """,
    'category': '',
    'website': '',
    'depends': ['sale.order'],
    'data': [
            'views/depend_view.xml',
            'views/sale_order_tag_view.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
