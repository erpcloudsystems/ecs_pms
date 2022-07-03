# Copyright (c) 2013, erpcloud.systems and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


def execute(filters=None):
	columns, data = [], []
	columns = get_columns(filters)
	data = get_data(filters, columns)
	return columns, data

def get_columns(filters):
	if filters.get('group_by') == "Unit Type":
		return [
			{
				"label": _("Unit Type"),
				"fieldname": "type",
				"fieldtype": "Data",
				"width": 160
			},
			
			{
				"label": _("Avg Meter Price (EGP)"),
				"fieldname": "avg_base_meter_price",
				"fieldtype": "Currency",
				"width": 180
			}
		]

	if filters.get('group_by') == "Floor":
		return [
			{
				"label": _("Floor"),
				"fieldname": "floor",
				"fieldtype": "Data",
				"width": 160
			},
			
			{
				"label": _("Avg Meter Price (EGP)"),
				"fieldname": "avg_base_meter_price",
				"fieldtype": "Currency",
				"width": 180
			}
		]

	if filters.get('group_by') == "Area":
		return [
			{
				"label": _("Area"),
				"fieldname": "area",
				"fieldtype": "Data",
				"width": 160
			},
			
			{
				"label": _("Avg Meter Price (EGP)"),
				"fieldname": "avg_base_meter_price",
				"fieldtype": "Currency",
				"width": 180
			}
		]

	if filters.get('group_by') == "Phase":
		return [
			{
				"label": _("Phase"),
				"fieldname": "phase",
				"fieldtype": "Data",
				"width": 160
			},
			
			{
				"label": _("Avg Meter Price (EGP)"),
				"fieldname": "avg_base_meter_price",
				"fieldtype": "Currency",
				"width": 180
			}
		]

	if filters.get('group_by') == "Zone":
		return [
			{
				"label": _("Zone"),
				"fieldname": "zone",
				"fieldtype": "Data",
				"width": 160
			},
			
			{
				"label": _("Avg Meter Price (EGP)"),
				"fieldname": "avg_base_meter_price",
				"fieldtype": "Currency",
				"width": 180
			}
		]

	if filters.get('group_by') == "Activity":
		return [
			{
				"label": _("Activity"),
				"fieldname": "activity",
				"fieldtype": "Data",
				"width": 160
			},
			
			{
				"label": _("Avg Meter Price (EGP)"),
				"fieldname": "avg_meter_price",
				"fieldtype": "Currency",
				"width": 180
			}
		]

	else:
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
				"label": _("Phase"),
				"fieldname": "phase",
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
				"label": _("Contract Currency"),
				"fieldname": "contract_currency",
				"fieldtype": "Link",
				"options": "Currency",
				"width": 160
			},
			{
				"label": _("Meter Price"),
				"fieldname": "meter_price",
				"fieldtype": "Currency",
				"width": 160
			},
			{
				"label": _("Meter Price (EGP)"),
				"fieldname": "base_meter_price",
				"fieldtype": "Currency",
				"width": 180
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
				"label": _("Rental Amount (EGP)"),
				"fieldname": "base_rent_value",
				"fieldtype": "Currency",
				"width": 160
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
				"label": _("Total Payable Amount (EGP)"),
				"fieldname": "base_total_payable_amount",
				"fieldtype": "Currency",
				"width": 200
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
	if filters.get('group_by') == "Unit Type":
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
		if filters.get("phase"):
			conditions += " and a.phase=%(phase)s"
		if filters.get("activity"):
			conditions += " and a.activity=%(activity)s"
		if filters.get("allocation"):
			conditions += " and a.allocation=%(allocation)s"
		if filters.get("from_date"):
			conditions += " and a.posting_date>=%(from_date)s"
		if filters.get("to_date"):
			conditions += " and a.posting_date<=%(to_date)s"

		item_results2 = frappe.db.sql("""
	                SELECT distinct
	                    a.type as type
	                FROM
	                    `tabPMS Lease Contract` a 
					WHERE
						a.docstatus = 1
						{conditions}	
	                Group BY a.type
	                """.format(conditions=conditions), filters, as_dict=1)

		result2 = []
		if item_results2:
			for item_dict in item_results2:
				data = {
					'type': item_dict.type

				}
				details = frappe.db.sql("""
	                    SELECT 
	                        avg(a.base_meter_price) as avg_base_meter_price,
							avg(a.meter_price) as avg_meter_price
	                    FROM
	                        `tabPMS Lease Contract` a
	                    WHERE 
	                        a.type = '{unit_type}'
	                        and a.docstatus = 1
	                        {conditions}
	                    """.format(unit_type=item_dict.type, conditions=conditions), filters, as_dict=1)


				for x in details:
					data['avg_base_meter_price'] = x.avg_base_meter_price
					data['avg_meter_price'] = x.avg_meter_price

				result2.append(data)
		return result2

	if filters.get('group_by') == "Floor":
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
		if filters.get("phase"):
			conditions += " and a.phase=%(phase)s"
		if filters.get("activity"):
			conditions += " and a.activity=%(activity)s"
		if filters.get("allocation"):
			conditions += " and a.allocation=%(allocation)s"
		if filters.get("from_date"):
			conditions += " and a.posting_date>=%(from_date)s"
		if filters.get("to_date"):
			conditions += " and a.posting_date<=%(to_date)s"

		item_results2 = frappe.db.sql("""
	                SELECT distinct
	                    a.floor as floor
	                FROM
	                    `tabPMS Lease Contract` a 
					WHERE
						a.docstatus = 1
						{conditions}	
	                Group BY a.floor
	                """.format(conditions=conditions), filters, as_dict=1)

		result2 = []
		if item_results2:
			for item_dict in item_results2:
				data = {
					'floor': item_dict.floor

				}
				details = frappe.db.sql("""
	                    SELECT 
	                        avg(a.base_meter_price) as avg_base_meter_price,
	                        avg(a.meter_price) as avg_meter_price
	                    FROM
	                        `tabPMS Lease Contract` a
	                    WHERE 
	                        a.floor = '{floor}'
	                        and a.docstatus = 1
	                        {conditions}
	                    """.format(floor=item_dict.floor, conditions=conditions), filters, as_dict=1)


				for x in details:
					data['avg_base_meter_price'] = x.avg_base_meter_price
					data['avg_meter_price'] = x.avg_meter_price

				result2.append(data)
		return result2

	if filters.get('group_by') == "Area":
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
		if filters.get("phase"):
			conditions += " and a.phase=%(phase)s"
		if filters.get("activity"):
			conditions += " and a.activity=%(activity)s"
		if filters.get("allocation"):
			conditions += " and a.allocation=%(allocation)s"
		if filters.get("from_date"):
			conditions += " and a.posting_date>=%(from_date)s"
		if filters.get("to_date"):
			conditions += " and a.posting_date<=%(to_date)s"

		item_results2 = frappe.db.sql("""
	                SELECT distinct
	                    a.area as area
	                FROM
	                    `tabPMS Lease Contract` a 
					WHERE
						a.docstatus = 1
						{conditions}	
	                Group BY a.area
	                """.format(conditions=conditions), filters, as_dict=1)

		result2 = []
		if item_results2:
			for item_dict in item_results2:
				data = {
					'area': item_dict.area

				}
				details = frappe.db.sql("""
	                    SELECT 
	                        avg(a.base_meter_price) as avg_base_meter_price,
	                        avg(a.meter_price) as avg_meter_price
	                    FROM
	                        `tabPMS Lease Contract` a
	                    WHERE 
	                        a.area = '{area}'
	                        and a.docstatus = 1
	                        {conditions}
	                    """.format(area=item_dict.area, conditions=conditions), filters, as_dict=1)


				for x in details:
					data['avg_base_meter_price'] = x.avg_base_meter_price
					data['avg_meter_price'] = x.avg_meter_price

				result2.append(data)
		return result2

	if filters.get('group_by') == "Phase":
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
		if filters.get("phase"):
			conditions += " and a.phase=%(phase)s"
		if filters.get("activity"):
			conditions += " and a.activity=%(activity)s"
		if filters.get("allocation"):
			conditions += " and a.allocation=%(allocation)s"
		if filters.get("from_date"):
			conditions += " and a.posting_date>=%(from_date)s"
		if filters.get("to_date"):
			conditions += " and a.posting_date<=%(to_date)s"

		item_results2 = frappe.db.sql("""
	                SELECT distinct
	                    a.phase as phase
	                FROM
	                    `tabPMS Lease Contract` a 
					WHERE
						a.docstatus = 1
						{conditions}	
	                Group BY a.phase
	                """.format(conditions=conditions), filters, as_dict=1)

		result2 = []
		if item_results2:
			for item_dict in item_results2:
				data = {
					'phase': item_dict.phase

				}
				details = frappe.db.sql("""
	                    SELECT 
	                        avg(a.base_meter_price) as avg_base_meter_price,
	                        avg(a.meter_price) as avg_meter_price
	                    FROM
	                        `tabPMS Lease Contract` a
	                    WHERE 
	                        a.phase = '{phase}'
	                        and a.docstatus = 1
	                        {conditions}
	                    """.format(phase=item_dict.phase, conditions=conditions), filters, as_dict=1)


				for x in details:
					data['avg_base_meter_price'] = x.avg_base_meter_price
					data['avg_meter_price'] = x.avg_meter_price

				result2.append(data)
		return result2

	if filters.get('group_by') == "Zone":
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
		if filters.get("phase"):
			conditions += " and a.phase=%(phase)s"
		if filters.get("activity"):
			conditions += " and a.activity=%(activity)s"
		if filters.get("allocation"):
			conditions += " and a.allocation=%(allocation)s"
		if filters.get("from_date"):
			conditions += " and a.posting_date>=%(from_date)s"
		if filters.get("to_date"):
			conditions += " and a.posting_date<=%(to_date)s"

		item_results2 = frappe.db.sql("""
	                SELECT distinct
	                    a.zone as zone 
	                FROM
	                    `tabPMS Lease Contract` a 
					WHERE
						a.docstatus = 1
						{conditions}	
	                Group BY a.zone
	                """.format(conditions=conditions), filters, as_dict=1)

		result2 = []
		if item_results2:
			for item_dict in item_results2:
				data = {
					'zone': item_dict.zone

				}
				details = frappe.db.sql("""
	                    SELECT 
	                        avg(a.base_meter_price) as avg_base_meter_price,
	                        avg(a.meter_price) as avg_meter_price
	                    FROM
	                        `tabPMS Lease Contract` a
	                    WHERE 
	                        a.zone = '{zone}'
	                        and a.docstatus = 1
	                        {conditions}
	                    """.format(zone=item_dict.zone, conditions=conditions), filters, as_dict=1)


				for x in details:
					data['avg_base_meter_price'] = x.avg_base_meter_price
					data['avg_meter_price'] = x.avg_meter_price

				result2.append(data)
		return result2

	if filters.get('group_by') == "Activity":
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
		if filters.get("phase"):
			conditions += " and a.phase=%(phase)s"
		if filters.get("activity"):
			conditions += " and a.activity=%(activity)s"
		if filters.get("allocation"):
			conditions += " and a.allocation=%(allocation)s"
		if filters.get("from_date"):
			conditions += " and a.posting_date>=%(from_date)s"
		if filters.get("to_date"):
			conditions += " and a.posting_date<=%(to_date)s"

		item_results2 = frappe.db.sql("""
	                SELECT distinct
	                    a.activity as activity
	                FROM
	                    `tabPMS Lease Contract` a 
					WHERE
						a.docstatus = 1
						{conditions}	
	                Group BY a.activity
	                """.format(conditions=conditions), filters, as_dict=1)

		result2 = []
		if item_results2:
			for item_dict in item_results2:
				data = {
					'activity': item_dict.activity

				}
				details = frappe.db.sql("""
	                    SELECT 
	                        avg(a.base_meter_price) as avg_base_meter_price,
	                        avg(a.meter_price) as avg_meter_price
	                    FROM
	                        `tabPMS Lease Contract` a
	                    WHERE 
	                        a.activity = '{activity}'
	                        and a.docstatus = 1
	                        {conditions}
	                    """.format(activity=item_dict.activity, conditions=conditions), filters, as_dict=1)


				for x in details:
					data['avg_base_meter_price'] = x.avg_base_meter_price
					data['avg_meter_price'] = x.avg_meter_price

				result2.append(data)
		return result2

	else:
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
		if filters.get("phase"):
			conditions += " and a.phase=%(phase)s"
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
							a.phase as phase,
							a.activity as activity,
							a.allocation as allocation,
							a.internal_space as internal_space,
							a.external_space as external_space,
							(a.internal_space + a.external_space) as total_space,
							a.base_meter_price as base_meter_price,
							a.meter_price as meter_price,
							a.state as state,
							a.no_of_months as no_of_months,
							a.base_rent_value as base_rent_value,
							a.rent_value_ as rent_value_,
							a.annual_increase as annual_increase,
							a.annual_increase_type as annual_increase_type,
							a.start_date as start_date,
							a.end_date as end_date,
							a.base_total_payable_amount as base_total_payable_amount,
							a.total_payable_amount as total_payable_amount,
							a.total_amount_paid as total_amount_paid,	
							a.insurance_value as insurance_value,
							a.currency as contract_currency				
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
					'contract_currency': item_dict.contract_currency,
					'party_name': item_dict.party_name,
					'unit': item_dict.unit,
					'type': item_dict.type,
					'floor': item_dict.floor,
					'zone': item_dict.zone,
					'area': item_dict.area,
					'phase': item_dict.phase,
					'allocation': item_dict.allocation,
					'internal_space': item_dict.internal_space,
					'external_space': item_dict.external_space,
					'total_space': item_dict.total_space,
					'meter_price': item_dict.meter_price,
					'base_meter_price': item_dict.base_meter_price,
					'activity': item_dict.activity,
					'state': item_dict.state,
					'posting_date': item_dict.posting_date,
					'no_of_months': item_dict.no_of_months,
					'base_rent_value': item_dict.base_rent_value,
					'rent_value_': item_dict.rent_value_,
					'annual_increase': item_dict.annual_increase,
					'annual_increase_type': item_dict.annual_increase_type,
					'start_date': item_dict.start_date,
					'end_date': item_dict.end_date,
					'base_total_payable_amount': item_dict.base_total_payable_amount,
					'total_payable_amount': item_dict.total_payable_amount,
					'total_amount_paid': item_dict.total_amount_paid,
					'insurance_value': item_dict.insurance_value,
				}
				result.append(data)

		return result

