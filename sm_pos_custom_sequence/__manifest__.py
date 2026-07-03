# -*- coding: utf-8 -*-
{
    "name": "POS Custom Receipt Sequence",
    "version": "18.0.1.0.0",
    "category": "Point of Sale",
    "summary": "Number POS receipts with your own ir.sequence: custom prefix, suffix, padding per POS configuration",
    "description": """
POS Custom Receipt Sequence
===========================

Replace the default POS receipt number with your own sequence.

* Enable per POS configuration and pick any ir.sequence
* Full sequence power: prefix, suffix, padding, date ranges
  (for example POS/ORD-001BI)
* The number is generated on the server when the order is paid,
  so it is gap-free and safe with several cashiers
* Printed on the receipt in place of the default order reference
* Stored on the order: see Receipt Number in the Extra Info tab
    """,
    "author": "Steven Marp",
    "website": "https://apps.odoo.com/apps/modules/browse?author=Steven Marp",
    "license": "OPL-1",
    "depends": ["point_of_sale"],
    "data": [
        "views/res_config_settings_views.xml",
        "views/pos_order_views.xml",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "sm_pos_custom_sequence/static/src/js/*",
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
    "price": 15.00,
    "currency": "USD",
}
