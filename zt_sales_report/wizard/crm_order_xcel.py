from odoo import models, fields, api


class CRMOrderTeamtWizard(models.TransientModel):
    """Create new wizard crm.order.xlsx"""
    _name = 'crm.order.xlsx'
    _description = 'Wizard to generate CRM Team report'

    date_start = fields.Datetime(string="Start Date", required=True)
    date_end = fields.Datetime(string="End Date", required=True)
    team_sales_id = fields.Many2one('crm.team','Sales Team Category')

    def get_report(self):
        data = {'date_start': self.date_start, 'date_end': self.date_end,'team_sales_id':int(self.team_sales_id)}
        return self.env.ref('zt_sales_report.crm_order_xlsx').report_action(self, data=data)






