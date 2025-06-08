{
    "name": "Hospital Management System",
    "version": "1.0",
    "category": "Healthcare",
    "summary": "Hospital Management System for Odoo",
    "description": """
        This module provides hospital management functionality:
        - Patient Management
        - Doctor Management
        - Appointment Scheduling
    """,
    "depends": ["base"],
    "data": ['security/ir.model.access.csv',
             'views/menu.xml',
             'views/patients.xml'],
    "application": True,
    "installable": True,
    "auto_install": False,
    "sequence": -100,
    "author": "Wycliff Ochieng",
    "website": "https://www.yourwebsite.com",
    "license": "LGPL-3",
}