{
    'name': 'Odoo Academy',
    'summary': """Modulo para el manejo de recurso y sesiones""",
    'description':"""Modolo para el manejo de:
        -recursos
        -sesiones
        -atenciones
        """,
    'license': 'OPL-1',
    'author': 'santoescu',
    'website': 'www.odoo.com',
    'category': 'Çustom Modules/Tech Training',
    'depends': ['base'],
    'data': [
        'security/academy_groups.xml',
        'security/ir.model.access.csv',
        'security/academy_security.xml'
    ],
    'demo': [
        'demo/course_demo.xml',
    ],
    'application': True,
}