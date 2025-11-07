# -*- coding: utf-8 -*-
{
    'name': 'HR Expense by Cline',
    'version': '19.0.1.0.0',
    'category': 'Human Resources/Expenses',
    'summary': 'Extends HR Expense with AI Cline field and wizard',
    'description': """
        HR Expense Extension by Cline
        ==============================

        This module extends the hr_expense module with:
        * AI Cline field in expense forms and tree views
        * AI button to open a wizard for date selection
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': [
        'hr_expense',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_expense_views.xml',
        'wizard/hr_expense_ai_wizard_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
