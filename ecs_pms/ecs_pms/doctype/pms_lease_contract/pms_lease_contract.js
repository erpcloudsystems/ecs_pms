// Copyright (c) 2022, ERP Cloud Systems and contributors
// For license information, please see license.txt



frappe.ui.form.on("PMS Lease Contract", "no_of_years", function(frm){
    var x = (cur_frm.doc.no_of_years * 12) + cur_frm.doc.no_of_months;
    cur_frm.set_value("total_no_of_months",x);
});

frappe.ui.form.on("PMS Lease Contract", "no_of_months", function(frm){
    var x = (cur_frm.doc.no_of_years * 12) + cur_frm.doc.no_of_months;
    cur_frm.set_value("total_no_of_months",x);
});

frappe.ui.form.on("PMS Lease Contract", "validate", function(frm){
    if(cur_frm.doc.total_no_of_months <= 0){
        frappe.throw("Please Enter Contract Period");
    }
    
    if(cur_frm.doc.total_no_of_months > 240){
        frappe.throw("Maximum Contract Length Is 20 Years");
    }
});

frappe.ui.form.on("PMS Lease Contract", "internal_meter_price", function(frm){
    var x = (cur_frm.doc.internal_meter_price * cur_frm.doc.internal_space) + (cur_frm.doc.external_meter_price * cur_frm.doc.external_space);
    cur_frm.set_value("rent_value_",x);
});
 
frappe.ui.form.on("PMS Lease Contract", "external_meter_price", function(frm){
    var x = (cur_frm.doc.internal_meter_price * cur_frm.doc.internal_space) + (cur_frm.doc.external_meter_price * cur_frm.doc.external_space);
    cur_frm.set_value("rent_value_",x);
}); 

frappe.ui.form.on("PMS Lease Contract", "validate", function(frm){
    if(cur_frm.doc.rent_value_ <= 0){
        frappe.throw("Please Enter Internal and External Meter Price To Set Rent Value");
    }
    
    if(cur_frm.doc.total_no_of_months > 240){
        frappe.throw("Maximum Contract Length Is 20 Years");
    }
});

frappe.ui.form.on("PMS Lease Contract", {
	setup: function(frm) {
        frm.set_query("unit", function() {
            return {
                filters: [
                    ["Unit","status", "=", "Vacant"]
                ]
            }
        });
    }
});

frappe.ui.form.on('PMS Lease Contract', 'marketing_service',  function(frm) {
    cur_frm.set_value('marketing_based_on', '');
    cur_frm.set_value('marketing_percent', 0);
    cur_frm.set_value('marketing_amount', 0);
    cur_frm.set_value('base_marketing_amount', 0);
    cur_frm.set_value('marketing_increase_percent', 0);
    cur_frm.set_value('marketing_increase_type', '');
});

frappe.ui.form.on('PMS Lease Contract', 'maintenance_service',  function(frm) {
    cur_frm.set_value('maintenance_based_on', '');
    cur_frm.set_value('maintenance_percent', 0);
    cur_frm.set_value('maintenance_amount', 0);
    cur_frm.set_value('base_maintenance_amount', 0);
    cur_frm.set_value('maintenance_increase_percent', 0);
    cur_frm.set_value('maintenance_increase_type', '');
});

frappe.ui.form.on('PMS Lease Contract', 'electricity',  function(frm) {
    cur_frm.set_value('electricity_based_on', '');
    cur_frm.set_value('electricity_percent', 0);
    cur_frm.set_value('electricity_amount', 0);
    cur_frm.set_value('base_electricity_amount', 0);
});

frappe.ui.form.on('PMS Lease Contract', 'with_insurance',  function(frm) {
    cur_frm.set_value('insurance_value', 0);
    cur_frm.set_value('base_insurance_value', 0);
});

frappe.ui.form.on('PMS Lease Contract', 'with_advanced_payment',  function(frm) {
    cur_frm.set_value('advanced_amount', 0);
    cur_frm.set_value('base_advanced_amount', 0);
});

frappe.ui.form.on("PMS Repayment Schedule", "create_invoice", function(frm,cdt,cdn) {
    {
                    frappe.db.insert(populate_je_obj(frm))
                        .then(function (doc) {
                            console.log(`${doc.doctype} ${doc.name} created on ${doc.creation}`);
                            frappe.set_route('Form', doc.doctype, doc.name);
    
                            }
                    );
    }
        function populate_je_obj(frm, data) {
        var d = locals[cdt][cdn];
        let si = {};
        let items = [
                    {
                        "doctype": "Sales Invoice Item",
                        "item_code": frm.doc.lease_item,
                        "qty": 1,
                        "rate": d.base_net_total,
                        "uom": "Nos",
                        "description": "القيمة الايجارية عن عقد رقم  "+"("+ frm.doc.name+") "+ "لشهر"+"( " +d.payment_date+")",
                        "conversion_factor": 1,
                        "item_tax_template": frm.doc.default_tax_template,
                        "cost_center": frm.doc.cost_center ,
                        "income_account": frm.doc.income_account ,
                    },
                ];
    
        si["doctype"] = "Sales Invoice";
        si["customer"] = frm.doc.party;
        si["payment_date"] = d.payment_date;
        si["posting_date"] = d.payment_date;
        si["row_name"] = d.name;
        si["posting_date"] = d.payment_date;
        si["due_date"] = d.payment_date;
        si["pms_lease_contract"] = cur_frm.doc.name;
        si["cost_center"] = cur_frm.doc.cost_center;
        si["items"] = items;
        si["currency"] = "EGP";
        si["reference_doctype"] = "PMS Lease Contract";
        si["contract_repayment_schedule"] = 1;
        
        return si;
    
    }
    
    });
    
frappe.ui.form.on("PMS Repayment Schedule", "create_payment", function(frm,cdt,cdn) {
    {
                    frappe.db.insert(populate_je_obj(frm))
                        .then(function (doc) {
                            console.log(`${doc.doctype} ${doc.name} created on ${doc.creation}`);
                            frappe.set_route('Form', doc.doctype, doc.name);
    
                            }
                    );
    }
        function populate_je_obj(frm, data) {
        var d = locals[cdt][cdn];
        let py = {};
        let references = [
                        {
                            "doctype": "Payment Entry Reference",
                            "reference_doctype": "Sales Invoice",
                            "reference_name": d.sales_invoice,
                            "allocated_amount": d.outstanding_amount,
                            
                        },
                    ];
      
    
        py["doctype"] = "Payment Entry";
        py["mode_of_payment"] = frm.doc.default_mode_of_payment;
        py["reference_doctype"] = "PMS Lease Contract";
        py["reference_link"] = frm.doc.name;
        py["posting_date"] = d.payment_date;
        py["payment_type"] = "Receive";
        py["party_type"] = "Customer";
        py["party"] = frm.doc.party;
        py["paid_amount"] = d.outstanding_amount;
        py["received_amount"] = d.outstanding_amount;
        py["source_exchange_rate"] = 1;
        py["target_exchange_rate"] = 1;
        py["cost_center"] = cur_frm.doc.cost_center;
        py["paid_to"] = frm.doc.mode_of_payment_account;
        py["contract_repayment_schedule"] = 1;
        py["references"] = references;
        py["payment_date"] = d.payment_date;
        py["row_name"] = d.name;

        
        return py;
    
    }
    
    });
    
    frappe.ui.form.on("PMS Repayment Schedule", "create_electricity_journal", function(frm,cdt,cdn) {
        {
                        frappe.db.insert(populate_je_obj(frm))
                            .then(function (doc) {
                                console.log(`${doc.doctype} ${doc.name} created on ${doc.creation}`);
                                frappe.set_route('Form', doc.doctype, doc.name);
        
                                }
                        );
        }
            function populate_je_obj(frm, data) {
            var d = locals[cdt][cdn];
            let je = {};
            let accounts = [
                        {
                            "doctype": "Journal Entry Account",
                            "account": frm.doc.mode_of_payment_account,
                            "debit": d.base_electricity,
                            "party_type": "Customer",
               		        "party": frm.doc.party,
                            "credit": 0,
                            "debit_in_account_currency": d.base_electricity,
                            "user_remark": cur_frm.docname
                        },
                        {
                            "doctype": "Journal Entry Account",
                            "account": frm.doc.electricity_expense_account,
                            "debit": 0,
                            "credit": d.base_electricity,
                            "credit_in_account_currency": d.base_electricity,
                            "cost_center": frm.doc.cost_center,
                            "user_remark": cur_frm.docname
                        },
        
                    ];
        
            je["doctype"] = "Journal Entry";
            je["voucher_type"] = "Journal Entry";
            je["posting_date"] = d.payment_date;
            je["reference_doctype"] = "PMS Lease Contract";
            je["row_name"] = d.name;
            je["reference_link"] = cur_frm.doc.name;
            je["cheque_no"] = cur_frm.doc.name;
            je["bill_no"] = d.name;
            je["cost_center"] = cur_frm.doc.cost_center;
            je["cheque_date"] = d.payment_date;
            je["posting_date"] = d.payment_date;
        
            je["accounts"] = accounts;
            return je;
        
        }
      
        });
