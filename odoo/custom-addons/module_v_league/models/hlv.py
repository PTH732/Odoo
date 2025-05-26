from odoo import models, fields

class FootballCoach(models.Model):
    _name = 'football.coach'
    _description = 'Football Coach'

    name = fields.Char(required=True)
    image = fields.Binary(string="Image", attachment=True)
    country = fields.Char(string='Country')
    age = fields.Integer()
    experience_years = fields.Integer()
    current_club_id = fields.Many2one('football.club', string='Current Club')
