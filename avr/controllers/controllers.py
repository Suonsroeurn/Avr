# -*- coding: utf-8 -*-
# from odoo import http


# class Avr(http.Controller):
#     @http.route('/avr/avr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/avr/avr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('avr.listing', {
#             'root': '/avr/avr',
#             'objects': http.request.env['avr.avr'].search([]),
#         })

#     @http.route('/avr/avr/objects/<model("avr.avr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('avr.object', {
#             'object': obj
#         })
