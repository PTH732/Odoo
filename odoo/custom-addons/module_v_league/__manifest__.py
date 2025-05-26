{
    'name': "module-v-league",
    'version' : "1.0",
    'summary': "Manage football",
        
    'description': " Long description of module's purpose",
    'author': "PTH",
    'category': 'Sports',
    'license': 'LGPL-3',
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/cauthu_views.xml",
        "views/hlv_views.xml",
        "views/clb_views.xml",
        "views/giaidau_views.xml",
        "views/trandau_views.xml",
        "views/menu.xml"
        
    ],
    'depends': ['base'],
    'installable': True,
    'application': True,
}