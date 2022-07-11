# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Warehouse(models.Model):
    _inherit = "stock.warehouse"
    is_spacefill_warehouse  = fields.Boolean(default=False,string='SPACEFILL')
    spacefill_warehouse_account_id =fields.Char(string='ID WAREHOUSE')
  
