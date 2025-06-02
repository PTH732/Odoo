from odoo import models, fields, api

class FootballTransfer(models.Model):
    _name = 'football.transfer'
    _description = 'Football Transfer'

    player_id = fields.Many2one('football.player', required=True)
    from_club_id = fields.Many2one('football.club', string='From Club')
    to_club_id = fields.Many2one('football.club', string='To Club')
    transfer_date = fields.Date()
    transfer_fee = fields.Float()

    @api.model
    def create(self, vals):
        transfer = super().create(vals)
        # Cập nhật club_id của cầu thủ
        if transfer.player_id and transfer.to_club_id:
            transfer.player_id.club_id = transfer.to_club_id.id
        return transfer

    def write(self, vals):
        res = super().write(vals)
        for rec in self:
            # Nếu có cập nhật to_club_id thì cập nhật club_id của cầu thủ
            if 'to_club_id' in vals and rec.to_club_id:
                rec.player_id.club_id = rec.to_club_id.id
        return res