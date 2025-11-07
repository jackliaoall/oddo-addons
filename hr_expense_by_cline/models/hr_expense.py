# -*- coding: utf-8 -*-

from odoo import api, fields, models


class HrExpense(models.Model):
    _inherit = 'hr.expense'

    ai_cline = fields.Char(
        string='AI Cline',
        help='AI Cline field for expense tracking'
    )

    def action_open_ai_wizard(self):
        """Open the AI wizard for date selection"""
        self.ensure_one()
        return {
            'name': 'AI 按鈕',
            'type': 'ir.actions.act_window',
            'res_model': 'hr.expense.ai.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_expense_id': self.id,
            },
        }
