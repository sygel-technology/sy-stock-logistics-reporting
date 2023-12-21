# Copyright 2023 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    unvalued_copy = fields.Boolean(
        'Unvalued Copy',
        help='Print an unvalued picking copy',
    )

    def create(self, values):
        values.update({
            'unvalued_copy': self.env['res.partner'].browse(
                values['partner_id']).unvalued_picking_copy
        })
        return super().create(values)
