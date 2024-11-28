# -*- coding: utf-8 -*-
{
    'name': 'Farm Manager',
    'version': '16.0.1.0',
    'license': 'LGPL-3',
    'author': 'PAIA',
    'website': '',
    'category': 'Agriculture',

    'summary': """
        Module for managing animals, their groups, and feed consumption.
                """,

    'description': """
        The Farm Manager module allows the user to:
        - Register and manage individual animals.
        - Create and manage groups of animals.
        - Assign feed to animals and track their consumption.
        - Maintain stock levels of products such as feed and other resources.
        - Generate reports on consumption and stock status.
        """,     

    'depends': [

    ],
    'data': [
        'views/menus.xml',
    ],   
    'installable': True,  
}
