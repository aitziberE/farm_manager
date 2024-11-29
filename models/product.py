from odoo import api, fields, models

class Product(models.Model):
    _name = 'farm_manager.product'
    _description = 'Product'
    
    name = fields.Char(string='Name', required=True)
    stock = fields.Integer(string='Stock (Kg)', default=1, required=True)
    provider_id = fields.Many2many(comodel_name='farm_manager.provider', string='Provider', ondelete='set null')

    def get_provided_product(self):        
        if self.provider_id:
            return self.provider_id
        return None