# -*- coding: utf-8 -*-

from odoo import models, fields, api


class avr_fleet(models.Model):
    _inherit = 'fleet.vehicle'
    _description = 'avr_fleet'

    short_vin = fields.Char('Short VIN')
    loan = fields.Char('Loan')
    engine_no = fields.Char('Engin No')
    vehicle_type_id = fields.Selection([('car', 'Car'),
                                     ('accessory', 'Accessory'),
                                     ('driver', 'Driver'),
                                     ('generator', 'Generator'),
                                     ('gps', 'GPS'),
                                     ('heavy_equipment', 'Heavy Equipment'),
                                     ('material_handling', 'Material Handling'),
                                     ('mini_suv', 'Mini Suv'),
                                     ('pick_up', 'Pick Up'),
                                     ('sedan', 'Sedan'),
                                     ('suv', 'Suv'),
                                     ('truck', 'Truck'),
                                     ('u_others', 'U-Others'),
                                     ('van', 'Van')
                                    ], default='car', required=True)
    division = fields.Selection([
        ('avis', 'AVIS'),
        ('budget', 'BUDGET')
        ], 'Division', default='avis', help='Division in AVR', required=True)
    delivery_order = fields.Date("Delivery Order")
    invoice_date = fields.Date("Invoice Date")
    insurance_company = fields.Char("Insurance Company")
    insurance_expire = fields.Date("Insurance Expiry Date")
    gps_company = fields.Char("GPS Company")
    inspection_expire = fields.Date("Inspection Expiry Date")

    @api.depends('model_id.brand_id.name', 'vehicle_type_id', 'model_id.name', 'license_plate')
    def _compute_vehicle_name(self):
        for record in self:
            record.name = (dict(self._fields['vehicle_type_id'].selection).get(record.vehicle_type_id) or '') + '/' + (record.model_id.brand_id.name or '') + '/' + (record.model_id.name or '') + '/' + (record.license_plate or _('No Plate'))