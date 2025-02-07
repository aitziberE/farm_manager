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
    'base', 'hr',
        'stock',
        'sale',
        'account',
    ],
    'data': [
        'security/res_groups.xml',
		'security/ir_model_access.xml',
        'views/menus.xml',
        'data/default_data.xml',

        'views/animal_group_views.xml',
        'views/animal_views.xml',
        'views/species_views.xml',
        'reports/animal_group_report.xml',
        'reports/animal_report.xml',
        'views/area_view.xml',
        'views/partner_views.xml'
    ],
    'installable': True,
}