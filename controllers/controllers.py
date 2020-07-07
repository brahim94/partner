# -*- coding: utf-8 -*-
# from odoo import http


# class TechPartner(http.Controller):
#     @http.route('/tech_partner/tech_partner/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tech_partner/tech_partner/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tech_partner.listing', {
#             'root': '/tech_partner/tech_partner',
#             'objects': http.request.env['tech_partner.tech_partner'].search([]),
#         })

#     @http.route('/tech_partner/tech_partner/objects/<model("tech_partner.tech_partner"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tech_partner.object', {
#             'object': obj
#         })
