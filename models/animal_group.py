from odoo import models, fields

class AnimalGroup(models.Model):
    _name = 'farm_manager.animal_group'
    _description = 'Animal Group'

    name = fields.Char(string="Group Name", required=True)
    product_id = fields.Many2one('product.product', string="Product")
