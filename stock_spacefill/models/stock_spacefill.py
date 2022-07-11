
from odoo import models, fields, api




class stock_spacefill(models.Model):
    _name = 'stock_spacefill.stock_spacefill'
    _description = 'stock_spacefill.stock_spacefill'

    spacefill_shipper_token = fields.Char(string='Token Shipper')
    spacefill_api_url = fields.Char(string='URL SPACEFILL')
    spacefill_erp_account_id =fields.Char(string='ID ERP Shipper')
  #  spacefill_warehouse_ids = fields.Many2one()
