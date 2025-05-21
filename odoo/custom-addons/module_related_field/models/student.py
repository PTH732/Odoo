from odoo import models, fields, api


class Student(models.Model):
    _name = 'student'
    _description = 'Student'

    people_id = fields.Many2one('people7', string='People7')
    name = fields.Char(related='people_id.name', store=True)