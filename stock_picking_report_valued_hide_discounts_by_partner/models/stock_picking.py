# Copyright 2025 Valentin Vinagre <valentin.vinagre@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "stock.picking"

    show_discounts = fields.Boolean(
        compute="_compute_show_discounts",
        store=True,
        readonly=False,
        string="Show Discounts in Sale",
    )

    @api.depends("partner_id", "sale_id.show_discounts")
    def _compute_show_discounts(self):
        for rec in self:
            rec.show_discounts = (
                rec.sale_id.show_discounts or rec.partner_id.show_sale_discounts
            )
