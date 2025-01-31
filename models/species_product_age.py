from odoo import fields, models

class SpeciesProductAge(models.Model):
    _name = 'farm_manager.species_product_age'
    _description = 'Species Product Requirements by Age'

<<<<<<< HEAD
    product_id = fields.Many2one(comodel_name='product.product', string='Product', required=True, ondelete='restrict')
=======
    product_id = fields.Many2one(comodel_name='farm_manager.product', string='Product', required=True, ondelete='restrict')
>>>>>>> ac4a3dc8328dff7d0b7a7e92434794fbc167680e
    species_id = fields.Many2one(comodel_name='farm_manager.species', string='Species', required=True, ondelete='cascade')
    age = fields.Integer(string='Age (years)', required=True)
    amount = fields.Float(string='Amount (kg/month)', required=True)

    _sql_constraints = [
        ('unique_species_age_product', 'unique(species_id, age, product_id)', 'The same product for a species at the same age already exists!')
    ]
