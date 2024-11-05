import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-stock-logistics-reporting",
    description="Meta package for sygel-technology-sy-stock-logistics-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-stock_picking_report_valued_copy_unvalued>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
