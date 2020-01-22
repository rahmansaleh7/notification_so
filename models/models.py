# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from . import time
from odoo.exceptions import UserError
form . import logging
_logger = logging.getLogger(__name__)

class Sale_order(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    @api.model
    def create(self, vals):
        self.add_followers(vals)
        new_id = super(Sale_order, self).create(vals)

        new_id.message_subscribe([x.partner_id.id for x in new_id.message_follower_ids])

        body = "SO Create, Please Check SO Now"
        new_id.send_followers(body)
        return new_id

    ###############################################
    # Menambah Followers di SO
    ###############################################

    def add_followers(self, vals):
        uid = self.env.uid
        group_ids = self.find_notif_users()
        partner_ids = []

        for group in group_ids:
            for user in group.users:
                if user.id != uid:
                    partner_ids.append(user.partner_id.id)

            if partner_ids:
                vals['message_follower_ids'] = [(0,0, {
                    'res_model' : 'sale.order',
                    'partner_id' : pid}) for pid in partner_ids]

    ###############################################
    # Mencari nama-nama group yang hendak di notif
    ###############################################

    def find_notif_users(self):
        group_obj = self.env['res.groups']
        group_ids = group_obj.sudo().search([('name', '=', 'Deposit Notification')])
        return group_ids