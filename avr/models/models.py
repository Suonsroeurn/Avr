# -*- coding: utf-8 -*-

from odoo import models, fields, api


class avr(models.Model):
    _inherit = 'res.partner'
    _description = 'address customize'

    address_en = fields.Char("Address English")
    address_kh = fields.Char("Address Khmer")
    address_id = fields.Many2one("khmer.address", string='Commune search', ondelete='restrict')
    
    @api.onchange('address_id')
    def _onchange_address(self):
        if self.address_id:
            address_str = self.address_id.commune_en
            if self.address_id.district_en:
                address_str += ", " + self.address_id.district_en
            if self.address_id.province_en:
                address_str += ", " + self.address_id.province_en
            if self.address_id.country_en:
                address_str += ", " + self.address_id.country_en
            self.address_en = address_str
            address_str = self.address_id.commune_kh
            if self.address_id.district_kh:
                address_str += ", " + self.address_id.district_kh
            if self.address_id.province_kh:
                address_str += ", " + self.address_id.province_kh
            if self.address_id.country_kh:
                address_str += ", " + self.address_id.country_kh
            self.address_kh = address_str

class KhmerAddress(models.Model):
    _description = "Khmer Address"
    _name = 'khmer.address'
    _order = 'name'

    name = fields.Char(string='Commune Search', required=True,
               help='Administrative divisions of Cambodia')
    commune_en = fields.Char(string='Commune English')
    commune_kh = fields.Char(string='Commune Khmer')
    district_en = fields.Char(string='District English')
    district_kh = fields.Char(string='District Khmer')
    province_en = fields.Char(string='Khan/Province English')
    province_kh = fields.Char(string='Khan/Province Khmer')
    country_en = fields.Char(string='Country English', default="Cambodia")
    country_kh = fields.Char(string='Country Khmer', default="កម្ពុជា")