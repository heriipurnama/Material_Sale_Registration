from odoo import models, fields

class Supplier(models.Model):
    _inherit = 'res.partner'
    
    is_supplier = fields.Boolean(string='Is Supplier', default=True)
    material_ids = fields.One2many('material', 'supplier_id', string='Materials')
