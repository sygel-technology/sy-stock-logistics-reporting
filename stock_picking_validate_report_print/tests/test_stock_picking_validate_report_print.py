# Copyright 2025 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import Command
from odoo.tests import common


class TestStockPickingValidateReportPrint(common.TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.server = cls.env["printing.server"].create({})
        cls.printer_1 = cls.env["printing.printer"].create(
            {
                "name": "Printer-1",
                "server_id": cls.server.id,
                "system_name": "Sys Name",
            }
        )
        cls.printer_2 = cls.env["printing.printer"].create(
            {
                "name": "Printer-2",
                "server_id": cls.server.id,
                "system_name": "Sys Name",
            }
        )
        cls.user_1 = cls.env["res.users"].create({"name": "User-1", "login": "user_1"})
        cls.user_2 = cls.env["res.users"].create({"name": "User-2", "login": "user_2"})
        cls.product = cls.env["product.product"].create(
            {"name": "Test Product", "type": "consu"}
        )

    def create_out_picking(self):
        return self.env["stock.picking"].create(
            {
                "picking_type_id": self.env.ref("stock.picking_type_out").id,
                "location_id": self.env.ref("stock.stock_location_stock").id,
                "location_dest_id": self.env.ref("stock.stock_location_customers").id,
                "move_type": "one",
                "move_ids_without_package": [
                    Command.create(
                        {
                            "name": "test",
                            "product_id": self.product.id,
                            "product_uom_qty": 1.0,
                            "location_id": self.env.ref(
                                "stock.stock_location_stock"
                            ).id,
                            "location_dest_id": self.env.ref(
                                "stock.stock_location_customers"
                            ).id,
                        }
                    ),
                ],
            }
        )

    def test_general_printing_without_user(self):
        delivery_slip_report = self.env.ref("stock.action_report_delivery")
        picking_operations_report = self.env.ref("stock.action_report_picking")
        picking_type_out = self.env.ref("stock.picking_type_out")
        picking_type_out.write(
            {
                "print_at_validate": True,
                "validate_print_report_ids": [
                    delivery_slip_report.id,
                    picking_operations_report.id,
                ],
                "validate_print_report_printer_id": self.printer_1.id,
                "validate_print_report_copies": 2,
            }
        )
        picking = self.create_out_picking()
        docs_to_print = picking.with_user(
            self.user_1
        )._get_validate_documents_to_print()

        # User 1
        docs_to_print = picking.with_user(
            self.user_1
        )._get_validate_documents_to_print()

        # Check total number of documents to print
        self.assertEqual(len(docs_to_print), 2)

        # Check stock.action_report_delivery report
        report_dict = list(
            filter(lambda d: d.get("report") == delivery_slip_report, docs_to_print)
        )
        self.assertEqual(len(report_dict), 1)
        self.assertEqual(report_dict[0].get("printer"), self.printer_1)
        self.assertEqual(report_dict[0].get("copies"), 2)

        # Check stock.action_report_picking report
        report_dict = list(
            filter(
                lambda d: d.get("report") == picking_operations_report, docs_to_print
            )
        )
        self.assertEqual(len(report_dict), 1)
        self.assertEqual(report_dict[0].get("printer"), self.printer_1)
        self.assertEqual(report_dict[0].get("copies"), 2)

        # User 2
        docs_to_print = picking.with_user(
            self.user_2
        )._get_validate_documents_to_print()

        # Check total number of documents to print
        self.assertEqual(len(docs_to_print), 2)

        # Check stock.action_report_delivery report
        report_dict = list(
            filter(lambda d: d.get("report") == delivery_slip_report, docs_to_print)
        )
        self.assertEqual(len(report_dict), 1)
        self.assertEqual(report_dict[0].get("printer"), self.printer_1)
        self.assertEqual(report_dict[0].get("copies"), 2)

        # Check stock.action_report_picking report
        report_dict = list(
            filter(
                lambda d: d.get("report") == picking_operations_report, docs_to_print
            )
        )
        self.assertEqual(len(report_dict), 1)
        self.assertEqual(report_dict[0].get("printer"), self.printer_1)
        self.assertEqual(report_dict[0].get("copies"), 2)

    def test_general_printing_with_users(self):
        delivery_slip_report = self.env.ref("stock.action_report_delivery")
        picking_operations_report = self.env.ref("stock.action_report_picking")
        picking_type_out = self.env.ref("stock.picking_type_out")
        picking_type_out.write(
            {
                "print_at_validate": True,
                "validate_print_report_ids": [
                    delivery_slip_report.id,
                    picking_operations_report.id,
                ],
                "validate_print_report_printer_id": self.printer_1.id,
                "validate_print_report_user_ids": [self.user_1.id],
                "validate_print_report_copies": 2,
            }
        )
        picking = self.create_out_picking()

        # User 1
        docs_to_print = picking.with_user(
            self.user_1
        )._get_validate_documents_to_print()

        # Check total number of documents to print
        self.assertEqual(len(docs_to_print), 2)

        # Check stock.action_report_delivery report
        report_dict = list(
            filter(lambda d: d.get("report") == delivery_slip_report, docs_to_print)
        )
        self.assertEqual(len(report_dict), 1)
        self.assertEqual(report_dict[0].get("printer"), self.printer_1)
        self.assertEqual(report_dict[0].get("copies"), 2)

        # Check stock.action_report_picking report
        report_dict = list(
            filter(
                lambda d: d.get("report") == picking_operations_report, docs_to_print
            )
        )
        self.assertEqual(len(report_dict), 1)
        self.assertEqual(report_dict[0].get("printer"), self.printer_1)
        self.assertEqual(report_dict[0].get("copies"), 2)

        # User 2
        docs_to_print = picking.with_user(
            self.user_2
        )._get_validate_documents_to_print()

        # Check total number of documents to print
        self.assertFalse(docs_to_print)

    def test_general_printing_user_not_included(self):
        delivery_slip_report = self.env.ref("stock.action_report_delivery")
        picking_operations_report = self.env.ref("stock.action_report_picking")
        picking_type_out = self.env.ref("stock.picking_type_out")
        picking_type_out.write(
            {
                "print_at_validate": True,
                "validate_print_report_ids": [
                    delivery_slip_report.id,
                    picking_operations_report.id,
                ],
                "validate_print_report_printer_id": self.printer_1.id,
                "validate_print_report_user_ids": [self.user_2.id],
                "validate_print_report_copies": 2,
            }
        )
        picking = self.create_out_picking()

        # User 1
        docs_to_print = picking.with_user(
            self.user_1
        )._get_validate_documents_to_print()

        # Check total number of documents to print
        self.assertFalse(docs_to_print)

        # User 2
        docs_to_print = picking.with_user(
            self.user_2
        )._get_validate_documents_to_print()

        # Check total number of documents to print
        self.assertEqual(len(docs_to_print), 2)

        # Check stock.action_report_delivery report
        report_dict = list(
            filter(lambda d: d.get("report") == delivery_slip_report, docs_to_print)
        )
        self.assertEqual(len(report_dict), 1)
        self.assertEqual(report_dict[0].get("printer"), self.printer_1)
        self.assertEqual(report_dict[0].get("copies"), 2)

        # Check stock.action_report_picking report
        report_dict = list(
            filter(
                lambda d: d.get("report") == picking_operations_report, docs_to_print
            )
        )
        self.assertEqual(len(report_dict), 1)
        self.assertEqual(report_dict[0].get("printer"), self.printer_1)
        self.assertEqual(report_dict[0].get("copies"), 2)

    def test_user_printing_no_user_general(self):
        delivery_slip_report = self.env.ref("stock.action_report_delivery")
        picking_operations_report = self.env.ref("stock.action_report_picking")
        packages_report = self.env.ref("stock.action_report_picking_packages")
        picking_type_out = self.env.ref("stock.picking_type_out")
        picking_type_out.write(
            {
                "print_at_validate": True,
                "validate_print_report_ids": [
                    delivery_slip_report.id,
                    picking_operations_report.id,
                    packages_report.id,
                ],
                "validate_print_report_printer_id": self.printer_1.id,
                "validate_print_report_copies": 2,
                "stock_picking_validate_print_report_ids": [
                    (
                        0,
                        0,
                        {
                            "user_id": self.user_1.id,
                            "report_id": delivery_slip_report.id,
                            "printer_id": self.printer_2.id,
                            "copies": 3,
                        },
                    ),
                    (
                        0,
                        0,
                        {
                            "user_id": self.user_1.id,
                            "report_id": picking_operations_report.id,
                            "printer_id": self.printer_2.id,
                            "copies": 4,
                        },
                    ),
                ],
            }
        )
        picking = self.create_out_picking()

        # User 1
        docs_to_print = picking.with_user(
            self.user_1
        )._get_validate_documents_to_print()

        # Check total number of documents to print
        self.assertEqual(len(docs_to_print), 3)

        # Check stock.action_report_delivery report
        report_dict = list(
            filter(lambda d: d.get("report") == delivery_slip_report, docs_to_print)
        )
        self.assertEqual(len(report_dict), 1)
        self.assertEqual(report_dict[0].get("printer"), self.printer_2)
        self.assertEqual(report_dict[0].get("copies"), 3)

        # Check stock.action_report_picking report
        report_dict = list(
            filter(
                lambda d: d.get("report") == picking_operations_report, docs_to_print
            )
        )
        self.assertEqual(len(report_dict), 1)
        self.assertEqual(report_dict[0].get("printer"), self.printer_2)
        self.assertEqual(report_dict[0].get("copies"), 4)

        # Check action_report_picking_packages report
        report_dict = list(
            filter(lambda d: d.get("report") == packages_report, docs_to_print)
        )
        self.assertEqual(len(report_dict), 1)
        self.assertEqual(report_dict[0].get("printer"), self.printer_1)
        self.assertEqual(report_dict[0].get("copies"), 2)

        # User 2
        docs_to_print = picking.with_user(
            self.user_2
        )._get_validate_documents_to_print()

        # Check total number of documents to print
        self.assertEqual(len(docs_to_print), 3)

        # Check stock.action_report_delivery report
        report_dict = list(
            filter(lambda d: d.get("report") == delivery_slip_report, docs_to_print)
        )
        self.assertEqual(len(report_dict), 1)
        self.assertEqual(report_dict[0].get("printer"), self.printer_1)
        self.assertEqual(report_dict[0].get("copies"), 2)

        # Check stock.action_report_picking report
        report_dict = list(
            filter(
                lambda d: d.get("report") == picking_operations_report, docs_to_print
            )
        )
        self.assertEqual(len(report_dict), 1)
        self.assertEqual(report_dict[0].get("printer"), self.printer_1)
        self.assertEqual(report_dict[0].get("copies"), 2)

        # Check action_report_picking_packages report
        report_dict = list(
            filter(lambda d: d.get("report") == packages_report, docs_to_print)
        )
        self.assertEqual(len(report_dict), 1)
        self.assertEqual(report_dict[0].get("printer"), self.printer_1)
        self.assertEqual(report_dict[0].get("copies"), 2)

    def test_user_printing_with_user_general(self):
        delivery_slip_report = self.env.ref("stock.action_report_delivery")
        picking_operations_report = self.env.ref("stock.action_report_picking")
        packages_report = self.env.ref("stock.action_report_picking_packages")
        picking_type_out = self.env.ref("stock.picking_type_out")
        picking_type_out.write(
            {
                "print_at_validate": True,
                "validate_print_report_ids": [
                    delivery_slip_report.id,
                    picking_operations_report.id,
                    packages_report.id,
                ],
                "validate_print_report_printer_id": self.printer_1.id,
                "validate_print_report_user_ids": [self.user_2.id],
                "validate_print_report_copies": 2,
                "stock_picking_validate_print_report_ids": [
                    (
                        0,
                        0,
                        {
                            "user_id": self.user_1.id,
                            "report_id": delivery_slip_report.id,
                            "printer_id": self.printer_2.id,
                            "copies": 3,
                        },
                    ),
                    (
                        0,
                        0,
                        {
                            "user_id": self.user_1.id,
                            "report_id": picking_operations_report.id,
                            "printer_id": self.printer_2.id,
                            "copies": 4,
                        },
                    ),
                ],
            }
        )
        picking = self.create_out_picking()

        # User 1
        docs_to_print = picking.with_user(
            self.user_1
        )._get_validate_documents_to_print()

        # Check total number of documents to print
        self.assertEqual(len(docs_to_print), 2)

        # Check stock.action_report_delivery report
        report_dict = list(
            filter(lambda d: d.get("report") == delivery_slip_report, docs_to_print)
        )
        self.assertEqual(len(report_dict), 1)
        self.assertEqual(report_dict[0].get("printer"), self.printer_2)
        self.assertEqual(report_dict[0].get("copies"), 3)

        # Check stock.action_report_picking report
        report_dict = list(
            filter(
                lambda d: d.get("report") == picking_operations_report, docs_to_print
            )
        )
        self.assertEqual(len(report_dict), 1)
        self.assertEqual(report_dict[0].get("printer"), self.printer_2)
        self.assertEqual(report_dict[0].get("copies"), 4)

        # User 2
        docs_to_print = picking.with_user(
            self.user_2
        )._get_validate_documents_to_print()

        # Check total number of documents to print
        self.assertEqual(len(docs_to_print), 3)

        # Check stock.action_report_delivery report
        report_dict = list(
            filter(lambda d: d.get("report") == delivery_slip_report, docs_to_print)
        )
        self.assertEqual(len(report_dict), 1)
        self.assertEqual(report_dict[0].get("printer"), self.printer_1)
        self.assertEqual(report_dict[0].get("copies"), 2)

        # Check stock.action_report_picking report
        report_dict = list(
            filter(
                lambda d: d.get("report") == picking_operations_report, docs_to_print
            )
        )
        self.assertEqual(len(report_dict), 1)
        self.assertEqual(report_dict[0].get("printer"), self.printer_1)
        self.assertEqual(report_dict[0].get("copies"), 2)

        # Check action_report_picking_packages report
        report_dict = list(
            filter(lambda d: d.get("report") == packages_report, docs_to_print)
        )
        self.assertEqual(len(report_dict), 1)
        self.assertEqual(report_dict[0].get("printer"), self.printer_1)
        self.assertEqual(report_dict[0].get("copies"), 2)
