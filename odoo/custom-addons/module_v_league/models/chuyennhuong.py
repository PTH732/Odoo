from odoo import models, fields, api

class FootballTransfer(models.Model):
    _name = 'football.transfer'
    _description = 'Football Transfer'

    player_id = fields.Many2one('football.player', required=True)
    from_club_id = fields.Many2one('football.club', string='From Club')
    to_club_id = fields.Many2one('football.club', string='To Club')
    transfer_date = fields.Date()
    transfer_fee = fields.Float()