from odoo import http
form odoo.addons.module_controller.controllers.main import PTHController

class PTHController(PTHController)

    @http.route('/PTH')
    def PTH_check(self):
        super(PTHController, self).mountain_check()
        return "inherrit"