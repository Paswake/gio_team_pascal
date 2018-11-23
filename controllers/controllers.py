# -*- coding: utf-8 -*-
from odoo import http

# class GioTeamPascal(http.Controller):
#     @http.route('/gio_team_pascal/gio_team_pascal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gio_team_pascal/gio_team_pascal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gio_team_pascal.listing', {
#             'root': '/gio_team_pascal/gio_team_pascal',
#             'objects': http.request.env['gio_team_pascal.gio_team_pascal'].search([]),
#         })

#     @http.route('/gio_team_pascal/gio_team_pascal/objects/<model("gio_team_pascal.gio_team_pascal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gio_team_pascal.object', {
#             'object': obj
#         })