# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PreferredAreas(models.Model):
    _name='real_estate_inventory.preferred_area'
    name = fields.Char( string = "area")
    

class Project(models.Model):
    _name = 'real_estate_inventory.project'
    name = fields.Char()
    location_id = fields.Many2one('real_estate_inventory.preferred_area', string='project_location')



class Building(models.Model):
    _name = 'real_estate_inventory.building'
    name = fields.Char()
    project_id = fields.Many2one('real_estate_inventory.project', string='project')
    number = fields.Char()
    block_number = fields.Char()
    phase = fields.Integer('phase')
    

class RealEstateUnit(models.Model):
     _name = 'real_estate_inventory.unit'
    _inherit = 'product.product'
    unit_building_id = fields.Many2one('real_estate_inventory.building', string='Building')
    unit_code = fields.Char('Code')
    view = fields.Char('View')
    unit_status =  fields.Selection([
        ('available', 'available'),
        ('on hold', 'on_hold'),
        ('mockup', 'mockup'),
        ('sold', 'sold'),

    ], string='unit_status')
    contract_status = fields.Selection([
        ('none', 'none'),
        ('contract signed','contract_signed'),
        ('booked','booked')
    ], string='contract_status')
    unit_type = fields.Selection([
        ('apartment', 'apartment'),
        ('twinhouse','twinhouse'),
        ('townhouse','townhouse')
        
    ], string='unit_type')
    unit_number = fields.Integer('Unit Number')
    unit_floor = fields.Integer('Floor #')
    unit_area = fields.Integer('Unit Area')
    unit_extra_area = fields.Integer('Extra Area')
    unit_cash_price  = fields.Float('Cash Price')
    # main_owner_id = fields.Many2one('res.partner', string='main_owner')
 

# class real_estate_inventory(models.Model):
#     _name = 'real_estate_inventory.real_estate_inventory'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
        
        