from odoo import models, fields, api

class SaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    track_id = fields.Many2one('iti.track', string='Track')