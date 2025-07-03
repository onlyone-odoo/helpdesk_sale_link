from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    ticket_ids = fields.Many2many("helpdesk.ticket", string="Tickets")
