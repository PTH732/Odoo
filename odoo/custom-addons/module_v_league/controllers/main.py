from odoo import http
from odoo.http import request


class VLeagueController(http.Controller):

    @http.route('/vleague', type='http', auth='public', website=True)
    def show_players(self, **kwargs):
        players = request.env['football.player'].sudo().search([])
        clubs = request.env['football.club'].sudo().search([])
        standings = request.env['football.standing'].sudo().search([])
        tournament = request.env['football.tournament'].sudo().search([])

        return request.render('module_v_league.players_template', {
            'players': players,
            'clubs': clubs,
            'standings': standings,
            'tournament': tournament,
        })

    @http.route('/vleague/player/<int:player_id>', type='http', auth='public', website=True)
    def show_player_detail(self, player_id, **kwargs):
        player = request.env['football.player'].sudo().browse(player_id)
        if not player.exists():
            return request.not_found()

        return request.render('module_v_league.player_detail_template', {
            'player': player
        })
