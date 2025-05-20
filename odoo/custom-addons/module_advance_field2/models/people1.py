from odoo import models, fields

class People1(models.Model):
    _inherit = 'people1'

    # Selection field
    gender = fields.Selection(selection_add=[('3d', '3D')], ondelete={'3d':'set null'})
