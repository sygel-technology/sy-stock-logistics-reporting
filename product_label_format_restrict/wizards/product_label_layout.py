# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class ProductLabelLayout(models.TransientModel):
    _inherit = "product.label.layout"

    def fields_get(self, allfields=None, attributes=None):
        res = super().fields_get(allfields, attributes)
        new_selection = []
        restricted_vals = self.env.company.restricted_product_label_formats.mapped(
            "value"
        )
        if (
            restricted_vals
            and "print_format" in res
            and "selection" in res["print_format"]
        ):
            for sel in res["print_format"]["selection"]:
                if sel[0] not in restricted_vals:
                    new_selection.append(sel)
            res["print_format"]["selection"] = new_selection
        return res

    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        if "print_format" in res.keys():
            restricted_vals = self.env.company.restricted_product_label_formats.mapped(
                "value"
            )
            if res["print_format"] in restricted_vals:
                res.pop("print_format")
        return res
