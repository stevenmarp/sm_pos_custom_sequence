# -*- coding: utf-8 -*-
from odoo import fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    sm_use_receipt_sequence = fields.Boolean(
        string="Set Receipt Sequence Number",
        help="Number receipts with a custom sequence instead of the default "
             "order reference.")
    sm_receipt_sequence_id = fields.Many2one(
        "ir.sequence", string="Receipt Sequence",
        help="Sequence used to number the receipts of this POS.")
