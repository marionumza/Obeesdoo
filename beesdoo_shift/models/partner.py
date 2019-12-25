
from odoo import models, fields, api, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_worker = fields.Boolean(string="is Worker")
    cooperator_type = fields.Selection([('share_a', 'Share A'), ('share_b', 'Share B'), ('share_c', 'Share C')], store=True, compute=None)