# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class AccountReport(models.AbstractModel):
    _inherit = 'account.report'

    filter_country = None


    @api.model
    def _get_options(self, previous_options=None):
        options = super(AccountReport,self)._get_options(previous_options)
        if self.env.context.get('model') == 'account.general.ledger':
            options['country'] = previous_options.get('country')
        return options



class AccountGeneralLedgerReport(models.AbstractModel):
    _inherit = "account.general.ledger"

    country_ids = fields.Many2many('res.country', 'res_country_rel', 'country_id', 'gerenal_ids')

    @api.model
    def _get_options_domain(self, options):
        domain = super(AccountGeneralLedgerReport, self)._get_options_domain(options)
        if options.get('country'):
            domain += [
                ('partner_id.country_id', 'in', options.get('country')),
            ]
        return domain
