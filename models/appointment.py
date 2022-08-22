from odoo import api,fields,models,tools

class HospitalAppointment(models.Model):
    _name ="hospital.appointment"
    _rec_name = "ref"
    patient_id = fields.Many2one('hospital.patient',string="Patient")
    ref = fields.Char(string="Reference")
    gender = fields.Selection(related="patient_id.gender",readonly=True)
    appointment_time = fields.Datetime(string="Appointment time")
    booking_date = fields.Date(string="booking Date")
    prescription = fields.Html(String="Doctor Prescription")
    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref
