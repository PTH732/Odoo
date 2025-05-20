from odoo import models, fields

class TodoTask (models.Model):
    _name = 'todo.task'
    _description = 'Todo task'

    name = fields.Char('Ten Task', required=True)
    description = fields.Char('Ghi Chu', required=True)
    due_date = fields.Date(string='')
    done = fields.Boolean('Da hoan thanh', default=False)