from odoo import models,fields,api

class Visit(models.Model):
    _name = "student.visits"
    _description = "hospital visit account"

    student_id = fields.Many2one(comodel_name="student.profile" ,string="Student ID", required=True, ondelete="cascade")
    date = fields.Date(string="Date")
    symptoms = fields.Text(string="Symptoms")
    prescription = fields.One2many(comodel_name="student.prescription", string="Prescription",inverse_name="visit_id")
    description = fields.Text(string="True")
    doctor_id = fields.Many2one(comodel_name="hms.employee",string="Doctor")


