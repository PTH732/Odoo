from odoo import models, fields

class FootballTournament(models.Model):
    _name = 'football.tournament'
    _description = 'Football Tournament'

    name = fields.Char(required=True)
    year = fields.Integer()
    club_ids = fields.Many2many('football.club', string='Participating Clubs')
    match_ids = fields.One2many('football.match', 'tournament_id', string='Matches')
