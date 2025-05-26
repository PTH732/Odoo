from odoo import models, fields, api

class FootballStanding(models.Model):
    _name = 'football.standing'
    _description = 'Football Standing'
    _order = 'points desc, won desc'
    _sql_constraints = [
        ('club_tournament_unique', 'unique(club_id, tournament_id)', 'Một CLB chỉ được có 1 bảng xếp hạng cho mỗi giải đấu.')
    ]

    club_id = fields.Many2one('football.club', string="Câu lạc bộ", required=True)
    tournament_id = fields.Many2one('football.tournament', string="Giải đấu", required=True)
    played = fields.Integer(string="Số trận", default=0)
    won = fields.Integer(string="Thắng", default=0)
    draw = fields.Integer(string="Hòa", default=0)
    lost = fields.Integer(string="Thua", default=0)
    points = fields.Integer(string="Điểm số", default=0)

    @api.onchange('won', 'draw', 'lost')
    def _compute_played_points(self):
        """Tự tính số trận đã chơi và điểm số khi sửa số trận thắng/hòa/thua."""
        for rec in self:
            rec.played = rec.won + rec.draw + rec.lost
            rec.points = rec.won * 3 + rec.draw
