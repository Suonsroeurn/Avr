# -*- coding: utf-8 -*-

from odoo import models, fields, api


class avr(models.Model):
    _inherit = 'res.partner'
    _description = 'address customize'

    father_name = fields.Char("Father Name")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
