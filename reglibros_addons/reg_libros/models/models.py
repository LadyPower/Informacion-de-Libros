from odoo import models,fields

class Libros(models.Model):
    _name = "reglib.libros"

    name = fields.Char("Título del libro",required = True)
    autor_id = fields.Many2one('reglib.autores',required = True)
    name_e = fields.Char("Editorial",required = True)
    num_e = fields.Integer("Edición")
    publ = fields.Integer("Año de publicación")
    status = fields.Selection(selection=[("disponible","Disponible"),("agotado","Agotado")],required = True)
    pertc = fields.Boolean("¿Pertenece a una colección?")
    coleccion_id = fields.Many2one('reglib.coleccion', string="Colección")
    num_t = fields.Integer("Número de tomo")
    portada = fields.Binary('Imagen de Portada')

class Autores(models.Model):
    _name = "reglib.autores"

    name = fields.Char("Autor del libro", required = True)
    libros_ids = fields.One2many('reglib.libros', inverse_name='autor_id', string="Libros")

class Coleccion(models.Model):
    _name = "reglib.coleccion"

    name = fields.Char("Nombre de la colección", required = True)
    libros_ids = fields.One2many('reglib.libros', inverse_name='coleccion_id', string="Libros")