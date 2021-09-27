from odoo import fields, models, exceptions, api, _


class ResPartnerExtension(models.Model):
    _inherit = 'res.partner'

    climbing_gym_main_member_membership_name = fields.Char(
        related='climbing_gym_main_member_membership_id.name',
    )
