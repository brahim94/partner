from odoo import api, fields, models


class account_payement_methode(models.Model):
    _name = "payement.methode"
    _rec_name = 'name'

    name = fields.Char('Nom')
    description = fields.Text('Description')
    image = fields.Binary("Icon", help="Select image here")

    
class tech_partner(models.Model):
    _inherit = "res.partner"

    if_id = fields.Char('IF')
    professional_tax = fields.Char('Taxe professionnelle')
    rc = fields.Char('RC')
    ice = fields.Char('ICE')
    cin = fields.Char('CIN')
    payment_methode_id = fields.Many2one('payement.methode', string='Mode de paiement')


