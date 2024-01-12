from odoo import fields, models

class Couser(models.Model):
    _name = "academy.course"
    _description = "Couser Info"

    name = fields.Char(string="Titulo", required=True)
    active = fields.Boolean(string="Activo",default=True)
    description = fields.Text()
    level = fields.Selection(string="Nivel",
                             selection=[
                                 ('beginner','Beginner'),
                                 ('intermediate','Intermediate'),
                                 ('advanced','Advance'),
                             ],
                             copy=False)
    