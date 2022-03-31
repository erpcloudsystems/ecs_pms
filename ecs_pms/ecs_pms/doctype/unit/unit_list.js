// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

// render
frappe.listview_settings['Unit'] = {
	get_indicator: function(doc) {
		const status_colors = {
			"Vacant": "green",
			"Occupied": "red"
		};
		return [__(doc.status), status_colors[doc.status], "status,=,"+doc.status];
	},
};
