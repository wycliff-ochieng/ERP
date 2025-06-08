from odoo import models,fields,api

class Prescription(models.Model):
    _name = "student.prescription"
    _description = "prescription given to students"

    visit_id = fields.Many2one(comodel_name="student.visits",string="Visit ID",  ondelete="cascade")
    medicine = fields.Char(string="Medicine")
    dosage = fields.Text(string="Dosage", required=True)
    frequency = fields.Char(string="Frequency")
    duration = fields.Integer(string="Duration")