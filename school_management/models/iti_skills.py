from odoo import models, fields, api

class ItiSkills(models.Model):
    _name = 'iti.skills'
    _description = 'Skills'

    name = fields.Char()