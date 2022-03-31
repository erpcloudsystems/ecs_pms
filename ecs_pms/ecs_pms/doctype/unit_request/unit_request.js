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