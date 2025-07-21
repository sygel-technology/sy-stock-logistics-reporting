import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-stock-logistics-reporting",
    description="Meta package for sygel-technology-sy-stock-logistics-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-product_label_format_restrict>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_report_valued_copy_unvalued>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_report_valued_hide_discounts_by_partner>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
