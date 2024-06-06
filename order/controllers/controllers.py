from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class MaterialController(http.Controller):

    @http.route('/material', type='json', auth='user', methods=['POST'])
    def create_material(self, **kwargs):
        # Log the incoming data for debugging
        _logger.info('Incoming data: %s', kwargs)
        
        material = request.env['material'].create({
            'material_code': kwargs.get('material_code'),
            'material_name': kwargs.get('material_name'),
            'material_type': kwargs.get('material_type'),
            'material_buy_price': kwargs.get('material_buy_price'),
            'supplier_id': kwargs.get('supplier_id')
        })
        
        # Log the created material
        _logger.info('Created material: %s', material)

        return {'material_id': material.id}


    @http.route('/material', type='json', auth='user', methods=['GET'])
    def list_materials(self, **kwargs):
        materials = request.env['material'].search([])
        return [{'id': mat.id, 'material_code': mat.material_code, 'material_name': mat.material_name, 'material_type': mat.material_type, 'material_buy_price': mat.material_buy_price, 'supplier_id': mat.supplier_id.name} for mat in materials]

    @http.route('/material/<int:material_id>', type='json', auth='user', methods=['PUT'])
    def update_material(self, material_id, **kwargs):
        material = request.env['material'].browse(material_id)
        if material:
            material.write({
                'material_code': kwargs.get('material_code'),
                'material_name': kwargs.get('material_name'),
                'material_type': kwargs.get('material_type'),
                'material_buy_price': kwargs.get('material_buy_price'),
                'supplier_id': kwargs.get('supplier_id')
            })
            return {'status': 'success'}
        return {'status': 'fail'}

    @http.route('/material/<int:material_id>', type='json', auth='user', methods=['DELETE'])
    def delete_material(self, material_id, **kwargs):
        material = request.env['material'].browse(material_id)
        if material:
            material.unlink()
            return {'status': 'success'}
        return {'status': 'fail'}

    @http.route('/material/filter', type='json', auth='user', methods=['GET'])
    def filter_materials(self, **kwargs):
        material_type = kwargs.get('material_type')
        materials = request.env['material'].search([('material_type', '=', material_type)])
        return [{'id': mat.id, 'material_code': mat.material_code, 'material_name': mat.material_name, 'material_type': mat.material_type, 'material_buy_price': mat.material_buy_price, 'supplier_id': mat.supplier_id.name} for mat in materials]
