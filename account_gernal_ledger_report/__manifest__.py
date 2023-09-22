
{
    'name': 'Gernal Ledger Report', 
    'version': '13.0.1.1',
    'sequence': 1, 
    'category': 'Gernal Ledger Report', 
    'description': 
        """ 
        Gernal Ledger Report.
    """,
    'summary': 'Gernal Ledger Report',
    'author': 'De ',
    'website': 'http://www.de.com',
    'depends': ['account','account_reports','web'],
    'data': [
        'views/template_search_country.xml',
        'views/assets.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
