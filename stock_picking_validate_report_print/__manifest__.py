# Copyright 2025 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Stock Picking Validate Report Print",
    "version": "17.0.1.0.0",
    "category": "Stock",
    "summary": "Automatically send picking reports to printer when validating",
    "website": "https://github.com/sygel-technology/sy-stock-logistics-reporting",
    "author": "Sygel, Odoo Community Association (OCA)",
    "depends": ["stock", "base_report_to_printer"],
    "data": [
        "security/ir.model.access.csv",
        "views/stock_picking_type_views.xml",
    ],
    "installable": True,
    "application": False,
    "license": "AGPL-3",
}
