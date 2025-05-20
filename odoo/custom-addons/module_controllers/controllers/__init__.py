import json
import werkzeug
from odoo import http
from odoo.http import request


class PTHController(http.Controller):

    # nhap link hien noi dung don gian voi ten pth
    @http.route('/PTH', auth='public', type='http')
    def PTH_check(self):
        return "PTH check check check"

    # nhap link hien noi dung kem id o cuoi
    # @http.route('/PTH/<int:id>', auth='public', type='http')
    # def PTH_check(self, id):
    #     return "PTH check check check %s" % str(id)

    # nhap link chuyen duong dan
    # @http.route('/PTH', auth='public', type='http')
    # def PTH_check(self):
    #     return werkzeug.utils.redirect('https://www.google.com')

    # nhap link chuyen sang web dang nhap
    # @http.route('/PTH', auth='public')
    # def PTH_check(self):
    #     return request.render("web.login")

    # nhap link chuyen sang tra ve json thu cong
    # @http.route('/PTH', auth='public', type='http')
    # def PTH_check(self):
    #     return json.dumps({
    #         "check": "check 123"
    #     })

    # tao doi tuong moi trong model res.partner voi ten pth
    # @http.route('/PTH', auth='public', type='http')
    # def PTH_check(self):
    #     partner = request.env['res.partner'].sudo().create({
    #           'name' : 'PTH'
    #     })
    # return 'Partner has been created'