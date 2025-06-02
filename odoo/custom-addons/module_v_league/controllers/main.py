# File: module_v_league/controllers/main.py

from odoo import http
from odoo.http import request


class VLeagueController(http.Controller):
    @http.route('/vleague/players', type='http', auth='public', website=True)
    def show_players(self, **kwargs):
        """
        Hàm này sẽ hiển thị danh sách cầu thủ trên website.
        Đường dẫn truy cập: http://localhost:8017/vleague/players
        """
        players = request.env['football.player'].sudo().search([])

        return request.render('module_v_league.players_template', {
            'players': players
        })

    @http.route('/vleague/player/<int:player_id>', type='http', auth='public', website=True)
    def show_player_detail(self, player_id, **kwargs):
        """
        Xem chi tiết 1 cầu thủ dựa vào ID.
        Ví dụ: http://localhost:8017/vleague/player/1
        """
        player = request.env['football.player'].sudo().browse(player_id)
        if not player.exists():
            return request.not_found()

        return request.render('module_v_league.player_detail_template', {
            'player': player
        })
