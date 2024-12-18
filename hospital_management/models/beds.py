from odoo import api, fields, models


class HospitalBed(models.Model):
    _name = 'hospital.bed'
    _description = 'Hospital Bed Information'

    bed_no = fields.Integer(string='Bed No', required=True)
    bed_type = fields.Selection([('gatch', 'Gatch Bed'),
                                 ('electric', 'Electric'),
                                 ('stretcher', 'Stretcher'),
                                 ('low', 'Low Bed'),
                                 ('air', 'Low Air Loss'),
                                 ('circo', 'Circo Electric'),
                                 ('clinitron', 'Clinitron'),
                                 ], string='Bed Type')
    note = fields.Text(string='Notes')
    date_bed_assign = fields.Date(default=fields.Date.today, string='Assign Date')
    bed_rent = fields.Float(string='Bed Rent', help='The charge for the bed')
    repair_date = fields.Date(string='Repair Date', help='The next repair date')
    repair_charge = fields.Float(string='Repair Charge', help="The repairing charge whether any damage is happened")
    state = fields.Selection([
        ('available','Available'),
        ('unavailable', 'Unavailable')
    ], string='Status', default='available')