# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors and contributors
# For license information, please see license.txt


from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from erpnext.stock.utils import update_bin
from erpnext.controllers.selling_controller import SellingController
from frappe.utils import flt, cint

from frappe import msgprint, _
import frappe.defaults
from frappe.model.mapper import get_mapped_doc

class ToolsAllocation(SellingController):
	fname = 'tools_information'

	def on_submit(self):
		frappe.errprint("in the submit")

		# self.validate_packed_qty()

		# Check for Approving Authority
		# frappe.get_doc('Authorization Control').validate_approving_authority(self.doctype, self.company, self.grand_total, self)

		# update delivered qty in sales order
		# self.update_prevdoc_status()

		# create stock ledger entry
		self.update_stock_ledger()

		# self.credit_limit()

		# self.make_gl_entries()

		# set DN status
		# frappe.db.set(self, 'status', 'Submitted')			
# 

	def update_stock_ledger(self):
		frappe.errprint(self.get_item_list())
		sl_entries = []
		for d in self.get_item_list():
			frappe.errprint(self.get_item_list())
			if frappe.db.get_value("Item", d.item_code, "is_stock_item") == "Yes" \
					and d.warehouse:
				# self.update_reserved_qty(d)

				sl_entries.append(self.get_sl_entries(d, {
					"actual_qty": -1*flt(d['qty']),
				}))

		self.make_sl_entries(sl_entries)
		frappe.errprint("updated")

		# frappe.throw(_("""Approval Status must be 'Approved' or 'Rejected'"""))




