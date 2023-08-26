
import pytest

from app import app

from model.produto import Produto

def test_index():
    response = app.test_client().get('/')

    assert response.status_code == 200

def test_listar():
    response = app.test_client().get('/listar')

    assert response.status_code == 200
    assert str(response.get_data(as_text=True)) is not None

def test_get_produto():
    
    pass

def test_cadastrar():
    
    formdata = {'formNomeProduto': 'Adidas Shoe', 'formPartNumber': 'AD2313', 'formLabelProduto': 'Adida Shoe Air',  'formStartInventory' : 100}
    response = app.test_client().post('/cadastrar', data=formdata)
   
    assert response.status_code == 200
    
    

