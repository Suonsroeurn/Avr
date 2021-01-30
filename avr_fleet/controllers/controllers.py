# -*- coding: utf-8 -*-
# from odoo import http


# class AvrFleet(http.Controller):
#     @http.route('/avr_fleet/avr_fleet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/avr_fleet/avr_fleet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('avr_fleet.listing', {
#             'root': '/avr_fleet/avr_fleet',
#             'objects': http.request.env['avr_fleet.avr_fleet'].search([]),
#         })

#     @http.route('/avr_fleet/avr_fleet/objects/<model("avr_fleet.avr_fleet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('avr_fleet.object', {
#             'object': obj
#         })
