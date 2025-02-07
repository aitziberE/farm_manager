from odoo import models, fields, api

class Provider(models.Model):
    _name = 'farm_manager.provider'
    _description = 'Provider Model'
    _inherit = 'res.partner'

    # Relación One2Many con Product
    product_ids = fields.One2many('product.template', 'provider_id', string='Products')

    channel_ids=fields.Many2many('mail.channel','farm_manager_user_mail_channel_rel','user_id','channel_id')

class Product(models.Model):
    _inherit = 'product.template'

    provider_id = fields.Many2one('provider', string='Provider')

