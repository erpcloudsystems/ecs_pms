# Copyright (c) 2013, erpcloud.systems and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


def execute(filters=None):
    columns, data = [], []
    columns = get_columns()
    data = get_data(filters, columns)
    return columns, data


def get_columns():
    return [
        {
            "label": _("Contract No"),
            "fieldname": "name",
            "fieldtype": "Link",
            "options": "PMS Lease Contract",
            "width": 155
        },
        {
            "label": _("Customer"),
            "fieldname": "party_name",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("No Of Payments"),
            "fieldname": "no_of_months",
            "fieldtype": "Int",
            "width": 130
        },
        {
            "label": _("Payment #"),
            "fieldname": "idx",
            "fieldtype": "data",
            "width": 100
        },
        {
            "label": _("Payment Date"),
            "fieldname": "payment_date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "label": _("Monthly Payment"),
            "fieldname": "monthly_payment",
            "fieldtype": "Currency",
            "width": 170
        },
        {
            "label": _("Is Paid"),
            "fieldname": "is_paid",
            "fieldtype": "Check",
            "width": 80
        },
        {
            "label": _("Journal Entry"),
            "fieldname": "journal_entry",
            "fieldtype": "Link",
            "options": "Journal Entry",
            "width": 160
        }
    ]


def get_data(filters, columns):
    item_price_qty_data = []
    item_price_qty_data = get_item_price_qty_data(filters)
    return item_price_qty_data


def get_item_price_qty_data(filters):
    conditions = ""
    if filters.get("contract"):
        conditions += " and a.name=%(contract)s"
    if filters.get("is_paid"):
        conditions += " and b.is_paid=%(is_paid)s"
    if filters.get("from_date"):
        conditions += " and b.payment_date>=%(from_date)s"
    if filters.get("to_date"):
        conditions += " and b.payment_date<=%(to_date)s"
    item_results = frappe.db.sql("""
				select
						a.name as name,
						a.party_name as party_name,
						a.posting_date as posting_date,
						a.unit as unit,
						a.no_of_months as no_of_months,
						a.rent_value_ as rent_value_,
						a.annual_increase as annual_increase,
						a.annual_increase_type as annual_increase_type,
						a.start_date as start_date,
						a.end_date as end_date,
						a.total_payable_amount as total_payable_amount,
						a.total_amount_paid as total_amount_paid,	
						a.insurance_value as insurance_value,
						b.payment_date as payment_date,
						CONCAT_WS('Payment #',b.idx) as idx,
						b.monthly_payment as monthly_payment,
						b.is_paid as is_paid,
						b.journal_entry as journal_entry				
				from `tabPMS Lease Contract` a join `tabPMS Repayment Schedule` b on b.parent = a.name

				where
					 a.docstatus = 1
					{conditions}
				order by b.payment_date asc
				""".format(conditions=conditions), filters, as_dict=1)

    # price_list_names = list(set([item.price_list_name for item in item_results]))

    # buying_price_map = get_price_map(price_list_names, buying=1)
    # selling_price_map = get_price_map(price_list_names, selling=1)

    result = []
    if item_results:
        for item_dict in item_results:
            data = {
                'name': item_dict.name,
                'party_name': item_dict.party_name,
                'unit_type': item_dict.unit_type,
                'posting_date': item_dict.posting_date,
                'no_of_months': item_dict.no_of_months,
                'rent_value_': item_dict.rent_value_,
                'annual_increase': item_dict.annual_increase,
                'annual_increase_type': item_dict.annual_increase_type,
                'start_date': item_dict.start_date,
                'end_date': item_dict.end_date,
                'total_payable_amount': item_dict.total_payable_amount,
                'total_amount_paid': item_dict.total_amount_paid,
                'insurance_value': item_dict.insurance_value,
                'idx': item_dict.idx,
                'payment_date': item_dict.payment_date,
                'monthly_payment': item_dict.monthly_payment,
                'is_paid': item_dict.is_paid,
                'journal_entry': item_dict.journal_entry,
            }
            result.append(data)

    return result


def get_price_map(price_list_names, buying=0, selling=0):
    price_map = {}

    if not price_list_names:
        return price_map

    rate_key = "Buying Rate" if buying else "Selling Rate"
    price_list_key = "Buying Price List" if buying else "Selling Price List"

    filters = {"name": ("in", price_list_names)}
    if buying:
        filters["buying"] = 1
    else:
        filters["selling"] = 1

    pricing_details = frappe.get_all("Item Price",
                                     fields=["name", "price_list", "price_list_rate"], filters=filters)

    for d in pricing_details:
        name = d["name"]
        price_map[name] = {
            price_list_key: d["price_list"],
            rate_key: d["price_list_rate"]
        }

    return price_map
