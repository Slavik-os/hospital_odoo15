from odoo import api,fields,models,tools
from datetime import date

class HospitalPatient(models.Model):
    _name="hospital.patient"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = """
        Hospital learning module
    """

    name = fields.Char(string="name",tracking=True)
    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age",compute="_compute_age",tracking=True)
    gender = fields.Selection([("male","Male"),("female","Female")],string="Gender",tracking=True)
    ref = fields.Char(string="Reference",tracking=True)
    active = fields.Boolean(String="Active",default=True,tracking=True)
    appointment = fields.Many2one('hospital.appointment',String="Appointment")


    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else :
                rec.age = 0
