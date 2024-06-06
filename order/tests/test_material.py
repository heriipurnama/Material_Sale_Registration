from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestMaterial(TransactionCase):

    def setUp(self):
        super(TestMaterial, self).setUp()
        self.supplier = self.env['res.partner'].create({
            'name': 'Test Supplier',
            'is_supplier': True
        })

    def test_create_material(self):
        material = self.env['material'].create({
            'material_code': 'M001',
            'material_name': 'Test Material',
            'material_type': 'fabric',
            'material_buy_price': 150,
            'supplier_id': self.supplier.id
        })
        self.assertEqual(material.material_code, 'M001')
        self.assertEqual(material.material_buy_price, 150)

    def test_create_material_invalid_price(self):
        with self.assertRaises(ValidationError):
            self.env['material'].create({
                'material_code': 'M002',
                'material_name': 'Invalid Material',
                'material_type': 'jeans',
                'material_buy_price': 50,
                'supplier_id': self.supplier.id
            })

    def test_update_material(self):
        material = self.env['material'].create({
            'material_code': 'M003',
            'material_name': 'Update Material',
            'material_type': 'cotton',
            'material_buy_price': 200,
            'supplier_id': self.supplier.id
        })
        material.write({
            'material_name': 'Updated Material Name'
        })
        self.assertEqual(material.material_name, 'Updated Material Name')

    def test_delete_material(self):
        material = self.env['material'].create({
            'material_code': 'M004',
            'material_name': 'Delete Material',
            'material_type': 'fabric',
            'material_buy_price': 300,
            'supplier_id': self.supplier.id
        })
        material_id = material.id
        material.unlink()
        material_check = self.env['material'].search([('id', '=', material_id)])
        self.assertFalse(material_check)
