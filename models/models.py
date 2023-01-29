# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.product'

    coste = fields.Float(compute='_compute_costo', string='Costo Producto',store=True)
    
    @api.depends('stock_move_ids','stock_quant_ids')
    def _compute_costo(self):
        for p in self:
            coste=self.env['product.price.history'].search([('product_id','=',p.id)],order="datetime desc",limit=1)
            if coste:
                p.coste=coste.cost

    @api.model
    def _obtener_costo_producto(self):
        productos=self.env['product.product'].search([('type','=','product')])
        for p in productos:
            coste=self.env['product.price.history'].search([('product_id','=',p.id)],order="datetime desc",limit=1)
            if coste and coste.cost>0:
                p.coste=coste.cost

