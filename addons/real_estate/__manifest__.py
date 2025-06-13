{
    "name": "Real Estate",
    "version": "1.0",
    "category": "Healthcare",
    "summary": "Real Estate System for Odoo",
    "description": """
        This module provides Real Estate functionality:
        - Patient Management
        - Doctor Management
        - Appointment Scheduling
    """,
    "depends": ["base"],
    "data": ['security/ir.model.access.csv',
             'views/estate.xml',
             'views/estate_property_views.xml',
             'views/estate_menu.xml',],
    "application": True,
    "installable": True,
    "auto_install": False,
    "sequence": -100,
    "author": "Wycliff Ochieng",
    "website": "https://www.wyclifff.com",
    "license": "LGPL-3",
}