from odoo import fields, models


class StockPickingType(models.Model):
    _inherit = "stock.picking.type"

    show_packages_delivery_slip = fields.Boolean(
        string="Show Packages in Delivery Report"
    )
