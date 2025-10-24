# Copyright (c) 2025, d and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from abc import ABC, abstractmethod

class EmployeeTable(Document):
	def validate(self):
		pass		
