// Copyright (c) 2022, ERP Cloud Systems and contributors
// For license information, please see license.txt

frappe.ui.form.on("Unit Request", {
    refresh: function(frm, cdt, cdn) {
        if(frm.doc.docstatus == 1){
            frm.add_custom_button(__("Quotation"), function() {
                var child = locals[cdt][cdn];
                frappe.route_options = {
                    "quotation_to": "Customer",
                    "party_name": frm.doc.customer,
                    "unit_request": frm.doc.name,
                };
                frappe.new_doc("Quotation");
            }, __("Create"));
        }
    }
});

frappe.ui.form.on("Unit Request", {
	setup: function(frm) {
		frm.set_query("party_type", function() {
			return {
				filters: [
					["DocType","name", "in", ["Customer", "Lead"]]
				]
			};
		});
	}
});


frappe.ui.form.on('Unit Request', 'customer',  function(frm) {

    if (cur_frm.doc.party_type =="Customer"){

    frappe.call({ method: "frappe.client.get_value",
	args: { doctype: "Customer",
	fieldname: "customer_name",
	filters: { 'name': cur_frm.doc.customer},
	}, callback: function(r)
	{cur_frm.set_value("customer_name", r.message.customer_name);
  } });


    frappe.call({ method: "frappe.client.get_value",
	args: { doctype: "Customer",
	fieldname: "customer_group",
	filters: { 'name': cur_frm.doc.customer},
	}, callback: function(r)
	{cur_frm.set_value("customer_group", r.message.customer_group);
  } });
        }

  if (cur_frm.doc.party_type =="Lead"){

    frappe.call({ method: "frappe.client.get_value",
    args: { doctype: "Lead",
    fieldname: "lead_name",
    filters: { 'name': cur_frm.doc.customer},
    }, callback: function(r)
    {cur_frm.set_value("customer_name", r.message.lead_name);
  } });
        }
});

frappe.ui.form.on('Unit Request', 'party_type', function(frm){
    cur_frm.set_value("customer","");
    cur_frm.set_value("customer_name","");
    cur_frm.set_value("customer_group","");
});