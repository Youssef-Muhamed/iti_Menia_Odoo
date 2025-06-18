from odoo import fields, models, api

class Track(models.Model):
    _name = 'iti.track'
    _description = 'Track'
    _rec_name = 'track_no'

    track_no = fields.Char()
    category = fields.Selection([('open_source', 'Open Source'), ('erp', 'ERP'), ('java', 'Java')],)
    duration = fields.Integer()
    student_ids = fields.One2many('iti.students', 'track_id')

    def add_student(self):
        # students = self.env['iti.students'].search([]).ids
        students = self.env['iti.students'].search([]).mapped('id')
        students_obj = self.env['iti.students'].browse(students).filtered(lambda s: s.id == 13)
        # self.write({'student_ids': [(5,)]})
        # stude_dict = {
        #     'name': 'Ahmed',
        #     'email': 'a@b.com',
        #     'mobile': '011',
        #         'notes': 'test',
        #     'track_id': self.id,
        # }
        # self.write({'student_ids': [(0, 0, stude_dict)]})
        self.write({'student_ids': [(4, students_obj)]})
        print("students_obj -------",students_obj.name)