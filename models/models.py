# -*- coding: utf-8 -*-

from odoo import models, fields


class firstmodule(models.Model):
    _name = 'firstmodule.firstmodule'
    _description = 'firstmodule.firstmodule'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    extra_field1 = fields.Char(string='New fiield')
    one_more_field = fields.Char(string='Another one')
    date_field = fields.Date(string='Date field')
