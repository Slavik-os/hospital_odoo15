{
    'name' : 'Hospital',
    'version' : '1.2',
    'summary': 'Hospital',
    'sequence': 1,
    'description': """
        learning module hospital
    """,
    'category': 'Hospital',
    'depends': ['base', 'mail'],
    'data': [
             'security/ir.model.access.csv',
             'security/ir.model.access.csv',
             'views/menu.xml',
             'views/patients_view.xml',
             'views/female_patient_view.xml',
             'views/appointment_view.xml'
             ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
