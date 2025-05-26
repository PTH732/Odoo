from odoo import models, fields, api

class FootballMatch(models.Model):
    _name = 'football.match'
    _description = 'Football Match'

    name = fields.Char(compute='_compute_name', store=True)
    date = fields.Date()
    home_club_id = fields.Many2one('football.club', string='Home Club')
    away_club_id = fields.Many2one('football.club', string='Away Club')
    home_score = fields.Integer()
    away_score = fields.Integer()
    tournament_id = fields.Many2one('football.tournament', string='Tournament')
    match_date = fields.Datetime(string="Match Date", required=True)

    @api.depends('home_club_id', 'away_club_id')
    def _compute_name(self):
        for rec in self:
            if rec.home_club_id and rec.away_club_id:
                rec.name = f"{rec.home_club_id.name} vs {rec.away_club_id.name}"
            else:
                rec.name = "Match"
