{
    'name': 'Hospital Management',
    'description': """
        Hospital management module which is used to mange the hospital functionalities prescription,patient,doctor diagnosis etc
    """,
    'summary': """
    Hospital management module which is used to mange the hospital functionalities prescription,patient,doctor diagnosis etc
""",
    'author': "Fahim Hasan Rakib",
    "license": "AGPL-3",
    'category': 'Hospital',
    'version': '13.0.1.0.2',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/beds_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
