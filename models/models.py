# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class tech_partner(models.Model):
#     _name = 'tech_partner.tech_partner'
#     _description = 'tech_partner.tech_partner'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
