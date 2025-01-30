from odoo import fields, models, api
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
    # Campo calculado
    group_type = fields.Char(string="Edad", compute="_compute_group_type", store=True)
    phone_number = fields.Char(string="Teléfono asociado")

    @api.depends('creationDate')
    def _compute_group_type(self):
        for record in self:
            if record.creationDate:
                age = (date.today() - record.creationDate).days // 365
                if age < 1:
                    record.group_type = "Joven"
                elif 1 <= age <= 5:
                    record.group_type = "Adulto"
                elif age > 10:
                    record.group_type = "Viejo"
                else:
                    record.group_type = "Desconocido"

    @api.onchange('creationDate')
    def _check_creation_date(self):
        today = date.today()
        for record in self:
            if record.creationDate and record.creationDate > today:
                raise models.ValidationError("La fecha de creación no puede ser mayor a la fecha actual.")

    @api.constrains('phone_number')
    def _check_phone_number(self):
        for record in self:
            if record.phone_number and (not record.phone_number.isdigit() or len(record.phone_number) != 9):
                raise models.ValidationError("El número de teléfono debe contener 9 dígitos.")