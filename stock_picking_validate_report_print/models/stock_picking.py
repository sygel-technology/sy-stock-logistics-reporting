# Copyright 2025 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def _get_validate_documents_to_print(self):
        self.ensure_one()
        docs_to_print = []
        picking_type = self.picking_type_id
        user_report = self.env["ir.actions.report"]
        user_prints = picking_type.stock_picking_validate_print_report_ids.filtered(
            lambda p: self.env.user == p.user_id
        )
        for user_print in user_prints:
            report = user_print.report_id
            content, content_format = report._render_qweb_pdf(
                report.report_name, res_ids=[self.id]
            )
            docs_to_print.append(
                {
                    "printer": user_print.printer_id,
                    "report": report,
                    "content": content,
                    "doc_format": content_format,
                    "copies": user_print.copies,
                }
            )
            user_report += report
        if (
            picking_type.validate_print_report_printer_id
            and picking_type.validate_print_report_ids
            and (
                self.env.user.id in picking_type.validate_print_report_user_ids.ids
                or not picking_type.validate_print_report_user_ids.ids
            )
        ):
            for report in picking_type.validate_print_report_ids.filtered(
                lambda r: r.id not in user_report.ids
            ):
                content, content_format = report._render_qweb_pdf(
                    report.report_name, res_ids=[self.id]
                )
                docs_to_print.append(
                    {
                        "printer": picking_type.validate_print_report_printer_id,
                        "report": report,
                        "content": content,
                        "doc_format": content_format,
                        "copies": picking_type.validate_print_report_copies,
                    }
                )
        return docs_to_print

    def _validate_auto_print(self):
        self.ensure_one()
        docs_to_print = self._get_validate_documents_to_print()
        for doc in docs_to_print:
            doc["printer"].print_document(
                doc["report"],
                doc["content"],
                doc_format=doc["doc_format"],
                copies=doc["copies"],
            )

    def _action_done(self):
        res = super()._action_done()
        for picking in self.filtered(
            lambda p: p.state == "done" and p.picking_type_id.print_at_validate
        ):
            picking._validate_auto_print()
        return res
