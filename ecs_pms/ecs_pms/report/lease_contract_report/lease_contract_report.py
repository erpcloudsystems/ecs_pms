# Copyright (c) 2013, erpcloud.systems and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns, data = [], []
	columns=get_columns()
	data=get_data(filters,columns)
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
			"label": _("Party"),
			"fieldname": "party_name",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("Posting Date"),
			"fieldname": "posting_date",
			"fieldtype": "Date",
			"width": 105
		},
		{
			"label": _("Contract Period In Months"),
			"fieldname": "no_of_months",
			"fieldtype": "Data",
			"width": 220
		},
		{
			"label": _("Start Date"),
			"fieldname": "start_date",
			"fieldtype": "Date",
			"width": 100
		},
		{
			"label": _("End Date"),
			"fieldname": "end_date",
			"fieldtype": "Date",
			"width": 100
		},
		{
			"label": _("Unit"),
			"fieldname": "unit",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"label": _("Unit Type"),
			"fieldname": "type",
			"fieldtype": "Data",
			"width": 110
		},
		{
			"label": _("Floor"),
			"fieldname": "floor",
			"fieldtype": "Data",
			"width": 110
		},
		{
			"label": _("Zone"),
			"fieldname": "zone",
			"fieldtype": "Data",
			"width": 110
		},
		{
			"label": _("Area"),
			"fieldname": "area",
			"fieldtype": "Data",
			"width": 140
		},
		{
			"label": _("Allocation"),
			"fieldname": "allocation",
			"fieldtype": "Data",
			"width": 90
		},
		{
			"label": _("Activity"),
			"fieldname": "activity",
			"fieldtype": "Data",
			"width": 140
		},
		{
			"label": _("Internal Space"),
			"fieldname": "internal_space",
			"fieldtype": "Float",
			"width": 130
		},
		{
			"label": _("External Space"),
			"fieldname": "external_space",
			"fieldtype": "Float",
			"width": 130
		},
		{
			"label": _("Total Space"),
			"fieldname": "total_space",
			"fieldtype": "Float",
			"width": 110
		},
		{
			"label": _("Meter Price"),
			"fieldname": "meter_price",
			"fieldtype": "Currency",
			"width": 160
		},
		{
			"label": _("State"),
			"fieldname": "state",
			"fieldtype": "Data",
			"width": 110
		},
		{
			"label": _("Rent Amount"),
			"fieldname": "rent_value_",
			"fieldtype": "Currency",
			"width": 140
		},
		{
			"label": _("Annual Increase %"),
			"fieldname": "annual_increase",
			"fieldtype": "Percent",
			"width": 160
		},
		{
			"label": _("Annual Increase Type"),
			"fieldname": "annual_increase_type",
			"fieldtype": "Data",
			"width": 160
		},
		{
			"label": _("Insurance Amount"),
			"fieldname": "insurance_value",
			"fieldtype": "Currency",
			"width": 160
		},
		{
			"label": _("Total Payable Amount"),
			"fieldname": "total_payable_amount",
			"fieldtype": "Currency",
			"width": 160
		},
		{
			"label": _("Total Amount Paid"),
			"fieldname": "total_amount_paid",
			"fieldtype": "Currency",
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
	if filters.get("unit"):
		conditions += " and a.unit=%(unit)s"
	if filters.get("type"):
		conditions += " and a.type=%(type)s"
	if filters.get("floor"):
		conditions += " and a.floor=%(floor)s"
	if filters.get("zone"):
		conditions += " and a.zone=%(zone)s"
	if filters.get("area"):
		conditions += " and a.area=%(area)s"
	if filters.get("activity"):
		conditions += " and a.activity=%(activity)s"
	if filters.get("allocation"):
		conditions += " and a.allocation=%(allocation)s"
	if filters.get("from_date"):
		conditions += " and a.posting_date>=%(from_date)s"
	if filters.get("to_date"):
		conditions += " and a.posting_date<=%(to_date)s"
	item_results = frappe.db.sql("""
				select
					a.name as name,
					a.party_name as party_name,
					a.posting_date as posting_date,
					a.unit as unit,
					a.type as type,
					a.floor as floor,
					a.zone as zone,
					a.area as area,
					a.activity as activity,
					a.allocation as allocation,
					a.internal_space as internal_space,
					a.external_space as external_space,
					(a.internal_space + a.external_space) as total_space,
					a.meter_price as meter_price,
					a.state as state,
					a.no_of_months as no_of_months,
					a.rent_value_ as rent_value_,
					a.annual_increase as annual_increase,
					a.annual_increase_type as annual_increase_type,
					a.start_date as start_date,
					a.end_date as end_date,
					a.total_payable_amount as total_payable_amount,
					a.total_amount_paid as total_amount_paid,	
					a.insurance_value as insurance_value				
				from `tabPMS Lease Contract` a 
				where
					a.docstatus = 1
					{conditions}
				""".format(conditions=conditions), filters, as_dict=1)

	result = []
	if item_results:
		for item_dict in item_results:
			data = {
				'name': item_dict.name,
				'party_name': item_dict.party_name,
				'unit': item_dict.unit,
				'type': item_dict.type,
				'floor': item_dict.floor,
				'zone': item_dict.zone,
				'area': item_dict.area,
				'allocation': item_dict.allocation,
				'internal_space': item_dict.internal_space,
				'external_space': item_dict.external_space,
				'total_space': item_dict.total_space,
				'meter_price': item_dict.meter_price,
				'activity': item_dict.activity,
				'state': item_dict.state,
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
			}
			result.append(data)

	return result

