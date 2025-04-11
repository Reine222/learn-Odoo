# -*- coding: utf-8 -*-
from odoo import models, fields


class Suggestion(models.Model):
    _name = 'suggestion.suggestion'
    _description = 'model pour faire des suggestions'

    name = fields.Char(string='Nom')
    sujet = fields.Char(string='Sujet')
    description = fields.Text(string='description de la suggestion')
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

