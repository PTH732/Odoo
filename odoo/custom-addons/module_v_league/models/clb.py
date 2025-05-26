from odoo import models, fields

class FootballClub(models.Model):
    _name = 'football.club'
    _description = 'Football Club'

    name = fields.Char(required=True)
    image = fields.Binary(string='Image', attachment = True)
    city = fields.Char()
    stadium = fields.Char()
    coach_id = fields.Many2one('football.coach', string='Coach')
    player_ids = fields.One2many('football.player', 'club_id', string='Players')
