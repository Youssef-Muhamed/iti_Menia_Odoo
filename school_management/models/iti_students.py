from odoo import fields, models, api,_
from odoo.exceptions import ValidationError


class ItiStudents(models.Model):
    _name = 'iti.students'
    _description = 'Students'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Student Name', tracking=True,copy=False)
    email = fields.Char()
    mobile = fields.Char(default='011', readonly=True)
    description = fields.Text()
    notes = fields.Html()
    # domain = [('category', '=', 'open_source')],
    track_id = fields.Many2one('iti.track', tracking=True)
    birthday = fields.Datetime(string='Birthday')
    age = fields.Integer(compute='_compute_age', )
    category = fields.Selection([('open_source', 'Open Source'), ('erp', 'ERP'), ('java', 'Java')],
                                related='track_id.category', store=True)
    skills_ids = fields.Many2many('iti.skills')
    salary = fields.Float()
    state = fields.Selection(
        [('draft', 'Draft'), ('in_progress', 'In Progress'), ('accepted', 'Accepted'),
         ('rejected', 'Rejected')], default='draft',tracking=True)

    # _sql_constraints = [
    #     ('email_unique', 'unique(email)', 'Email must be unique'),
    #     ('check_salary', 'check(salary > 1000)', 'Salary must be greater than 1000')
    # ]

    # @api.constrains('email')
    # def _check_email(self):
    #     for record in self:
    #         if record.email and '@' not in record.email:
    #             raise ValidationError(_('Email must contain @'))

    @api.constrains('salary')
    def _check_salary(self):
        for record in self:
            if record.salary < 1000:
                raise ValidationError(_('Salary must be greater than 1000'))

    # @api.onchange('birthday')
    # def _onchange_birthday(self):
    #     print("onchange birthday -------")
    #     if self.birthday:
    #         self.age = fields.Date.today().year - self.birthday.year
    @api.depends('birthday')
    def _compute_age(self):
        for record in self:
            if record.birthday:
                # self.age = self.birthday.year - self.birthday.year
                record.age = fields.Date.today().year - record.birthday.year
            else:
                record.age = 0

    def action_accept(self):
        self.state = 'accepted'

    def action_reject(self):
        self.state = 'rejected'

    def action_in_progress(self):
        self.state = 'in_progress'

    def action_reset_to_draft(self):
        self.state = 'draft'


    @api.model
    def create(self, vals):
        print("create student -------",vals)
        if vals.get('email') and '@' not in vals['email']:
            vals['email'] += '@gmail.com'
        return super(ItiStudents, self).create(vals)

    def write(self, vals):
        print("write student -------",vals)
        if vals.get('email') and '@' not in vals['email']:
            vals['email'] += '@gmail.com'
        return super(ItiStudents, self).write(vals)

    def unlink(self):
        print("unlink student -------")
        return super(ItiStudents, self).unlink()


    def copy(self, default=None):
        print("copy student -------")
        return super(ItiStudents, self).copy(default)

    def action_open_track(self):
        # action = self.env.ref('school_management.action_create_track').read()[0]
        # print("action_open_track -------",action)
        # return action
        view = self.env.ref('school_management.iti_students_form_view').id
        tracks = self.env['iti.track'].search([('category', '=', 'open_source')])
        print("action_open_track -------",tracks.read())
        return {
            'type': 'ir.actions.act_window',
            'name': _('Create Track'),
            'views': [(self.env.ref("school_management.create_track_wizard_view").id, 'form')],
            'res_model': 'iti.create.track.wizard',
            'target': 'new',
        }

        # return action
    def add_skill_hard_work(self):
        # skill = self.env['iti.skills'].search([('id', '=', 3)])
        skill = self.env['iti.skills'].browse([3])
        self.skills_ids |= skill
        print("add_skill_hard_work -------",skill)
        # self.write({'skills_ids': [(4, self.env.ref('school_management.skill_hard_work').id)]/})








# inhertance
# python inheritance
# model inhertance
# view inhertance
