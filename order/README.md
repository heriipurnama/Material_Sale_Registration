# Material Sale Registration Module for Odoo 14

This Odoo module allows users to manage materials for sale, including the creation, updating, and deletion of materials. It includes features such as material registration, supplier association, and filtering by material type.

## Features

- Material Registration
  - Material Code
  - Material Name
  - Material Type (Fabric, Jeans, Cotton)
  - Material Buy Price (must be >= 100)
  - Related Supplier

- Material Management
  - View all materials
  - Filter materials by type
  - Update material information
  - Delete materials

## Directory Structure

- **ERD**: Located in the `ERD/` directory.
- **Addon**: Located in the `order/` directory.

## Installation

1. Ensure you have Odoo 14 installed.
2. Clone this repository into your Odoo addons directory:
    ```bash
    git clone https://github.com/heriipurnama/Material_Sale_Registration.git
    ```
3. Update the Odoo module list and install the Material Sale Registration module:
    - Go to the Odoo web interface.
    - Navigate to `Apps`.
    - Click on the `Update Apps List` button.
    - Search for `Material Sale Registration` and click `Install`.

## Usage

### Creating a Material

1. Send a POST request to `http://localhost:8069/material` with the following JSON payload:
    ```json
    {
      "material_code": "M001",
      "material_name": "Test Material",
      "material_type": "fabric",
      "material_buy_price": 150,
      "supplier_id": 1
    }
    ```
2. Ensure to include the session ID in the request headers for authentication:
    ```plaintext
    Content-Type: application/json
    Cookie: session_id=your_session_id_value
    ```

### Example Using Postman

1. **Login to Odoo**:
    - **URL**: `http://localhost:8069/web/session/authenticate`
    - **Method**: POST
    - **Headers**:
        ```plaintext
        Content-Type: application/json
        ```
    - **Body**:
        ```json
        {
          "jsonrpc": "2.0",
          "params": {
            "db": "your_database_name",
            "login": "your_username",
            "password": "your_password"
          }
        }
        ```
    - Copy the `session_id` from the response cookies.

2. **Create Material**:
    - **URL**: `http://localhost:8069/material`
    - **Method**: POST
    - **Headers**:
        ```plaintext
        Content-Type: application/json
        Cookie: session_id=your_session_id_value
        ```
    - **Body**:
        ```json
        {
          "material_code": "M001",
          "material_name": "Test Material",
          "material_type": "fabric",
          "material_buy_price": 150,
          "supplier_id": 1
        }
        ```

## Unit Testing

### Running Tests

1. Ensure you have `unittest` and other necessary testing dependencies installed.
2. Navigate to your Odoo directory and run the following command to execute the tests:
    ```bash
    odoo --test-enable --stop-after-init -i material_sale_registration
    ```

### Example Test

```python
from odoo.tests import common

class TestMaterial(common.TransactionCase):

    def test_material_creation(self):
        # Create a test supplier
        supplier = self.env['res.partner'].create({
            'name': 'Test Supplier',
        })

        # Create a material
        material = self.env['material'].create({
            'material_code': 'M001',
            'material_name': 'Test Material',
            'material_type': 'fabric',
            'material_buy_price': 150,
            'supplier_id': supplier.id
        })

        # Assert material creation
        self.assertEqual(material.material_code, 'M001')
        self.assertEqual(material.material_name, 'Test Material')
        self.assertEqual(material.material_type, 'fabric')
        self.assertEqual(material.material_buy_price, 150)
        self.assertEqual(material.supplier_id, supplier)
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.