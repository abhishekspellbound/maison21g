from odoo import api, fields, models, _

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    shipping_box = fields.Selection([
        ('square', 'Square'),
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ])