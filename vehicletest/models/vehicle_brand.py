# -*- coding: utf-8 -*-

from odoo import fields, models


class Vehicle_Brand(models.Model):
    _name = 'vehicletest_brand'
    _description = 'brand'

    name = fields.Char(
        string='Brand Name',
        required=True,
        help="Fill brand name"
        )

    description = fields.Text(
        string='Description',
        )

    active = fields.Boolean(
        string='Active'
        )
    
     

        