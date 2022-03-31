// Copyright (c) 2016, ERP Cloud Systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Detailed Lease Contract Payments Report"] = {
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
			"fieldname":"is_paid",
			"label": __("Is Paid"),
			"fieldtype": "Check",
		},
	],
};