# -*- coding: utf-8 -*-
from odoo import http

class MyModule(http.Controller):
    @http.route('/real_estate_inventory/project/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/real_estate_inventory/project/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('real_estate_inventory.listing', {
            'root': '/real_estate_inventory/project',
            'objects': http.request.env['real_estate_inventory.project'].search([]),
        })

    @http.route('/real_estate_inventory/project/objects/<model("real_estate_inventory.project"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('real_estate_inventory.object', {
            'object': obj
        })