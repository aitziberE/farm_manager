from odoo import api, fields, models

class Product(models.Model):
    _name = 'farm_manager.provider'
    _description = 'Provider'

    name = fields.Char(string='Name', required=True)
    product_id = fields.Many2many(comodel_name='farm_manager.product', string='Provided product(s)', ondelete='set null')

    def get_provided_product(self):
        if self.product_id:
            return self.product_id
        return None