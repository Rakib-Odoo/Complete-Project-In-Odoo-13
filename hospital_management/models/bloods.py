from odoo import api, models, fields

class HospitalBlood(models.Model):
    _name = 'hospital.blood'
    _description = 'Hospital Blood Information'
    _rec_name = 'blood_grp'


    blood_grp = fields.Char(string='Blood Group', required=True)
    _sql_constraints = [('unique_blood','unique(blood_grp)',
                        'Blood Group Already Present!')]


class GeneticRisks(models.Model):
    _name = 'genetic.risk'
    _description = 'Genetic Risks'
    _rec_name = 'risks'

    risks = fields.Char(string='Genetic Risks', required=True)