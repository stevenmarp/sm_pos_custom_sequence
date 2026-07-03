# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    pos_sm_use_receipt_sequence = fields.Boolean(
        related="pos_config_id.sm_use_receipt_sequence", readonly=False)
    pos_sm_receipt_sequence_id = fields.Many2one(
        related="pos_config_id.sm_receipt_sequence_id", readonly=False)
