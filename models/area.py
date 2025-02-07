from odoo import fields, models

class Area(models.Model):
    _inherit = "hr.department"

    group_id = fields.One2many(comodel_name="farm_manager.animal_group", inverse_name="area", string="Groups")

    name = fields.Char(string="Nombre", realted="group_id.name")