# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import  api, fields, models
from odoo.exceptions import ValidationError
class TravelPlaces(models.Model):
    _name='travel.places'
    name=fields.Char(string="place")
    # meal_id= fields.Many2one('travel.meals')
    sequence= fields.Integer(string="sequence",default=10)
    code= fields.Char(string="place code")

    @api.multi
    def name_get(self):
        res = super(TravelPlaces, self).name_get()
        data=[]
        for place in self:
            display_value=''
            display_value+= place.name or""
            display_value+='['
            display_value+= place.code or""
            display_value+=']'
            data.append((place.id,display_value))
        return data
    @api.one
    @api.constrains('name')
    def unique_constraint(self):
        if len(self.search([('name', '=', self.name)])) > 1:
            raise ValidationError("Name already exists and violates unique field constraint")

class TravelPlacesMeals(models.Model):
    _name='travel.meals'
    name=fields.Char('Meal Name')
    meal_date = fields.Datetime('Meal Date')
    place_id = fields.Many2many('travel.places','Place')
    user_id = fields.Many2one('res.users','Meal User')
    notes = fields.Text('Meal Notes')
