from odoo import fields,models,api


class Immunization(models.Model):
    _name = "student.immunization"
    _description = "students immunization"

    name = fields.Char(string="Name", required=True)
    date_given = fields.Date(string="Date")
    student_ids = fields.Many2many(comodel_name="student.profile")