
import logging
import pdb
from turtle import pendown
from odoo import models, fields, api, exceptions, _
from odoo.addons.stock_spacefill.spacefillpy.api import API as API

_logger = logging.getLogger(__name__)


class ProductProduct(models.Model):
    _inherit = 'product.product'
#    @api.model
#    def create(self, vals):
#       res = super(ProductProduct, self).create(vals)        
#       res= self.create_spacefill(res)
#        return res

    def create_spacefill(self, product):
        self.item_url = 'logistic_management/master_items/'
        self.spacefil_id = None
        self.token ='63226053c-cd7d-4v43-981e-d24ab10c1cd7'
        self.url='https://api.sandbox.spacefill.fr/v1/'
        self.shipper_id= '595afc1d-6a03-48f3-b36c-69feb7d6fb67'
        instance = API(self.url,
                       self.token)
        vals= {
               # "id": "6f726d52-e1dc-4870-b0ed-7a777e83ba3e",
                "shipper_account_id": self.shipper_id,
                "item_reference": product.name,
                "designation": product.name,
                "cardboard_box_quantity_by_pallet": None,
                "each_barcode_type": "EAN",
                "each_barcode": None, #product.barcode,
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
                "edi_erp_id": product.name,
                "edi_wms_id": None,
                "edi_tms_id": None,
                "transfered_to_erp_at": "2022-04-25T09:43:07.742Z",
                "transfered_to_wms_at": "2022-04-25T09:43:07.742Z",
                "transfered_to_tms_at": "2022-04-25T09:43:07.742Z",
                "metadata": {
                    "internal_code": "A2NJ34-034",
                    "driver_licence_plate": "XX-123-XX",
                    "plant": "My plant"
                }
                }
        instance.create(self.url+self.item_url, vals)