# -*- coding: utf-8 -*-
from odoo import http

# class NotificationSo(http.Controller):
#     @http.route('/notification_so/notification_so/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/notification_so/notification_so/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('notification_so.listing', {
#             'root': '/notification_so/notification_so',
#             'objects': http.request.env['notification_so.notification_so'].search([]),
#         })

#     @http.route('/notification_so/notification_so/objects/<model("notification_so.notification_so"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('notification_so.object', {
#             'object': obj
#         })