# Copyright 2025 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class StockPickingValidateReport(models.Model):
    _name = "stock.picking.validate.print.report"
    _description = "Stock Picking Validate Print Report"

    stock_picking_type_id = fields.Many2one(
        comodel_name="stock.picking.type",
        string="Picking Type",
        required=True,
        ondelete="cascade",
    )
    user_id = fields.Many2one(
        comodel_name="res.users",
        string="User",
        required=True,
        ondelete="cascade",
        domain="[('share', '=', False)]",
    )
    report_id = fields.Many2one(
        comodel_name="ir.actions.report",
        string="Report",
        domain="[('report_type', '=', 'qweb-pdf'), ('model', '=', 'stock.picking')]",
        required=True,
        ondelete="cascade",
    )
    printer_id = fields.Many2one(
        comodel_name="printing.printer", string="Printer", required=True
    )
    copies = fields.Integer(default=1)

    _sql_constraints = [
        (
            "picking_printer_report_uniq",
            "UNIQUE(stock_picking_type_id, report_id, user_id)",
            "Each report can only be selected once in each picking type for each user.",
        ),
        (
            "check_copies",
            "CHECK(copies > 0)",
            "Number of copies in each printing line must be greater than 0",
        ),
    ]
