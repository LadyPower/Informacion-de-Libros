from datetime import datetime, timedelta
from odoo.tools.misc import DEFAULT_SERVER_DATE_FORMAT

from odoo import models, fields, api, _, tools
from odoo.exceptions import UserError
import logging

import io
from io import BytesIO

import xlsxwriter
import shutil
import base64
import csv
import xlwt

_logger = logging.getLogger(__name__)

class Impresion(models.TransientModel):
    _name = "reglib.impresion"

    autores = fields.Many2many('reglib.autores',)
    date_now = fields.Datetime(string='Date Now', default=lambda *a:datetime.now())    
    state = fields.Selection([('choose', 'choose'), ('get', 'get')],default='choose')
    report = fields.Binary('Prepared file', filters='.xls', readonly=True)
    name = fields.Char('File Name', size=50)
    company_id = fields.Many2one('res.company','Company',default=lambda self: self.env.user.company_id.id)
    
    def imprimir_pdf(self):
        return {'type': 'ir.actions.report','report_name': 'reg_libros.autores_variados','report_type':"qweb-pdf"}