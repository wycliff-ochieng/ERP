{
    "name": "Student Health Management",
    "version": "1.0",
    "category": "Healthcare",
    "summary": "Student Health Management System",
    "description": """
        This module provides student health management functionality:
        - Student Health Records
        - Medical Examinations
        - Health Reports
    """,
    "depends": ["base","hms"],
    "data": [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/student.xml',
        'views/students_list_view.xml',
    ],
    "application": True,    # This makes it appear in the app list
    "installable": True,
    "auto_install": False,
    "sequence": -100,       # This controls the position in the app list
    "author": "wycliff Ochorokodi",
    "license": "LGPL-3",
}