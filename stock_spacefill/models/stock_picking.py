from odoo import api, fields, models, _
from odoo.addons.stock_spacefill.spacefillpy.api import API as API
from datetime import date, datetime
import pdb

class Picking(models.Model):
    _inherit = "stock.picking"
    order_spacefill_id= fields.Char('order ID spacefill')
    status_spacefill= fields.Char('order spacefill status')