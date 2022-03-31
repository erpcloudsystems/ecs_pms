// Copyright (c) 2016, ERP Cloud Systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Units Report"] = {
	"filters": [
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
		{
			"fieldname":"state",
			"label": __("State"),
			"fieldtype": "Select",
			"options":  ["", "Furnished", "Core & Shell"],
		},
        {
			"fieldname":"status",
			"label": __("Status"),
			"fieldtype": "Select",
			"options":  ["", "Vacant", "Occupied"],
		},
	]
};
