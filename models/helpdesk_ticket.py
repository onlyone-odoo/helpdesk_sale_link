from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    sale_order_ids = fields.Many2many("sale.order", string="Órdenes de Venta")
    so_count = fields.Integer(
        string="Cantidad de Órdenes", compute="_compute_so_count", store=True
    )

    @api.depends("sale_order_ids")
    def _compute_so_count(self):
        for ticket in self:
            ticket.so_count = len(ticket.sale_order_ids)

    def action_view_sale_orders(self):
        """Muestra las órdenes de venta relacionadas con el ticket."""
        action = self.env["ir.actions.actions"]._for_xml_id("sale.action_orders")
        action["domain"] = [("ticket_ids", "in", self.ids)]
        action["context"] = {
            "default_ticket_ids": [(4, self.id)],
            "default_partner_id": self.partner_id.id,
        }
        return action
