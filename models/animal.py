from odoo import api, fields, models, exceptions
from datetime import date

class Animal(models.Model):
    _name = 'farm_manager.animal'
    _description = 'Animal'
    
    name = fields.Char(string='Name', required=True)
    birthdate = fields.Date(string='Birthdate', required=True)
    animal_group_id = fields.Many2one(comodel_name='farm_manager.animal_group', string='Animal Group', ondelete='set null')
    monthly_consume = fields.Float(string='Monthly Consume (kg)', compute="_compute_monthly_consume", store=True)
    species_id = fields.Many2one(comodel_name='farm_manager.species', string='Species', required=True, ondelete="restrict")
    sub_species = fields.Char(string='Subspecies', required=True)

    @api.constrains('birthdate')
    def _check_birthdate(self):
        for record in self:
            if record.birthdate and record.birthdate > date.today():
                raise exceptions.ValidationError("Birthdate cannot be superior to actual date.")

    def _get_consume_product(self):
        if self.animal_group_id:
            return self.animal_group_id.product_id
        return None
        
    def _get_consume_product_quantity(self, species, age, consume_product):

            species_product = self.env['farm_manager.species_product_age'].search([
                ('species_id', '=', species.id),
                ('age', '=', age),
                ('product_id', '=', consume_product.id)
            ], limit=1)
           
            if species_product:
                return species_product.amount
            return 0.0

    @api.depends('birthdate', 'species_id', 'animal_group_id')
    def _compute_monthly_consume(self):
        for record in self:
            if record.birthdate:
                today = date.today()
                birthdate = fields.Date.from_string(record.birthdate)
                age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            else:
                age = 1

            consume_product = record._get_consume_product()
            if consume_product and record.species_id:
                consume_quantity = record._get_consume_product_quantity(record.species_id, age, consume_product)
                record.monthly_consume = consume_quantity
            else:
                record.monthly_consume = 0.0
