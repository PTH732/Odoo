from odoo import models, fields, api


class People7(models.Model):
    _name = 'people7'
    _description = 'People7'

    name = fields.Char(string='Name')

