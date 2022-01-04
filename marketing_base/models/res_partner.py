# Copyright 2022 Xavier Bouquiaux
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, models
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = "res.partner"

    """create a constraint to restrict 2 active partner with the same email"""

    @api.constrains("email")
    def _check_email_unicity(self):
        for partner in self:
            emails = self.env["res.partner"].search(
                [("email", "=", partner.email), ("id", "!=", partner.id)]
            )
            if emails:
                raise ValidationError(_("Another partner exists with the same email"))
