from odoo import _, api, fields, models

class StockScrap(models.Model):
    _inherit = 'stock.scrap'

    notes_journal_scrapt = fields.Text(
        'Important Notes'
    )    

    def action_validate(self):
        res = super().action_validate()
        for scrap in self:
            if scrap.notes_journal_scrapt and scrap.move_ids:
                # Find the account.move record(s) linked to scrap.move_ids
                account_moves = self.env['account.move'].search([('stock_move_id', '=', scrap.move_ids.id)])
                for move in account_moves:
                    # Append the notes to the end of the ref field
                    new_ref = f"{move.ref} - {scrap.notes_journal_scrapt}" if move.ref else scrap.notes_journal_scrapt
                    move.write({'ref': new_ref})
        return res
