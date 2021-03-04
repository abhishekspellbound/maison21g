
from odoo import fields, models


class StockQuantityHistory(models.TransientModel):
    _inherit = "stock.quantity.history"

    location_id = fields.Many2many(
        "stock.location", 'stock_quantity_location_rel', 'stock_quantity_id', 'location',
        domain=[("usage", "in", ["internal", "transit"])]
    )
    include_child_locations = fields.Boolean("Include child locations", default=True)

    def open_at_date(self):
        action = super(StockQuantityHistory, self).open_at_date()
        ctx = action["context"]
        if self.location_id:
            ctx["location"] = self.location_id.ids
            ctx["compute_child"] = self.include_child_locations
            if ctx.get("company_owned", False):
                ctx.pop("company_owned")
            action["name"] = "{} ({})".format(
                action["name"], ",".join([item.complete_name for item in self.location_id])
            )
            action["context"] = ctx
        return action
