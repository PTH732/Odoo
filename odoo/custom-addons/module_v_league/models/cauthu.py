from odoo import models, fields

class FootballPlayer(models.Model):
    _name = 'football.player'
    _description = 'Football Player'
 
    name = fields.Char(string='Name', required = True)
    image = fields.Binary(string='Image', attachment = True)
    country = fields.Char(string='Country')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', default='male')
    day_of_birth = fields.Datetime(string='Day of birth')
    position_name = fields.Char('Position', groups='module2.group_player_manager')
    height = fields.Float('Height')
    weight = fields.Float('Weight')

    club_id = fields.Many2one('football.club', string='Club')