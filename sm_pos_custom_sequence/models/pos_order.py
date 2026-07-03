# -*- coding: utf-8 -*-
from odoo import fields, models


class PosOrder(models.Model):
    _inherit = "pos.order"

    sm_receipt_number = fields.Char(
        string="Custom Receipt Number", readonly=True, copy=False,
        help="Custom receipt number generated from the sequence configured "
             "on the POS.")

    def action_pos_order_paid(self):
        res = super().action_pos_order_paid()
        for order in self:
            config = order.config_id
            if (config.sm_use_receipt_sequence and config.sm_receipt_sequence_id
                    and not order.sm_receipt_number):
                order.sm_receipt_number = config.sm_receipt_sequence_id.next_by_id()
        return res
