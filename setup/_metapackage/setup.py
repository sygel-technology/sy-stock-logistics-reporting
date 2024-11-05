import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-sygel-technology-sy-stock-logistics-reporting",
    description="Meta package for sygel-technology-sy-stock-logistics-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-stock_picking_kit_components_sale_report',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 12.0',
    ]
)
