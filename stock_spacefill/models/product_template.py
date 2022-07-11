import pdb
from odoo import models, fields, api, exceptions, _
from odoo.addons.http_routing.models.ir_http import slugify
from odoo.addons.stock_spacefill.spacefillpy.api import API as API
from datetime import datetime



class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def create_spacefill(self, product,instance,setup):
        item_url = 'logistic_management/master_items/'
        spacefil_id = None
        #pdb.set_trace()

        vals= {
               # "id": "6f726d52-e1dc-4870-b0ed-7a777e83ba3e",
                "shipper_account_id": setup.spacefill_erp_account_id,
                "item_reference": product.default_code,
                "designation": product.name,
                "cardboard_box_quantity_by_pallet": None,
                "each_barcode_type": "EAN",
                "each_barcode":product.barcode,
                "cardboard_box_barcode_type": None,
                "cardboard_box_barcode": None,
                "pallet_barcode_type": None,
                "pallet_barcode": None,
                "each_quantity_by_cardboard_box": None,
                "each_quantity_by_pallet":None,
                "each_is_stackable": "true",
                "cardboard_box_is_stackable": "false",
                "pallet_is_stackable": "false",
                "each_width_in_cm": None,
                "each_length_in_cm": None,
                "each_height_in_cm": None,
                "each_volume_in_cm3": None,
                "cardboard_box_width_in_cm": None,
                "cardboard_box_length_in_cm": None,
                "cardboard_box_height_in_cm": None,
                "cardboard_box_volume_in_cm3": None,
                "pallet_width_in_cm": None,
                "pallet_length_in_cm": None,
                "pallet_height_in_cm": None,
                "pallet_gross_weight_in_kg": None,
                "pallet_net_weight_in_kg": None,
                "cardboard_box_gross_weight_in_kg": None,
                "cardboard_box_net_weight_in_kg": None,
                "each_gross_weight_in_kg": None,
                "each_net_weight_in_kg": None,
                "edi_erp_id": product.default_code,
                "edi_wms_id": None,
                "edi_tms_id": None,
                "transfered_to_erp_at":  datetime.utcnow().isoformat() + "Z",
                "transfered_to_wms_at": None,
                "transfered_to_tms_at": None,                
                }
        res= instance.create(instance.url+item_url, vals)
        self.write({'item_spacefill_id' : res.get('id')})  
       
    
    def export_product_in_spacefill(self):
            instance,setup = self.get_instance_spacefill()
            for product in self:
                product.create_spacefill(product,instance,setup)
    
    def get_instance_spacefill(self):
        setup = self.env['stock_spacefill.stock_spacefill'].search([])
        instance = API(setup.spacefill_api_url,
                       setup.spacefill_shipper_token)       
        return instance,setup