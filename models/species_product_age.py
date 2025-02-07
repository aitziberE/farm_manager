from odoo import fields, models

class SpeciesProductAge(models.Model):
    _name = 'farm_manager.species_product_age'
    _description = 'Species Product Requirements by Age'

    product_id = fields.Many2one(comodel_name='farm_manager.product', string='Product', required=True, ondelete='restrict')
    species_id = fields.Many2one(comodel_name='farm_manager.species', string='Species', required=True, ondelete='cascade')
    age = fields.Integer(string='Age (years)', required=True)
    amount = fields.Float(string='Amount (kg/month)', required=True)

    _sql_constraints = [
        ('unique_species_age_product', 'unique(species_id, age, product_id)', 'The same product for a species at the same age already exists!')
    ]