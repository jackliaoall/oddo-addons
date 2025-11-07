# -*- coding: utf-8 -*-

from odoo import api, fields, models


class HrExpenseAiWizard(models.TransientModel):
    _name = 'hr.expense.ai.wizard'
    _description = 'HR Expense AI Wizard'

    expense_id = fields.Many2one(
        'hr.expense',
        string='Expense',
        required=True
    )
    ai_date = fields.Date(
        string='AI Date',
        default=fields.Date.context_today,
        required=True
    )

    def action_confirm(self):
        """Confirm action for the wizard"""
        self.ensure_one()
        # Here you can add logic to process the selected date
        # For example, update the expense or perform some AI-related operation
        return {'type': 'ir.actions.act_window_close'}
