from odoo import fields, models
from datetime import date

class AnimalGroup(models.Model):
    _name = "farm_manager.animal_group"
    _description = "Animal Group"

    name = fields.Char(string="Group name", required=True)
    description = fields.Text(string="Description")
    area = fields.Char(string="Area", required=True)
    creationDate = fields.Date(string="Creation date", required=True)
    animal_ids = fields.One2many(comodel_name='farm_manager.animal', inverse_name='animal_group_id', string="Animals")
    product_id = fields.Many2one(comodel_name='farm_manager.product', string="Product", ondelete='set null')
