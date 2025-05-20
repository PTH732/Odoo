{
    'name': "module-advance",
    'summary': """ Short (1 phrase/line) summary of the module's purpose, used as subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "PTH",
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',
    'data': [
        'views/people_views.xml',
    ],
    'depends': ['base'],
    'installable': True,
    'application': True,
}