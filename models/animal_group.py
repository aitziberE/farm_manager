from odoo import fields, models

class AnimalGroup(models.Model):
    _name = "farm_manager.animal_group"
    _description = "Animal Groups"

    name = fields.Char(string="Group name", required=True)
    description = fields.Text(string="Description")
    area = fields.Char(string="Area", required=True)
    creationDate = fields.Datetime(string="Creation date")

    """animal_ids = fields.One2many(
        comodel_name='farm_manager.animal',
        inverse_name='animal_group_id',
        string="Animals",
        ondelete="set null"
    )
    consumes_ids = fields.One2many(
        comodel_name='farm_manager.consumes',
        inverse_name='animal_group_id',
        string="Consumes"
    )
    managers_ids = fields.Many2many(
        comodel_name='farm_manager.managers',
        relation='Manage',
        string="Managers",
        ondelete="set null"
    )"""
