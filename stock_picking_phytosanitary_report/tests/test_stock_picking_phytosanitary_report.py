# Copyright 2026 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.addons.product_botanic_denomination.tests.test_product_botanic_denomination import (  # noqa: E501
    TestProductBotanicDenomination,
)


class TestBasePhytosanitary(TestProductBotanicDenomination):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env.company.phytosanitary_reference = "Fito-123"
        cls.partner = cls.env["res.partner"].create({"name": "Test Partner"})
        cls.pick = cls.env["stock.picking"].create(
            {
                "partner_id": cls.partner.id,
                "picking_type_id": cls.env.ref("stock.picking_type_out").id,
                "state": "draft",
                "move_ids_without_package": [
                    (
                        0,
                        0,
                        {
                            "name": "test_line",
                            "product_id": cls.product.id,
                            "product_uom_qty": 1.0,
                            "quantity": 0.0,
                        },
                    )
                ],
            }
        )

    def test_report(self):
        """Check that the new report renders without failure"""
        report = self.env.ref(
            "stock_picking_phytosanitary_report.stock_phytosanitary_report"
        )
        self.env["ir.actions.report"]._render_qweb_pdf(report.id, res_ids=self.pick.ids)
