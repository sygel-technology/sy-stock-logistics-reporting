# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    restricted_product_label_formats = fields.Many2many(
        comodel_name="ir.model.fields.selection",
        domain=lambda self: [
            (
                "field_id",
                "=",
                self.env.ref("product.field_product_label_layout__print_format").id,
            )
        ],
    )
