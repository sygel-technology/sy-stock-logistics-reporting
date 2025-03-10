# Copyright 2025 Valentin Vinagre <valentin.vinagre@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    sale_price_unit_with_discount = fields.Float(
        related="sale_line.sale_price_unit_with_discount",
        string="Sale Price Unit With Discount",
    )
