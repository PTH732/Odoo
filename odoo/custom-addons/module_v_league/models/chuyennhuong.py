from odoo import models, fields, api

class FootballTransfer(models.Model):
    _name = 'football.transfer'
    _description = 'Football Transfer'

    player_id = fields.Many2one('football.player', required=True)
    from_club_id = fields.Many2one('football.club', string='From Club')
    to_club_id = fields.Many2one('football.club', string='To Club')
    transfer_date = fields.Date()
    transfer_fee = fields.Float()

    def _onchange_player_id(self):
        if self.player_id:
            self.from_club_id = self.player_id.club_id

    def _onchange_to_club_id(self):
        if self.player_id and self.to_club_id:
            self.player_id.club_id = self.to_club_id



