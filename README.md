# OM Inventory Scrap Note Integration

## Overview

This Odoo module extends the standard Inventory Scrap functionality by adding an "Important Notes" field. It ensures that when a scrap order is validated, any important notes are automatically carried over to the resulting Inventory Valuation Journal Entry (`account.move`).

This is particularly useful for accounting and inventory teams who need to understand the context or reason for a scrap directly from the financial journal entries, without having to navigate back to the original stock scrap document.

## Features

1. **Important Notes Field**: Adds a new text field `notes_journal_scrapt` labeled "Important Notes" on the Stock Scrap form view.
2. **Automated Journal Entry Update**: Upon validation of the scrap order, the module automatically finds the corresponding Journal Entries generated for inventory valuation.
3. **Reference Appending**: The notes are appended to the end of the standard "Reference" (`ref`) field on the Journal Entry. 
   * Format: `[Original Reference] - [Important Notes]`
   * Example: `Scrap - WH/SCRAP/0001 - Item damaged during transit`

## Installation

1. Clone or download this repository.
2. Place the `om_inventory_scrap_it` folder into your Odoo `addons` directory.
3. Restart your Odoo server service.
4. Log in to Odoo as an Administrator.
5. Activate **Developer Mode** (Settings > Activate the developer mode).
6. Go to the **Apps** menu.
7. Click on **Update Apps List** and confirm.
8. Remove the default "Apps" filter in the search bar.
9. Search for `OM Inventory Scrap` or `om_inventory_scrap_it`.
10. Click **Install**.

## Usage

1. Navigate to **Inventory > Operations > Scrap**.
2. Create a new Scrap Order.
3. Fill in the product, quantity, and other standard fields.
4. Fill in your reason/context in the new **Important Notes** field.
5. Click **Validate**.
6. Navigate to **Accounting > Accounting > Journal Entries**.
7. Find the newly created journal entry for the scrap operation.
8. Notice that the **Reference** column now includes your Important Notes.

## Compatibility

- No dependencies on Odoo Studio (`x_studio` fields have been removed for universal compatibility).
- Depends on `stock_account`, `account`, and `om_inventory_receipts_it`.

## License

This module is licensed under LGPL-3.

## Author

**A Yazid Bustomi**
* Website: [https://www.bustomi.my.id/](https://www.bustomi.my.id/)
