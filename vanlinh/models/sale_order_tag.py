# __author__ = "Linh"

from odoo import models, fields, api


class InheritSale(models.Model):
    _inherit = 'sale.order'

    name1 = fields.Char(string='Name')


