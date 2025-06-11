from odoo import models,fields,api



class Property(models.Model):
    _name="estate.property"
    _description="Table listing all properties of thr estate"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="PostCode")
    date_availability = fields.Date(string="Date", required=True)
    expected_price = fields.Float(string="Expected_Price", required=True)
    selling_price = fields.Float(string="Selling_Price")
    bedrooms = fields.Integer(string="Bedroom")
    living_area = fields.Integer(string="Living_Area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage", default=False)
    garden = fields.Boolean(string="Garden", default=False)
    garden_area = fields.Integer(string="Garden_Area")
    garden_orientation = fields.Selection([('north','North'),('south','South'),('east','East'),('west','west')])