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
			"label": _("Unit"),
			"fieldname": "unit",
			"fieldtype": "Link",
			"options": "Unit",
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
			"label": _("State"),
			"fieldname": "state",
			"fieldtype": "Data",
			"width": 110
		},
		{
			"label": _("Status"),
			"fieldname": "status",
			"fieldtype": "Data",
			"width": 140
		},
		{
			"label": _("Notes"),
			"fieldname": "notes",
			"fieldtype": "Data",
			"width": 250
		}
	]

def get_data(filters, columns):
	item_price_qty_data = []
	item_price_qty_data = get_item_price_qty_data(filters)
	return item_price_qty_data

def get_item_price_qty_data(filters):
	conditions = ""
	if filters.get("unit"):
		conditions += " and a.name1=%(unit)s"
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
	if filters.get("state"):
		conditions += " and a.state=%(state)s"
	if filters.get("status"):
		conditions += " and a.status=%(status)s"
	item_results = frappe.db.sql("""
				select
					a.name1 as unit,
					a.type as type,
					a.floor as floor,
					a.zone as zone,
					a.area as area,
					a.activity as activity,
					a.allocation as allocation,
					a.internal_space as internal_space,
					a.external_space as external_space,
					(a.internal_space + a.external_space) as total_space,
					a.state as state,
					a.status as status,
					a.notes as notes				
				from `tabUnit` a 
				where
					a.status in ("Vacant", "Occupied")
					{conditions}
				""".format(conditions=conditions), filters, as_dict=1)

	result = []
	if item_results:
		for item_dict in item_results:
			data = {
				'unit': item_dict.unit,
				'type': item_dict.type,
				'floor': item_dict.floor,
				'zone': item_dict.zone,
				'area': item_dict.area,
				'allocation': item_dict.allocation,
				'internal_space': item_dict.internal_space,
				'external_space': item_dict.external_space,
				'total_space': item_dict.total_space,
				'activity': item_dict.activity,
				'state': item_dict.state,
				'status': item_dict.status,
				'notes': item_dict.notes,
			}
			result.append(data)

	return result

