# -*- coding: utf-8 -*-
#############################################################################


##############################################################################

from odoo import api, fields, models, _
from odoo.addons.stock_spacefill.spacefillpy.api import API as API
from datetime import date, datetime
import pdb

class SaleOrder(models.Model):
    _inherit = "sale.order"       

    def action_confirm(self): 
        res= super(SaleOrder, self).action_confirm() 
       # pdb.set_trace()
        for order in self:
            picking = self.env['stock.picking'].search([('origin','=',order.name)])
            #self.export_order_exit_in_spacefill(picking)
            instance,setup = order.get_instance_spacefill()
            order.create_order_exit_spacefill(instance,picking)
        return res
   
    def create_order_exit_spacefill(self,instance,picking):
        item_url = 'logistic_management/orders/exit/'
        spacefil_id = None
        order=[]
        order_items=[]
       
        order_values= {                       
                           "shipper_order_reference": picking.name,
                            "warehouse_id": "fca9ad8c-d000-40ad-97b8-74a29f7696e0",#picking.location --> wh --> guid :todo
                            "comment": "exit from odoo",
                            "planned_execution_datetime_range": {
                                "datetime_from": "2025-09-28T15:12:41.538Z",
                                "datetime_to": "2025-09-28T15:12:41.538Z"
                            },
                            "carrier_name":None,
                            "carrier_phone_number": None,
                            "transport_management_owner": "PROVIDER",
                            "exit_final_recipient":"TEST", #picking.partner_id.name,
                            "exit_final_recipient_address_line1": None,
                            "exit_final_recipient_address_line2": None,
                            "exit_final_recipient_address_line3": None,
                            "exit_final_recipient_address_zip": None,
                            "exit_final_recipient_address_details": None,
                            "exit_final_recipient_address_city": None,
                            "exit_final_recipient_address_country": None,
                            "exit_final_recipient_address_lat": None,
                            "exit_final_recipient_address_lng": None,
                            "exit_final_recipient_planned_datetime_range": {
                                "datetime_from": "2025-09-28T15:12:41.538Z",
                                "datetime_to": "2025-09-28T15:12:41.538Z"
                            },
                            "edi_erp_id": picking.name,
                            "edi_wms_id": None,
                            "edi_tms_id": None,
                            "transfered_to_erp_at": datetime.utcnow().isoformat() + "Z",
                            "transfered_to_wms_at": None,
                            "transfered_to_tms_at": None,                        
                    }        
        
        for line in picking.move_line_ids:
            order_lines_values = {}
            order_lines_values['master_item_id'] = line.product_id.item_spacefill_id #need to update with id space fill on response
            order_lines_values["item_packaging_type"] = "EACH"# self.get_item_packaging_type(item)
            order_lines_values["expected_quantity"] = line.product_uom_qty
            order_items.append(
                order_lines_values
            )
        order_values.update({"order_items": order_items})       
        instance.create(instance.url+item_url, order_values)
    
    def export_order_exit_in_spacefill(self,picking):
            instance,setup = self.get_instance_spacefill()
            self.create_order_exit_spacefill(instance,picking)
    
    def get_instance_spacefill(self):
        setup = self.env['stock_spacefill.stock_spacefill'].search([])
        instance = API(setup.spacefill_api_url,
                       setup.spacefill_shipper_token)        
        return instance,setup

 