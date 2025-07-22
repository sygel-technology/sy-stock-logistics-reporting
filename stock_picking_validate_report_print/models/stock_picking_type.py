# Copyright 2025 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class StockPickingType(models.Model):
    _inherit = "stock.picking.type"

    print_at_validate = fields.Boolean(string="Print Reports at Validation")
    stock_picking_validate_print_report_ids = fields.One2many(
        comodel_name="stock.picking.validate.print.report",
        inverse_name="stock_picking_type_id",
        string="Reports",
    )
    validate_print_report_ids = fields.Many2many(
        comodel_name="ir.actions.report",
        string="Reports",
        domain="[('report_type', '=', 'qweb-pdf'), ('model', '=', 'stock.picking')]",
    )
    validate_print_report_printer_id = fields.Many2one(
        comodel_name="printing.printer", string="Printer"
    )
    validate_print_report_user_ids = fields.Many2many(
        comodel_name="res.users", domain="[('share', '=', False)]", string="Users"
    )
    validate_print_report_copies = fields.Integer(string="Copies", default=1)

    _sql_constraints = [
        (
            "check_copies",
            "CHECK(validate_print_report_copies > 0)",
            "Number of copies must be greater than 0",
        )
    ]
