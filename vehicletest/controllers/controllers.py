# -*- coding: utf-8 -*-
# from odoo import http


# class Vehicletest(http.Controller):
#     @http.route('/vehicletest/vehicletest/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vehicletest/vehicletest/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vehicletest.listing', {
#             'root': '/vehicletest/vehicletest',
#             'objects': http.request.env['vehicletest.vehicletest'].search([]),
#         })

#     @http.route('/vehicletest/vehicletest/objects/<model("vehicletest.vehicletest"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vehicletest.object', {
#             'object': obj
#         })
