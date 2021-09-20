# Copyright (C) 2016-Today: La Louve (<http://www.lalouve.net/>)
# Copyright (C) 2019-Today: Druidoo (<https://www.druidoo.io>)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import models, api, _
from odoo.exceptions import UserError


class PosMakePayment(models.TransientModel):
    _inherit = 'pos.make.payment'

    @api.multi
    def check(self):
        # Load current order
        order_obj = self.env['pos.order']
        order = order_obj.browse(self.env.context.get('active_id', False))

        # Check if control is required
        if not order.partner_id \
                and order.session_id.config_id.require_customer != 'no':
            raise UserError(_(
                "An anonymous order cannot be confirmed.\n"
                "Please select a customer for this order. <---"))

        for line in order.lines:
            if line.product_id.climbing_gym_only_members:
                # only members

                if order.partner_id is None or order.partner_id.climbing_gym_main_member_membership_id is None or len(
                        order.partner_id.climbing_gym_main_member_membership_id) == 0:
                    raise UserError('Product only available for climbing gym members: %s' % line.product_id.name)

                if line.product_id.climbing_gym_only_active_members and \
                        order.partner_id.climbing_gym_main_member_membership_id.state not in ['active']:
                    raise UserError(
                        'Product only available for ACTIVE climbing gym members: %s Membership: %s\n status: %s\n Due date %s' % (
                            line.product_id.name,
                            order.partner_id.climbing_gym_main_member_membership_id.name,
                            order.partner_id.climbing_gym_main_member_membership_id.state,
                            order.partner_id.climbing_gym_main_member_membership_id.due_date))

            return super(PosMakePayment, self).check()
