# -*- coding: utf-8 -*-
from odoo import http

# class MethodCosteProduct(http.Controller):
#     @http.route('/method_coste_product/method_coste_product/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_coste_product/method_coste_product/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_coste_product.listing', {
#             'root': '/method_coste_product/method_coste_product',
#             'objects': http.request.env['method_coste_product.method_coste_product'].search([]),
#         })

#     @http.route('/method_coste_product/method_coste_product/objects/<model("method_coste_product.method_coste_product"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_coste_product.object', {
#             'object': obj
#         })