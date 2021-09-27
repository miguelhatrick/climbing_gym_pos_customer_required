{
    'name': 'climbing_gym_pos_customer_required',
    'version': '12.0.1.0.1',
    'category': 'Point Of Sale',
    'summary': 'Point of Sale Require Customer / membership',
    'author': "Miguel Hatrick",
    'website': 'https://www.dacosys.com',
    'license': 'AGPL-3',
    'depends': [
        'point_of_sale',
        'pos_customer_required',
        'climbing_gym'
    ],
    'data': [
        'static/src/xml/templates.xml',
    ],
    'installable': True,
    'qweb': [
        'static/src/xml/pos_partner.xml',

    ],
}
