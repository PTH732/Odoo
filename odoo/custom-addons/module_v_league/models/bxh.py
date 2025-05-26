from odoo import models, fields

class FootballStanding(models.Model):
    _name = 'football.standing'
    _description = 'Football Standing'

    club_id = fields.Many2one('football.club', required=True)
    tournament_id = fields.Many2one('football.tournament', required=True)
    played = fields.Integer()
    won = fields.Integer()
    draw = fields.Integer()
    lost = fields.Integer()
    points = fields.Integer()
