from odoo import models, fields, api
from odoo.addons.avr_fleet.models.amount_text_en import amount_to_text

class avr_fleet(models.Model):
    _inherit = 'fleet.vehicle.log.contract'
    _description = 'fleet_vehicle_log_contract_customize'
    
    vehicle_ids = fields.Many2many('fleet.vehicle', 'fleet_vehicle_fleet_vehicle_log_contract_rel', 'fleet_vehicle_id', 'fleet_vehicle_log_contract_id', string="Vehicle Contract", copy=False)
    bank_account = fields.Many2one('res.bank', 'Bank Account')
    km_limited = fields.Integer('Limited Distance')
    deduct_insurance = fields.Monetary('Deducted Insurance')
    insurance_payment = fields.Monetary('Insurance Payment')
    security_deposit = fields.Monetary('Security Deposit')
    contract_number = fields.Char('Contract No', default='/')
    emp_id = fields.Many2one('hr.employee', 'Responsible Person')
    rep_com_id = fields.Many2one('hr.employee', 'Company Representative')
    period = fields.Integer(compute='_compute_period_rental', string='Period of Rental', store=True)
    pro_tmpl_id = fields.Many2one('product.template', 'Product')
    price_ids = fields.Many2many('rental.pricing', 'rental_pricing_fleet_vehicle_log_contract_rel', 'rental_pricing_id', 'fleet_vehicle_log_contract_id', string="Rental Price", compute='_compute_default')
    
    @api.model
    def create(self, vals):
        obj = super(avr_fleet, self).create(vals)
        if obj.contract_number == '/':
            number = self.env['ir.sequence'].get('contract.number') or '/'
            obj.write({'contract_number': number})
        return obj
    
    @api.depends('pro_tmpl_id')
    def _compute_default(self):
        pro = self.env['rental.pricing'].search([('product_template_id','=',self.pro_tmpl_id.id)])
        for rec in self:
            rec.price_ids = pro
    
    @api.model
    def num2currency(self, val):
        return amount_to_text(val)
    
    @api.depends('cost_subtype_id')
    def _compute_contract_name(self):
        for record in self:
            if record.cost_subtype_id.name:
                record.name = record.cost_subtype_id.name + ' ' + 'Contract'
    
    @api.model
    def get_firstname(self, val):
        return val.split()[0]
    
    @api.depends('start_date', 'expiration_date')
    def _compute_period_rental(self):
        for record in self:
            if record.expiration_date and record.start_date:
                start = fields.Date.from_string(record.start_date)
                end = fields.Date.from_string(record.expiration_date)
                record.period = (end - start).days
                
    def action_contract_send(self):
        ''' Opens a wizard to compose an email, with relevant mail template loaded by default '''
        self.ensure_one()
        template_id = int(self.env['ir.config_parameter'].sudo().get_param('contract_template'))
        ctx = {
            'default_model': 'fleet.vehicle.log.contract',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'force_email': True,
        }
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            'context': ctx,
        }