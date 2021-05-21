from odoo import models,fields

class Libros(models.Model):
    _name = "reglib.libros"

    name = fields.Char("Título del libro")
    autor_id = fields.Many2one('reglib.autores')
    name_e = fields.Char("Editorial")
    num_e = fields.Integer("Edición")
    publ = fields.Integer("Año de publicación")
    status = fields.Selection(selection=[("disponible","Disponible"),("agotado","Agotado")])
    pertc = fields.Boolean("¿Pertenece a una colección?")
    coleccion_id = fields.Many2one('reglib.coleccion')
    num_t = fields.Integer("Número de tomo")
    portada = fields.Binary('Imagen de Portada')

class Autores(models.Model):
    _name = "reglib.autores"

    name = fields.Char("Autor del libro")
    libros_ids = fields.One2many('reglib.libros', inverse_name='autor_id', string="Libros")

class Coleccion(models.Model):
    _name = "reglib.coleccion"

    name = fields.Char("Nombre de la colección")
    libros_ids = fields.One2many('reglib.libros', inverse_name='coleccion_id', string="Libros")