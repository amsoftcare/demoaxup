from odoo import api, fields, models, _
from datetime import datetime, date, time
import time
from datetime import timedelta,datetime
import datetime
from odoo.tools.translate import _
import pdb
import psycopg2
from odoo.tools.translate import html_translate
#from odoo.addons.stock_spacefill.spacefillpy.api import API as API
from odoo.tools import float_round


class product_template(models.Model):
    _inherit = 'product.template'
    is_to_be_exported_to_spacefill=fields.Boolean('Synchro SpaceFill',default= False)
    item_spacefill_id=fields.Char('Uiid Spacefill item')         
product_template()
class product_product(models.Model):
    _inherit='product.product'
    spacefill_product=fields.Boolean('Prestashop Product')
