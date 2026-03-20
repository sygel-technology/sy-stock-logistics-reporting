# Copyright 2026 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Stock Picking Phytosanitary Report",
    "summary": "Adds a phytosanitary report (plant passport) to stock picking",
    "version": "18.0.1.0.0",
    "category": "Stock",
    "website": "https://github.com/sygel-technology/sy-stock-logistics-reporting",
    "author": "Sygel",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "stock",
        "product_botanic_denomination",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/botanic_denomination_views.xml",
        "views/phytosanitary_report.xml",
        "views/res_company_views.xml",
    ],
}
