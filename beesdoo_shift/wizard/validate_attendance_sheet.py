# -*- coding: utf-8 -*-
from openerp import models, fields, api, exceptions, _
from openerp.exceptions import UserError, ValidationError


class ValidateAttendanceSheet(models.TransientModel):
    _name = "beesdoo.shift.sheet.validate"
    _description = """Check the user name and validate sheet.
    Useless for users in group_cooperative_admin"""
    _inherit = ["barcodes.barcode_events_mixin"]

    barcode = fields.Char(string="Barcode", required=True)
    annotation = fields.Text(
        "Important information requiring permanent member assistance", default=""
    )
    feedback = fields.Text(
        "General feedback"
    )
    worker_nb_feedback = fields.Selection(
        [
            ("not_enough", "Not enough"),
            ("enough", "Enough"),
            ("too_many", "Too many"),
        ],
        string="Number of workers",
        required=True
    )

    @api.multi
    def validate_sheet(self):
        sheet_id = self._context.get("active_id")
        sheet_model = self._context.get("active_model")
        sheet = self.env[sheet_model].browse(sheet_id)
        card = self.env["member.card"].search(
            [("barcode", "=", self.barcode)]
        )
        if not len(card):
            raise UserError("Please set a correct barcode.")
        user = card[0].partner_id
        if not user:
            raise UserError(
                "Only super-cooperators and administrators can validate attendance sheets."
            )
        sheet.annotation = self.annotation
        sheet.feedback = self.feedback
        sheet.worker_nb_feedback = self.worker_nb_feedback
        sheet.validated_by = user
        sheet.validate()

    def on_barcode_scanned(self, barcode):
        self.barcode = barcode