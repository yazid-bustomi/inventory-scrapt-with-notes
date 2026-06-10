<div align="center">
  
# Inventory Scrap Note Integration

**Odoo Module to add an "Important Note" field in Inventory Scrap and automatically sync it with Accounting Journal Entries.**

[![License: LGPL-3](https://img.shields.io/badge/License-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Odoo Version](https://img.shields.io/badge/Odoo-15.0%20%7C%2016.0%20%7C%2017.0-green.svg)]()
[![Author](https://img.shields.io/badge/Author-A_Yazid_Bustomi-orange.svg)](https://www.bustomi.my.id/)

</div>

---

## 📝 Overview

This module extends the standard Odoo Stock Scrap functionality. It bridges the communication gap between the Inventory team and the Accounting team by ensuring that whenever an item is scrapped, the exact reason or important notes are carried over to the financial records.

When a scrap order is validated, any important notes are automatically appended to the resulting Inventory Valuation Journal Entry (`account.move`), making audits and financial tracking much easier.

## ✨ Features

1. **New "Important Notes" Field**: 
   Adds a new text field (`notes_journal_scrapt`) on the Stock Scrap form view (`stock.scrap`).
   
2. **Automated Journal Entry Update**: 
   Upon validation of the scrap order, the module automatically locates the corresponding Journal Entries generated for inventory valuation.
   
3. **Smart Reference Appending**: 
   The notes are seamlessly appended to the end of the standard "Reference" (`ref`) field on the Journal Entry. 
   - **Format**: `[Original Reference] - [Important Notes]`
   - **Example**: `Scrap - WH/SCRAP/0001 - Item damaged by forklift`

## ⚙️ Dependencies

Ensure the following modules are installed in your Odoo database before installing this module:
- `stock_account`
- `account`
- `om_inventory_receipts_it`

## 🚀 Installation

1. Clone or download this repository.
2. Place the `inventory_scrapt_notes` folder into your Odoo `addons` directory.
3. Restart your Odoo server service.
4. Log in to Odoo as an Administrator.
5. Activate **Developer Mode** (Settings > Activate the developer mode).
6. Go to the **Apps** menu.
7. Click on **Update Apps List** and confirm.
8. Remove the default "Apps" filter in the search bar.
9. Search for `Inventory Scrap`.
10. Click **Install**.

## 💻 Usage

1. Navigate to **Inventory > Operations > Scrap**.
2. Create a new Scrap Order.
3. Fill in the product, quantity, and other standard fields.
4. Fill in your reason/context in the new **Important Notes** field.
5. Click **Validate**.
6. Navigate to **Accounting > Accounting > Journal Entries**.
7. Find the newly created journal entry for the scrap operation.
8. Notice that the **Reference** column now includes your Important Notes.

## 🤝 Compatibility

- No dependencies on Odoo Studio. Custom `x_studio` logic has been completely removed for universal compatibility across all Odoo environments (Community & Enterprise).

## 📄 License

This module is licensed under **LGPL-3**.

---

<div align="center">
  <b>Developed with ❤️ by <a href="https://www.bustomi.my.id/">A Yazid Bustomi</a></b>
</div>
