# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from odoo.tools.translate import _
from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT
import time
from odoo.exceptions import Warning as UserError


class payment_report(models.TransientModel):
    _name = 'payment.report'


    date_from = fields.Date(string="From", required=True, )
    date_to = fields.Date(string="To", required=True, )



    @api.constrains("date_from", "date_to")
    def _payment_date(self):
        strWarning = _(
            "Date start must be greater than date end")
        if self.date_from and self.date_to:
            if self.date_from > self.date_to:
                raise UserError(strWarning)



    @api.multi
    def payment_report(self):
        """Call when button 'Get Report' clicked.
        """
        [data] = self.read()
        # data['form'] = self.read(['date_start', 'date_end','priority','get_tickets',])[0]
        data['form'] = self.read(['date_from', 'date_to', 'get_payments','get_journal' ])[0]
        datas = {
            # 'type': type,
            'model': 'account.payment',
            'form': data

        }

        return self.env.ref('account_payment_report.account_paymnet_report_ref_id').report_action(self, data=datas)

