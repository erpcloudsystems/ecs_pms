// Copyright (c) 2016, erpcloud.systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Lease Contract Report"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"width": "80"
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"width": "80"
		},
		{
			"fieldname":"contract",
			"label": __("Contract No"),
			"fieldtype": "Link",
			"options":  "PMS Lease Contract",
		},
		{
			"fieldname":"unit",
			"label": __("Unit"),
			"fieldtype": "Link",
			"options":  "Unit",
		},
		{
			"fieldname":"type",
			"label": __("Unit Type"),
			"fieldtype": "Link",
			"options":  "Unit Type",
		},
		{
			"fieldname":"floor",
			"label": __("Floor"),
			"fieldtype": "Link",
			"options":  "Floor",
		},
		{
			"fieldname":"zone",
			"label": __("Zone"),
			"fieldtype": "Link",
			"options":  "Zone",
		},
		{
			"fieldname":"area",
			"label": __("Area"),
			"fieldtype": "Link",
			"options":  "Area",
		},
		{
			"fieldname":"activity",
			"label": __("Activity"),
			"fieldtype": "Link",
			"options":  "PMS Activity",
		},
		{
			"fieldname":"allocation",
			"label": __("Allocation"),
			"fieldtype": "Select",
			"options":  ["", "Prime", "Medium", "Low"],
		},
	],
};