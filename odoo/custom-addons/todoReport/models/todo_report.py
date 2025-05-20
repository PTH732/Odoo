from odoo import models, fields

class TodoReport (models.Model):
    _name = 'todo.report'
    _description = 'Todo report'

    name = fields.Char('Ten report', required=True)
    description = fields.Char('Ghi Chu', required=True)
    due_date = fields.Date(string='')
    done = fields.Boolean('Da hoan thanh', default=False)

    