from odoo import api, fields, models


class Product(models.Model):
    _name = 'farm_manager.product'
    _description = 'Product'

    name = fields.Char(string='Name', required=True)
    stock = fields.Integer(string='Stock (Kg)', default=1, required=True)
    provider_id = fields.Many2one(comodel_name='farm_manager.provider', string='Provider', ondelete='set null')
    animal_group_ids = fields.One2many(comodel_name='farm_manager.animal_group', inverse_name='product_id', string="Animal Groups")

    def get_provided_product(self):
        if self.provider_id:
            return self.provider_id
        return None