# Copyright (c) 2022, ERP Cloud Systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PMSLeaseContractInvoiceTool(Document):
	@frappe.whitelist()
	def on_submit(self):
		pms_repayment_schedule = frappe.db.sql(""" select `tabPMS Repayment Schedule`.payment_date as payment_date,
															`tabPMS Repayment Schedule`.parent as parent,
															`tabPMS Repayment Schedule`.name as name,
															`tabPMS Repayment Schedule`.base_net_total as base_net_total
															

																from `tabPMS Repayment Schedule`  
																where `tabPMS Repayment Schedule`.payment_date >= '{from_date}'
																and `tabPMS Repayment Schedule`.payment_date <='{to_date}'
																and `tabPMS Repayment Schedule`.is_invoiced = 0
																
															""".format(from_date=self.from_date, to_date = self.to_date), as_dict=1)
		for pms in pms_repayment_schedule:
			pms_lease =pms.parent
			pms_row_name =pms.name
			payment_date =pms.payment_date
			base_net_total =pms.base_net_total
			pms_lease_contract = frappe.db.sql(""" select `tabPMS Lease Contract`.name as name,
														  `tabPMS Lease Contract`.lease_item as lease_item,	
														  `tabPMS Lease Contract`.default_tax_template as default_tax_template,	
														  `tabPMS Lease Contract`.cost_center as cost_center,	
														  `tabPMS Lease Contract`.income_account as income_account,	
														  `tabPMS Lease Contract`.party as party
															

																from `tabPMS Lease Contract` 
																where `tabPMS Lease Contract`.name = '{name}'
																and `tabPMS Lease Contract`.docstatus =1
																
															""".format(name=pms.parent), as_dict=1)
			for lease in pms_lease_contract :
				n_lease_item = lease.lease_item
				n_name = lease.name
				n_default_tax_template = lease.default_tax_template
				n_cost_center = lease.cost_center
				n_income_account = lease.income_account
				n_party = lease.party

	
				new_doc = frappe.get_doc(dict(
					doctype = "Sales Invoice",
					customer = lease.party,
					payment_date = pms.payment_date,
					posting_date = pms.payment_date,
					due_date = pms.payment_date,
					pms_lease_contract = lease.name,
					row_name = pms.name,
					contract_repayment_schedule = 1,
					currency = "EGP",
					reference_doctype = "PMS Lease Contract",
					reference_doctype_tool = self.name,
			
						))
				items = new_doc.append("items", {})
				items.item_code = lease.lease_item
				items.rate = pms.base_net_total
				items.item_tax_template = lease.default_tax_template
				items.cost_center = lease.cost_center
				items.income_account = lease.income_account
				items.qty = 1
				items.conversion_factor = 1
				items.uom = "Nos"
				items.description = "القيمة الايجارية عن عقد رقم  "+"("+ lease.name+") "
				new_doc.insert(ignore_permissions=True)
				frappe.msgprint ( "Sales Invoices Created For Period From " +self.from_date + " To " +self.to_date ) 