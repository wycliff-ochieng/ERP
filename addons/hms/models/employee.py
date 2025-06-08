from odoo import models,fields,api


class HospitalEmployee(models.Model):
    _name = "hospital.employee"
    _description = "Hospiatl Employee"

    name=fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
    ], required=True, default='male')
    proffession = fields.Selection([
        ('doctor','Doctor'),
        ('nurse','Nurse'),
        ('pharmacist','Pharmacist')
    ])