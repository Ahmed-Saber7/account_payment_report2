from odoo import fields, models, api, _
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import time


class account_paymnet_report(models.AbstractModel):

    _name = 'report.account_payment_report.payment_report_template'



    def _get_start_date(self,form):
        date_from = form['date_from']
        return date_from

    def _get_end_date(self,form):
        date_to = form['date_to']
        return date_to

    def _get_journal(self):
        account_journal = self.env["account.journal"]
        data = []

        object_journal = account_journal.search([])


        for journals in object_journal:
            result = {
                "name": journals.name,

        }
            data.append(result)
        if data:
            return data
        else:
            return {}


    def _get_payments(self, date_from, date_to):#

        account_payment = self.env["account.payment"]

        data = []
        object_payments = account_payment.search([("payment_date", '>=', date_from),('payment_date', '<=', date_to)],order='payment_date')
        total_amount = 0.0
        for toalats in object_payments:

            total_amount = total_amount + toalats.amount

        for payments in object_payments:


            res = {
                "name": payments.name,
                "payment_date": payments.payment_date,
                "partner_name": payments.partner_id.name,
                "journal_id":payments.journal_id.name,
                "amount":payments.amount,
                'amount_total':total_amount,


        }
            data.append(res)
        if data:
            return data
        else:
            return {}


    @api.model
    def _get_report_values(self, docids, data=None):
        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_id'))
        check_report = self.env['ir.actions.report']._get_report_from_name('account_payment_report.account_payment_report_temp')

        return {
            'doc_ids': docids,
            'doc_model': check_report.model,
            'docs': docs,
            "time": time,
            "date_from": self._get_start_date(data['form']),
            "date_to": self._get_end_date(data['form']),
            "get_journal": self._get_journal,
            "get_payments": self._get_payments,

        }

