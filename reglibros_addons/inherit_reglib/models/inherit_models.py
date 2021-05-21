from odoo import models,fields

class InheritRegLib(models.Model):
     _inherit = 'reglib.libros'
     
     opinion = fields.Text("Opinión sobre el libro")
     clasif = fields.Selection(selection=[("0","0"),("1","1"),("2","2"),("3","3"),("4","4"),("5","5")])