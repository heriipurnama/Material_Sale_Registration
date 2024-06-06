from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Material(models.Model):
    _name = 'material'
    _description = 'Material'

    material_code = fields.Char(string='Material Code')
    material_name = fields.Char(string='Material Name')
    material_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')
    ], string='Material Type')
    material_buy_price = fields.Float(string='Material Buy Price')
    supplier_id = fields.Many2one('res.partner', string='Related Supplier')
    
    # @api.constrains('material_buy_price')
    # def _check_material_buy_price(self):
    #     for record in self:
    #         print("==================" , record)
    #         print("==================" , record.material_buy_price)
    #         print("==================" , record.material_type)

    #         if record.material_buy_price < 100:
    #             raise ValidationError('Material buy price cannot be less than 100.')
