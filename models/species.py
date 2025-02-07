from odoo import fields, models

class Species(models.Model):
    _name = 'farm_manager.species'
    _description = 'Animal Species'

    name = fields.Char(string='Name', required=True)
    animal_ids = fields.One2many(comodel_name='farm_manager.animal', inverse_name='species_id', string='Animals')
    per_age_ids = fields.One2many(comodel_name='farm_manager.species_product_age', inverse_name='species_id', string='Product Requirements by Age')