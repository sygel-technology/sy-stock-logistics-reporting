# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Product Label Format Restrict",
    "summary": "Allows you to restrict the usage of product label formats",
    "version": "16.0.1.0.0",
    "category": "Product",
    "website": "https://github.com/sygel-technology/sy-stock-logistics-reporting",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "product",
    ],
    "data": [
        "views/res_config_settings_views.xml",
    ],
}
