# Copyright (c) 2023, mahmoud haroun and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

from frappe.utils import time_diff_in_hours

class EmployeeExcuseApplication(Document):
	def validate(self):
		self.calc_hours()

	def calc_hours(self):
		print("*"*100)
		diff = time_diff_in_hours(self.to_time, self.from_time)
		

		excuse_hours_alowed = frappe.db.get_list('Department',
			filters={
				'department_name': self.department
			},
			fields=['excuse_hours_alowed'],
				)
		print(excuse_hours_alowed[0].excuse_hours_alowed)

		excuse_hours = frappe.db.get_list('Employee Excuse Application',
			filters={
				'employee': self.employee
			},
			fields=['hours'],
				)
		sum_excuse_hours = 0
		for i in excuse_hours:
			sum_excuse_hours += i.hours
		
		if (sum_excuse_hours + diff < excuse_hours_alowed[0].excuse_hours_alowed):
			self.hours = diff
		else:
			frappe.throw("You don't have enough time to excuse.")

