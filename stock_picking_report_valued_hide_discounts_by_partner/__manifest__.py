# Copyright 2025 Valentin Vinagre <valentin.vinagre@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Stock Picking Report Valued Hide Discounts by Partner",
    "summary": "Stock Picking Report Valued Hide Discounts by Partner",
    "version": "16.0.1.0.0",
    "category": "Stock",
    "website": "https://github.com/sygel-technology/sy-stock-logistics-reporting",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "stock_picking_report_valued",
        "sale_order_report_hide_discounts_by_partner",
    ],
    "data": [
        "views/stock_picking.xml",
        "reports/stock_picking_report_valued.xml",
    ],
}
