from odoo import fields, models, api
from odoo.exceptions import ValidationError

class CreateTrackWizard(models.TransientModel):
    _name = 'iti.create.track.wizard'
    _description = 'Create Track Wizard'

    track_no = fields.Char()
    category = fields.Selection([('open_source', 'Open Source'), ('erp', 'ERP'), ('java', 'Java')])
    duration = fields.Integer()

    def create_track(self):
        track = self.env['iti.track'].create({
            'track_no': self.track_no,
            'category': self.category,
            'duration': self.duration
        })
        return track
