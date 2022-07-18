# Copyright (c) 2021, ERP Cloud Systems and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, json
from frappe.model.document import Document
from frappe import _
from frappe.desk.search import sanitize_searchfield
from frappe.utils import (flt, getdate, get_url, now,
                          nowtime, get_time, today, get_datetime, add_days)
from frappe.utils import add_to_date, now, nowdate
import frappe, math, json
import erpnext
from frappe import _
from six import string_types
from frappe.utils import flt, rounded, add_months, nowdate, getdate, now_datetime
from erpnext.setup.utils import get_exchange_rate
from datetime import datetime
from datetime import timedelta
from datetime import date


class PMSLeaseContract(Document):
    @frappe.whitelist()
    def validate(self):
        self.calculate_net_totals()
        self.contract_defaults()
        self.calculate_totals()
        self.calculate_repayment_schedule()

    @frappe.whitelist()
    def on_update_after_submit(self):  
        self.calculate_net_totals()    
        self.contract_defaults()    
        self.calculate_net_total()

    @frappe.whitelist()
    def calculate_repayment_schedule(self):
        monthly_marketing = 0
        daily_marketing = 0
        monthly_maintenance = 0
        daily_maintenance = 0
        if self.revenue_type == "Fixed Lease" or "Revenue Share + Fixed Rent" or "Revenue Share / Minimum Rent":
            self.contract_repayment_schedule = []
            payment_date = add_months(self.start_date, self.grace_period)
            self.end_date = add_months(self.start_date, self.total_no_of_months)
            
            if self.no_of_days > 0:
                end_date = add_months(self.start_date, self.total_no_of_months)
                self.end_date = add_days(end_date, days=(self.no_of_days - 1))

            monthly_payment = self.rent_value_
            fixed_value = self.rent_value_ * self.annual_increase / 100
            a = self.total_no_of_months  - self.grace_period
            b = 1

            x = self.rent_value_ + fixed_value
            x1 = x + (x * self.annual_increase / 100)
            x2 = x1 + (x1 * self.annual_increase / 100)
            x3 = x2 + (x2 * self.annual_increase / 100)
            x4 = x3 + (x3 * self.annual_increase / 100)
            x5 = x4 + (x4 * self.annual_increase / 100)
            x6 = x5 + (x5 * self.annual_increase / 100)
            x7 = x6 + (x6 * self.annual_increase / 100)
            x8 = x7 + (x7 * self.annual_increase / 100)
            x9 = x8 + (x8 * self.annual_increase / 100)
            x10 = x9 + (x9 * self.annual_increase / 100)
            x11 = x10 + (x10 * self.annual_increase / 100)
            x12 = x11 + (x11 * self.annual_increase / 100)
            x13 = x12 + (x12 * self.annual_increase / 100)
            x14 = x13 + (x13 * self.annual_increase / 100)
            x15 = x14 + (x14 * self.annual_increase / 100)
            x16 = x15 + (x15 * self.annual_increase / 100)
            x17 = x16 + (x16 * self.annual_increase / 100)
            x18 = x17 + (x17 * self.annual_increase / 100)
            x19 = x18 + (x18 * self.annual_increase / 100)
            if self.marketing_service:
                fixed_value1 = self.marketing_amount * (self.marketing_increase_percent / 100)
                monthly_marketing = self.marketing_amount
                m = self.marketing_amount + fixed_value1
                m1 = m + (m * self.marketing_increase_percent / 100)
                m2 = m1 + (m1 * self.marketing_increase_percent / 100)
                m3 = m2 + (m2 * self.marketing_increase_percent / 100)
                m4 = m3 + (m3 * self.marketing_increase_percent / 100)
                m5 = m4 + (m4 * self.marketing_increase_percent / 100)
                m6 = m5 + (m5 * self.marketing_increase_percent / 100)
                m7 = m6 + (m6 * self.marketing_increase_percent / 100)
                m8 = m7 + (m7 * self.marketing_increase_percent / 100)
                m9 = m8 + (m8 * self.marketing_increase_percent / 100)
                m10 = m9 + (m9 * self.marketing_increase_percent / 100)
                m11 = m10 + (m10 * self.marketing_increase_percent / 100)
                m12 = m11 + (m11 * self.marketing_increase_percent / 100)
                m13 = m12 + (m12 * self.marketing_increase_percent / 100)
                m14 = m13 + (m13 * self.marketing_increase_percent / 100)
                m15 = m14 + (m14 * self.marketing_increase_percent / 100)
                m16 = m15 + (m15 * self.marketing_increase_percent / 100)
                m17 = m16 + (m16 * self.marketing_increase_percent / 100)
                m18 = m17 + (m17 * self.marketing_increase_percent / 100)
                m19 = m18 + (m18 * self.marketing_increase_percent / 100)
            if self.maintenance_service:
                fixed_value2 = self.maintenance_amount * self.maintenance_increase_percent / 100
                monthly_maintenance = self.maintenance_amount
                s = self.maintenance_amount + fixed_value2              
                s1 = s + (s * self.maintenance_increase_percent / 100)
                s2 = s1 + (s1 * self.maintenance_increase_percent / 100)
                s3 = s2 + (s2 * self.maintenance_increase_percent / 100)
                s4 = s3 + (s3 * self.maintenance_increase_percent / 100)
                s5 = s4 + (s4 * self.maintenance_increase_percent / 100)
                s6 = s5 + (s5 * self.maintenance_increase_percent / 100)
                s7 = s6 + (s6 * self.maintenance_increase_percent / 100)
                s8 = s7 + (s7 * self.maintenance_increase_percent / 100)
                s9 = s8 + (s8 * self.maintenance_increase_percent / 100)
                s10 = s9 + (s9 * self.maintenance_increase_percent / 100)
                s11 = s10 + (s10 * self.maintenance_increase_percent / 100)
                s12 = s11 + (s11 * self.maintenance_increase_percent / 100)
                s13 = s12 + (s12 * self.maintenance_increase_percent / 100)
                s14 = s13 + (s13 * self.maintenance_increase_percent / 100)
                s15 = s14 + (s14 * self.maintenance_increase_percent / 100)
                s16 = s15 + (s15 * self.maintenance_increase_percent / 100)
                s17 = s16 + (s16 * self.maintenance_increase_percent / 100)
                s18 = s17 + (s17 * self.maintenance_increase_percent / 100)
                s19 = s18 + (s18 * self.maintenance_increase_percent / 100)

            while (a > 0):
                self.append("contract_repayment_schedule", {
                    "payment_date": payment_date,
                    "monthly_payment": monthly_payment,
                    "base_monthly_payment_": monthly_payment * self.conversion_rate,
                    "marketing": monthly_marketing,
                    "base_marketing": monthly_marketing * self.conversion_rate,
                    "maintenance": monthly_maintenance,
                    "base_maintenance": monthly_maintenance * self.conversion_rate,
					"electricity": self.electricity_amount,
					"base_electricity": self.base_electricity_amount
                })
                next_payment_date = add_months(payment_date, 1)
                payment_date = next_payment_date
                rent_value = x
                daily_rent = x / 30
                daily_rent_value = daily_rent
            
                if b >= (12 - self.grace_period ) and b <= (23 - self.grace_period ):
                    rent_value = x
                    daily_rent = x / 30
                    daily_rent_value = daily_rent
                    marketing_value = m
                    daily_marketing = marketing_value / 30
                    maintenance_value = s
                    daily_maintenance = maintenance_value / 30
                    monthly_payment = rent_value
                    monthly_marketing = marketing_value
                    monthly_maintenance = maintenance_value

                if b >= (24 - self.grace_period ) and b <= (35 - self.grace_period ):
                    if self.annual_increase_type == "Fixed Rate":
                        rent_value = self.rent_value_ + (2 * fixed_value)
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.annual_increase_type == "Accumulated Rate":
                        rent_value = x1
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.marketing_increase_type == "Fixed Rate":
                        marketing_value = self.marketing_amount + (2 * fixed_value1)
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.marketing_increase_type == "Accumulated Rate":
                        marketing_value = m1
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.maintenance_increase_type == "Fixed Rate":
                        maintenance_value = self.maintenance_amount + (2 * fixed_value2)
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                    if self.maintenance_increase_type == "Accumulated Rate":
                        maintenance_value = s1
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                if b >= (36 - self.grace_period ) and b <= (47 - self.grace_period ):
                    if self.annual_increase_type == "Fixed Rate":
                        rent_value = self.rent_value_ + (3 * fixed_value)
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.annual_increase_type == "Accumulated Rate":
                        rent_value = x2
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.marketing_increase_type == "Fixed Rate":
                        marketing_value = self.marketing_amount + (3 * fixed_value1)
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.marketing_increase_type == "Accumulated Rate":
                        marketing_value = m2
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.maintenance_increase_type == "Fixed Rate":
                        maintenance_value = self.maintenance_amount + (3 * fixed_value2)
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                    if self.maintenance_increase_type == "Accumulated Rate":
                        maintenance_value = s2
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                if b >= (48 - self.grace_period ) and b <= (59 - self.grace_period ):
                    if self.annual_increase_type == "Fixed Rate":
                        rent_value = self.rent_value_ + (4 * fixed_value)
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.annual_increase_type == "Accumulated Rate":
                        rent_value = x3
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.marketing_increase_type == "Fixed Rate":
                        marketing_value = self.marketing_amount + (4 * fixed_value1)
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.marketing_increase_type == "Accumulated Rate":
                        marketing_value = m3
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.maintenance_increase_type == "Fixed Rate":
                        maintenance_value = self.maintenance_amount + (4 * fixed_value2)
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                    if self.maintenance_increase_type == "Accumulated Rate":
                        maintenance_value = s3
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                if b >= (60 - self.grace_period ) and b <= (71 - self.grace_period ):
                    if self.annual_increase_type == "Fixed Rate":
                        rent_value = self.rent_value_ + (5 * fixed_value)
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.annual_increase_type == "Accumulated Rate":
                        rent_value = x4
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.marketing_increase_type == "Fixed Rate":
                        marketing_value = self.marketing_amount + (5 * fixed_value1)
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.marketing_increase_type == "Accumulated Rate":
                        marketing_value = m4
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.maintenance_increase_type == "Fixed Rate":
                        maintenance_value = self.maintenance_amount + (5 * fixed_value2)
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                    if self.maintenance_increase_type == "Accumulated Rate":
                        maintenance_value = s4
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                if b >= (72 - self.grace_period ) and b <= (83 - self.grace_period ):
                    if self.annual_increase_type == "Fixed Rate":
                        rent_value = self.rent_value_ + (6 * fixed_value)
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.annual_increase_type == "Accumulated Rate":
                        rent_value = x5
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.marketing_increase_type == "Fixed Rate":
                        marketing_value = self.marketing_amount + (6 * fixed_value1)
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.marketing_increase_type == "Accumulated Rate":
                        marketing_value = m5
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.maintenance_increase_type == "Fixed Rate":
                        maintenance_value = self.maintenance_amount + (6 * fixed_value2)
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30
                        

                    if self.maintenance_increase_type == "Accumulated Rate":
                        maintenance_value = s5
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                if b >= (84 - self.grace_period ) and b <= (95 - self.grace_period ):
                    if self.annual_increase_type == "Fixed Rate":
                        rent_value = self.rent_value_ + (7 * fixed_value)
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.annual_increase_type == "Accumulated Rate":
                        rent_value = x6
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.marketing_increase_type == "Fixed Rate":
                        marketing_value = self.marketing_amount + (7 * fixed_value1)
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.marketing_increase_type == "Accumulated Rate":
                        marketing_value = m6
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.maintenance_increase_type == "Fixed Rate":
                        maintenance_value = self.maintenance_amount + (7 * fixed_value2)
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                    if self.maintenance_increase_type == "Accumulated Rate":
                        maintenance_value = s6
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                if b >= (96 - self.grace_period ) and b <= (107 - self.grace_period ):
                    if self.annual_increase_type == "Fixed Rate":
                        rent_value = self.rent_value_ + (8 * fixed_value)
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.annual_increase_type == "Accumulated Rate":
                        rent_value = x7
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.marketing_increase_type == "Fixed Rate":
                        marketing_value = self.marketing_amount + (8 * fixed_value1)
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.marketing_increase_type == "Accumulated Rate":
                        marketing_value = m7
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.maintenance_increase_type == "Fixed Rate":
                        maintenance_value = self.maintenance_amount + (8 * fixed_value2)
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                    if self.maintenance_increase_type == "Accumulated Rate":
                        maintenance_value = s7
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                if b >= (108 - self.grace_period ) and b <= (119 - self.grace_period ):
                    if self.annual_increase_type == "Fixed Rate":
                        rent_value = self.rent_value_ + (9 * fixed_value)
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.annual_increase_type == "Accumulated Rate":
                        rent_value = x8
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.marketing_increase_type == "Fixed Rate":
                        marketing_value = self.marketing_amount + (9 * fixed_value1)
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.marketing_increase_type == "Accumulated Rate":
                        marketing_value = m8
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.maintenance_increase_type == "Fixed Rate":
                        maintenance_value = self.maintenance_amount + (9 * fixed_value2)
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                    if self.maintenance_increase_type == "Accumulated Rate":
                        maintenance_value = s8
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                if b >= (120 - self.grace_period ) and b <= (131 - self.grace_period ):
                    if self.annual_increase_type == "Fixed Rate":
                        rent_value = self.rent_value_ + (10 * fixed_value)
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.annual_increase_type == "Accumulated Rate":
                        rent_value = x9
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.marketing_increase_type == "Fixed Rate":
                        marketing_value = self.marketing_amount + (10 * fixed_value1)
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.marketing_increase_type == "Accumulated Rate":
                        marketing_value = m9
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.maintenance_increase_type == "Fixed Rate":
                        maintenance_value = self.maintenance_amount + (10 * fixed_value2)
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                    if self.maintenance_increase_type == "Accumulated Rate":
                        maintenance_value = s9
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                if b >= (132 - self.grace_period ) and b <= (143 - self.grace_period ):
                    if self.annual_increase_type == "Fixed Rate":
                        rent_value = self.rent_value_ + (11 * fixed_value)
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.annual_increase_type == "Accumulated Rate":
                        rent_value = x10
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.marketing_increase_type == "Fixed Rate":
                        marketing_value = self.marketing_amount + (11 * fixed_value1)
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.marketing_increase_type == "Accumulated Rate":
                        marketing_value = m10
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.maintenance_increase_type == "Fixed Rate":
                        maintenance_value = self.maintenance_amount + (11 * fixed_value2)
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                    if self.maintenance_increase_type == "Accumulated Rate":
                        maintenance_value = s10
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                if b >= (144 - self.grace_period ) and b <= (155 - self.grace_period ):
                    if self.annual_increase_type == "Fixed Rate":
                        rent_value = self.rent_value_ + (12 * fixed_value)
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.annual_increase_type == "Accumulated Rate":
                        rent_value = x11
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.marketing_increase_type == "Fixed Rate":
                        marketing_value = self.marketing_amount + (12 * fixed_value1)
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.marketing_increase_type == "Accumulated Rate":
                        marketing_value = m11
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.maintenance_increase_type == "Fixed Rate":
                        maintenance_value = self.maintenance_amount + (12 * fixed_value2)
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                    if self.maintenance_increase_type == "Accumulated Rate":
                        maintenance_value = s11
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                if b >= (156 - self.grace_period ) and b <= (167 - self.grace_period ):
                    if self.annual_increase_type == "Fixed Rate":
                        rent_value = self.rent_value_ + (13 * fixed_value)
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.annual_increase_type == "Accumulated Rate":
                        rent_value = x12
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.marketing_increase_type == "Fixed Rate":
                        marketing_value = self.marketing_amount + (13 * fixed_value1)
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.marketing_increase_type == "Accumulated Rate":
                        marketing_value = m12
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.maintenance_increase_type == "Fixed Rate":
                        maintenance_value = self.maintenance_amount + (13 * fixed_value2)
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                    if self.maintenance_increase_type == "Accumulated Rate":
                        maintenance_value = s12
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                if b >= (168 - self.grace_period ) and b <= (179 - self.grace_period ):
                    if self.annual_increase_type == "Fixed Rate":
                        rent_value = self.rent_value_ + (14 * fixed_value)
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.annual_increase_type == "Accumulated Rate":
                        rent_value = x13
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.marketing_increase_type == "Fixed Rate":
                        marketing_value = self.marketing_amount + (14 * fixed_value1)
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.marketing_increase_type == "Accumulated Rate":
                        marketing_value = m13
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.maintenance_increase_type == "Fixed Rate":
                        maintenance_value = self.maintenance_amount + (14 * fixed_value2)
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                    if self.maintenance_increase_type == "Accumulated Rate":
                        maintenance_value = s13
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                if b >= (180 - self.grace_period ) and b <= (191 - self.grace_period ):
                    if self.annual_increase_type == "Fixed Rate":
                        rent_value = self.rent_value_ + (15 * fixed_value)
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.annual_increase_type == "Accumulated Rate":
                        rent_value = x14
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.marketing_increase_type == "Fixed Rate":
                        marketing_value = self.marketing_amount + (15 * fixed_value1)
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.marketing_increase_type == "Accumulated Rate":
                        marketing_value = m14
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.maintenance_increase_type == "Fixed Rate":
                        maintenance_value = self.maintenance_amount + (15 * fixed_value2)
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                    if self.maintenance_increase_type == "Accumulated Rate":
                        maintenance_value = s14
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                if b >= (192 - self.grace_period ) and b <= (203 - self.grace_period ):
                    if self.annual_increase_type == "Fixed Rate": 
                        rent_value = self.rent_value_ + (16 * fixed_value)
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.annual_increase_type == "Accumulated Rate":
                        rent_value = x15
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.marketing_increase_type == "Fixed Rate":
                        marketing_value = self.marketing_amount + (16 * fixed_value1)
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.marketing_increase_type == "Accumulated Rate":
                        marketing_value = m15
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.maintenance_increase_type == "Fixed Rate":
                        maintenance_value = self.maintenance_amount + (16 * fixed_value2)
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                    if self.maintenance_increase_type == "Accumulated Rate":
                        maintenance_value = s15
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                if b >= (204 - self.grace_period ) and b <= (215 - self.grace_period ):
                    if self.annual_increase_type == "Fixed Rate":
                        rent_value = self.rent_value_ + (17 * fixed_value)
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.annual_increase_type == "Accumulated Rate":
                        rent_value = x16
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.marketing_increase_type == "Fixed Rate":
                        marketing_value = self.marketing_amount + (17 * fixed_value1)
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.marketing_increase_type == "Accumulated Rate":
                        marketing_value = m16
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.maintenance_increase_type == "Fixed Rate":
                        maintenance_value = self.maintenance_amount + (17 * fixed_value2)
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                    if self.maintenance_increase_type == "Accumulated Rate":
                        maintenance_value = s16
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                if b >= (216 - self.grace_period ) and b <= (227 - self.grace_period ):
                    if self.annual_increase_type == "Fixed Rate":
                        rent_value = self.rent_value_ + (18 * fixed_value)
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.annual_increase_type == "Accumulated Rate":
                        rent_value = x17
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.marketing_increase_type == "Fixed Rate":
                        marketing_value = self.marketing_amount + (18 * fixed_value1)
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.marketing_increase_type == "Accumulated Rate":
                        marketing_value = m17
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.maintenance_increase_type == "Fixed Rate":
                        maintenance_value = self.maintenance_amount + (18 * fixed_value2)
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                    if self.maintenance_increase_type == "Accumulated Rate":
                        maintenance_value = s17
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                if b >= (228 - self.grace_period ) and b <= (239 - self.grace_period ):
                    if self.annual_increase_type == "Fixed Rate":
                        rent_value = self.rent_value_ + (19 * fixed_value)
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.annual_increase_type == "Accumulated Rate":
                        rent_value = x18
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.marketing_increase_type == "Fixed Rate":
                        marketing_value = self.marketing_amount + (19 * fixed_value1)
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.marketing_increase_type == "Accumulated Rate":
                        marketing_value = m18
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.maintenance_increase_type == "Fixed Rate":
                        maintenance_value = self.maintenance_amount + (19 * fixed_value2)
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                    if self.maintenance_increase_type == "Accumulated Rate":
                        maintenance_value = s18
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value / 30

                if b >= (240 - self.grace_period ) and b <= (251 - self.grace_period ):
                    if self.annual_increase_type == "Fixed Rate":
                        rent_value = self.rent_value_ + (20 * fixed_value)
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.annual_increase_type == "Accumulated Rate":
                        rent_value = x19
                        monthly_payment = rent_value
                        daily_rent_value = rent_value / 30

                    if self.marketing_increase_type == "Fixed Rate":
                        marketing_value = self.marketing_amount + (20 * fixed_value1)
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.marketing_increase_type == "Accumulated Rate":
                        marketing_value = m19
                        monthly_marketing = marketing_value
                        daily_marketing = marketing_value / 30

                    if self.maintenance_increase_type == "Fixed Rate":
                        maintenance_value = self.maintenance_amount + (20 * fixed_value2)
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value /30

                    if self.maintenance_increase_type == "Accumulated Rate":
                        maintenance_value = s19
                        monthly_maintenance = maintenance_value
                        daily_maintenance = maintenance_value /30

                b += 1
                a -= 1
            if self.no_of_days > 0:
                next_payment_date = add_days(payment_date, days=(self.no_of_days - 1))
                payment_date = next_payment_date
                self.append("contract_repayment_schedule", {
                    "payment_date": payment_date,
                    "monthly_payment": daily_rent_value * self.no_of_days,
                    "base_monthly_payment_": (daily_rent_value * self.no_of_days) * self.conversion_rate,
                    "marketing": daily_marketing * self.no_of_days,
                    "base_marketing": (daily_marketing * self.no_of_days) * self.conversion_rate,
                    "maintenance": daily_maintenance * self.no_of_days,
                    "base_maintenance": (daily_maintenance * self.no_of_days) * self.conversion_rate,
					"electricity": (self.electricity_amount / 30) * self.no_of_days,
					"base_electricity": (self.base_electricity_amount / 30) * self.no_of_days
                })
            total = 0
            for d in self.contract_repayment_schedule:
                d.total = d.monthly_payment + d.marketing + d.maintenance
                d.base_total = (d.monthly_payment + d.marketing + d.maintenance) * self.conversion_rate
                d.net_total = d.monthly_payment + d.marketing + d.maintenance
                d.base_net_total = (d.monthly_payment + d.marketing + d.maintenance) * self.conversion_rate
                total += d.net_total
                d.invoice_amount = 0
                d.paid_amount = 0
                d.outstanding_amount = 0
            self.total_payable_amount = total
            self.base_total_payable_amount = self.conversion_rate * self.total_payable_amount
            
    @frappe.whitelist()
    def calculate_net_total(self):
        total = 0
        for d in self.contract_repayment_schedule:
            if d.discount_type == "Percent":
                d.discount_amount = d.total * d.discount_percent / 100
                d.base_discount_amount = d.discount_amount * self.conversion_rate

            if not d.discount_type:
                d.discount_amount = 0
                d.base_discount_amount = 0

            d.net_total = d.total - d.discount_amount
            d.base_net_total = d.net_total * self.conversion_rate
            total += d.net_total

        self.total_payable_amount = total
        self.base_total_payable_amount = self.conversion_rate * self.total_payable_amount
    @frappe.whitelist()
    def contract_defaults(self):
        
        sales_invoice_item = frappe.db.get_single_value("Contract Defaults", "default_item_code")
        self.lease_item = sales_invoice_item
        mode_of_payment = frappe.db.get_single_value("Contract Defaults", "default_mode_of_payment")
        self.default_mode_of_payment = mode_of_payment
        electricity_account = frappe.db.get_single_value("Contract Defaults", "electricity_expense_account")
        self.electricity_expense_account = electricity_account
        mode_of_payment_account = frappe.db.get_value('Mode of Payment Account', {'parent': mode_of_payment},'default_account')
        self.mode_of_payment_account = mode_of_payment_account
        default_tax_template = frappe.db.get_value("Item", {"Name": sales_invoice_item}, "default_tax_template")
        self.default_tax_template = default_tax_template

    @frappe.whitelist()
    def calculate_net_totals(self): 
       pass
        
    @frappe.whitelist()
    def calculate_totals(self):
        
        if not self.conversion_rate:
            self.conversion_rate = get_exchange_rate(self.currency, "EGP")

        if (self.internal_space + self.external_space) == 0:
            self.meter_price = self.rent_value_
            self.base_meter_price = self.rent_value_ * self.conversion_rate
        else:
            self.meter_price = self.rent_value_ / (self.internal_space + self.external_space)
            self.base_meter_price = (self.rent_value_ / (
                        self.internal_space + self.external_space)) * self.conversion_rate

        self.base_rent_value = self.conversion_rate * self.rent_value_
        self.total_payable_amount = 0

        self.base_minimum_rent = self.conversion_rate * self.minimum_rent

        if self.maintenance_based_on == "Percent":
            self.maintenance_amount = self.rent_value_ * self.maintenance_percent / 100
        self.base_maintenance_amount = self.maintenance_amount * self.conversion_rate

        if self.marketing_based_on == "Percent":
            self.marketing_amount = self.rent_value_ * self.marketing_percent / 100
        self.base_marketing_amount = self.marketing_amount * self.conversion_rate

        if self.electricity_based_on == "Percent":
            self.electricity_amount = self.rent_value_ * self.electricity_percent / 100
        self.base_electricity_amount = self.electricity_amount * self.conversion_rate

        if self.with_insurance:
            self.base_insurance_value = self.insurance_value * self.conversion_rate

        if self.with_advanced_payment:
            self.base_advanced_amount = self.advanced_amount * self.conversion_rate


    @frappe.whitelist()
    def create_water_journal(self):
        water_expense_account = frappe.db.get_single_value("Contract Defaults", "water_expense_account")
        customer_account = frappe.db.get_value("Party Account", {"parent": self.customer_group}, "account")
        accounts = [
            {
                "doctype": "Journal Entry Account",
                "account": customer_account,
                "party_type": "Customer",
                "party": self.party,
                "credit": 0,
                "debit": self.base_water_amount,
                "debit_in_account_currency": self.base_water_amount,
                "user_remark": self.name,
                "cost_center": self.cost_center
            },
            {
                "doctype": "Journal Entry Account",
                "account": water_expense_account,
                
                "credit": self.base_water_amount,
                "debit": 0,
                "credit_in_account_currency": self.base_water_amount,
                 "cost_center": self.cost_center,
                "user_remark": self.name
            }
        ]
        new_doc = frappe.get_doc({
            "doctype": "Journal Entry",
            "voucher_type": "Journal Entry",
            "reference_doctype": "PMS Lease Contract",
            "reference_link": self.name,
            "cheque_no": self.name,
            "cheque_date": self.posting_date,
            "posting_date": self.posting_date,
            "accounts": accounts,
            "user_remark": self.party_name + " - Water Expense "

        })
        new_doc.insert(ignore_permissions=True)
        self.reload()
        frappe.msgprint(
            " Journal Entry For Water Expense " + "<a href=/app/journal-entry/" + new_doc.name + ">" + new_doc.name + "</a>" + " Created Successfully ")
    
    @frappe.whitelist()
    def create_electricity_journal(self):
        pass
        '''
        electricity_expense_account = frappe.db.get_single_value("Contract Defaults", "electricity_expense_account")
        customer_account = frappe.db.get_value("Party Account", {"parent": self.party}, "account")
        accounts = [
            {
                "doctype": "Journal Entry Account",
                "account": electricity_expense_account,
                "party_type": "Customer",
                "party": self.party,
                "credit": 0,
                "debit": self.base_electricity_amount,
                "debit_in_account_currency": self.base_electricity_amount, 
                "cost_center": self.cost_center,
                "user_remark": self.name
            },
            {
                "doctype": "Journal Entry Account",
                "account": customer_account,
                
                "credit": self.base_electricity_amount,
                "debit": 0,
                "credit_in_account_currency": self.base_electricity_amount,
                "cost_center": self.cost_center,
                "user_remark": self.name
            }
        ]
        new_doc = frappe.get_doc({
            "doctype": "Journal Entry",
            "voucher_type": "Journal Entry",
            "reference_doctype": "PMS Lease Contract",
            "reference_link": self.name,
            "cheque_no": self.name,
            "cheque_date": self.posting_date,
            "posting_date": self.posting_date,
            "accounts": accounts,
            "user_remark": self.party_name + " - Electricity Expense "

        })
        new_doc.insert(ignore_permissions=True)
        self.reload()
        frappe.msgprint(
            " Journal Entry For Electricity Expense " + "<a href=/app/journal-entry/" + new_doc.name + ">" + new_doc.name + "</a>" + " Created Successfully ")
        '''
    @frappe.whitelist()
    def insurance_payment(self):
        default_mode_of_payment = frappe.db.get_single_value("Contract Defaults", "default_mode_of_payment")
        mode_of_payment_account = frappe.db.get_value('Mode of Payment Account', {'parent': default_mode_of_payment},
                                                      'default_account')

        if not default_mode_of_payment:
            frappe.throw(" Please Set A Default Mode Of Payment In Contracts Defaults Page")

        if not mode_of_payment_account:
            frappe.throw(" Please Set A Default Account For Mode Of Payment " + mode_of_payment_account)

        new_doc = frappe.get_doc({
            "doctype": "Payment Entry",
            "reference_doctype": "PMS Lease Contract",
            "reference_link": self.name,
            "posting_date": self.posting_date,
            "payment_type": "Receive",
            "mode_of_payment": default_mode_of_payment,
            "party_type": "Customer",
            "party": self.party,
            "paid_amount": self.base_insurance_value,
            "received_amount": self.base_insurance_value,
            "source_exchange_rate": 1,
            "target_exchange_rate": 1,
            "paid_to": mode_of_payment_account
        })
        new_doc.insert(ignore_permissions=True)
        self.insurance_pe = new_doc.name
        self.save()
        self.reload()
        frappe.msgprint(" Insurance Payment " + "<a href=/app/payment-entry/" + new_doc.name + ">" + new_doc.name + "</a>" + " Created Successfully ")

    @frappe.whitelist()
    def advanced_payment(self):
        default_mode_of_payment = frappe.db.get_single_value("Contract Defaults", "default_mode_of_payment")
        insurance_account = frappe.db.get_single_value("Contract Defaults", "insurance_account")

        if not default_mode_of_payment:
            frappe.throw(" Please Set A Default Mode Of Payment In Contracts Defaults Page ")

        if not insurance_account:
            frappe.throw(" Please Set A Default Insurance Account In Contracts Defaults Page ")

        new_doc = frappe.get_doc({
            "doctype": "Payment Entry",
            "reference_doctype": "PMS Lease Contract",
            "reference_link": self.name,
            "posting_date": self.posting_date,
            "payment_type": "Receive",
            "mode_of_payment": default_mode_of_payment,
            "party_type": "Customer",
            "party": self.party,
            "paid_amount": self.base_advanced_amount,
            "received_amount": self.base_advanced_amount,
            "source_exchange_rate": 1,
            "target_exchange_rate": 1,
            "paid_to": insurance_account
        })
        new_doc.insert(ignore_permissions=True)
        self.advanced_pe = new_doc.name
        self.save()
        self.reload()
        frappe.msgprint(" Advanced Payment " + "<a href=/app/payment-entry/" + new_doc.name + ">" + new_doc.name + "</a>" + " Created Successfully ")


    def make_paid(doc, method=None):
        if doc.reference_doctype == "Lease Contract" and doc.bill_no:
            frappe.set_value('PMS Repayment Schedule', doc.bill_no, 'is_paid', '1')
            frappe.set_value('PMS Repayment Schedule', doc.bill_no, 'journal_entry', doc.name)
            row = frappe.get_doc('PMS Repayment Schedule', doc.bill_no)
            parent = frappe.get_doc('PMS Lease Contract', row.parent)
            cur_tot = parent.total_amount_paid
            row_tot = row.monthly_payment
            new_tot = cur_tot + row_tot
            frappe.set_value('PMS Lease Contract', row.parent, 'total_amount_paid', new_tot)


    def journal_cancel(doc, method=None):
        if doc.reference_doctype == "Lease Contract" and doc.bill_no:
            frappe.db.sql(
                """update `tabJournal Entry` set reference_link ='' where bill_no='{bill_no}'""".format(bill_no=bill_no))
            frappe.set_value('PMS Repayment Schedule', doc.bill_no, 'is_paid', '0')
            frappe.set_value('PMS Repayment Schedule', doc.bill_no, 'journal_entry', "")
            row = frappe.get_doc('PMS Repayment Schedule', doc.bill_no)
            parent = frappe.get_doc('PMS Lease Contract', row.parent)
            cur_tot = parent.total_amount_paid
            row_tot = row.monthly_payment
            new_tot = cur_tot - row_tot
            frappe.set_value('PMS Lease Contract', row.parent, 'total_amount_paid', new_tot)
        if doc.reference_doctype == "PMS Lease Contract":
            contract = frappe.get_doc('PMS Lease Contract', doc.reference_link)
            contract.cancel()


    def set_accured(self):
        frappe.db.sql(
            """update `tabPMS Repayment Schedule` set is_accrued = '1' where payment_date >= date(CURRENT_DATE() + 5) and payment_date < date(CURRENT_DATE() +10) """)
        frappe.db.sql("""update `tabPMS Repayment Schedule` set is_accrued = '1' where payment_date < CURRENT_DATE()""")
