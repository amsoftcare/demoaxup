# -*- coding: utf-8 -*-
# from odoo import http


# class StockSpacefill(http.Controller):
#     @http.route('/stock_spacefill/stock_spacefill/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_spacefill/stock_spacefill/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_spacefill.listing', {
#             'root': '/stock_spacefill/stock_spacefill',
#             'objects': http.request.env['stock_spacefill.stock_spacefill'].search([]),
#         })

#     @http.route('/stock_spacefill/stock_spacefill/objects/<model("stock_spacefill.stock_spacefill"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_spacefill.object', {
#             'object': obj
#         })
