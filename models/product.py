from odoo import api, fields, models


class Product(models.Model):
    _name = 'farm_manager.product'
    _description = 'Product'

    name = fields.Char(string='Name', required=True)
    price = fields.Float(string="Price(€/Kg)", default=1, required=False)
    stock = fields.Integer(string='Stock (Kg)', default=1, required=True)
    monthly_consume= fields.Float(string="Monthly Consume (Kg)", compute="_compute_monthly_consume", store=True)
    #provider_id = fields.Many2many(comodel_name='farm_manager.provider', string='Provider', ondelete='set null')
    animal_group_ids = fields.One2many(comodel_name='farm_manager.animal_group', inverse_name='product_id', string="Animal Groups")

    @api.depends('animal_group_ids.animal_ids.monthly_consume')
    def _compute_monthly_consume(self):
        for record in self:
            total_consume = sum(record.animal_group_ids.mapped('animal_ids').mapped('monthly_consume'))
            record.monthly_consume = total_consume