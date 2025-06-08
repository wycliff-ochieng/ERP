from odoo import models,fields



class Student(models.Model):
    _name = "student.profile"
    _description = "students health records"

    name = fields.Char(string="Name", required=True)
    birth_date = fields.Date(string="Date_Of_Birth")
    age = fields.Integer(string="Age")
    gender = fields.Selection([('female','Female'),('male','Male')],string="gender", required=True)
    allergies = fields.Char(string="Allergies", default=None)
    chronic_conditions = fields.Char(string="Chronic_Illness", default=None)
