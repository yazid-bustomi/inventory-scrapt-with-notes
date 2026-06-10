{
    'name': 'OM Inventory Scrap',
    'version': '1.0',
    'summary': 'Add field Important Note in Inventory Scrap',
    'description': '''
        OM Inventory Scrap Note Integration
        ===================================
        This module extends the Odoo Stock Scrap functionality:
        
        1. Adds an "Important Notes" (notes_journal_scrapt) field to the Stock Scrap model.
        2. Automatically transfers these notes to the corresponding Inventory Valuation Journal Entries (account.move) upon validation.
           - Appends the notes to the end of the standard "ref" (Reference) field of the journal entry (e.g. "Scrap - WH/SCRAP/0001 - <Important Notes>").
        3. Exposes the "Important Notes" field on the Stock Scrap form view.
    ''',
    'author': 'A Yazid Bustomi',
    'website': 'https://www.bustomi.my.id/',
    'license': 'LGPL-3',
    'depends': [ 'stock_account', 'account', 'om_inventory_receipts_it'],
    "data": [
        "views/stock_scrap_form_views.xml",
    ],
    'installable': True,
    'auto_install': False
}
