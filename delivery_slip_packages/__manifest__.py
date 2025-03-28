{
    "name": "Delivery Slip Packages",
    "version": "17.0.1.0.0",
    "category": "Stock",
    "summary": "Show package numbers in Delivery Slips and Invoices",
    "author": "Sygel, Odoo Community Association (OCA)",
    "website": "https://github.com/sygel-technology/sy-stock-logistics-reporting",
    "depends": ["stock", "delivery_package_number"],
    "data": [
        "views/stock_picking_type_view.xml",
        "views/report_delivery_slip_with_packages.xml",
    ],
    "installable": True,
    "application": False,
    "license": "AGPL-3",
}
