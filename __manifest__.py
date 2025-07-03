{
    "name": "Helpdesk Sale Link",
    "summary": "Vincula tickets de soporte con órdenes de venta en Odoo 16 EE",
    "author": "Be OnlyOne",
    "maintainers": ["onlyone-odoo"],
    "website": "https://onlyone.odoo.com/",
    "license": "AGPL-3",
    "category": "Helpdesk",
    "version": "16.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "depends": ["helpdesk", "sale_management"],
    "data": [
        "views/helpdesk_ticket_views.xml",
        "views/sale_order_views.xml",
    ],
}