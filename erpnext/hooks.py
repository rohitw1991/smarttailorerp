from erpnext.__version__ import __version__
app_name = "erpnext"
app_title = "ERPNext"
app_publisher = "Web Notes Technologies Pvt. Ltd. and Contributors"
app_description = "Open Source Enterprise Resource Planning for Small and Midsized Organizations"
app_icon = "icon-th"
app_color = "#e74c3c"
app_version = __version__

error_report_email = "support@erpnext.com"

app_include_js = ["assets/js/erpnext.min.js","assets/js/chart.js"]
app_include_css = "assets/css/erpnext.css"
web_include_js = "assets/js/erpnext-web.min.js"

after_install = "erpnext.setup.install.after_install"

boot_session = "erpnext.startup.boot.boot_session"
notification_config = "erpnext.startup.notifications.get_notification_config"

dump_report_map = "erpnext.startup.report_data_map.data_map"
update_website_context = "erpnext.startup.webutils.update_website_context"

on_session_creation = "erpnext.startup.event_handlers.on_session_creation"
before_tests = "erpnext.setup.utils.before_tests"

website_generators = ["Item Group", "Item", "Sales Partner"]

standard_queries = "Customer:erpnext.selling.doctype.customer.customer.get_customer_list"

permission_query_conditions = {
		"Feed": "erpnext.home.doctype.feed.feed.get_permission_query_conditions",
		"Note": "erpnext.utilities.doctype.note.note.get_permission_query_conditions"
	}

has_permission = {
		"Feed": "erpnext.home.doctype.feed.feed.has_permission",
		"Note": "erpnext.utilities.doctype.note.note.has_permission"
	}


doc_events = {
	"*": {
		"on_update": "erpnext.home.update_feed",
		"on_submit": "erpnext.home.update_feed"
	},
	"Comment": {
		"on_update": "erpnext.home.make_comment_feed"
	},
	"Stock Entry": {
		"on_submit": "erpnext.stock.doctype.material_request.material_request.update_completed_qty",
		"on_cancel": "erpnext.stock.doctype.material_request.material_request.update_completed_qty"
	},
	"User": {
		"validate": [
		"erpnext.hr.doctype.employee.employee.validate_employee_role",
		"erpnext.hr.doctype.employee.employee.validate_validity"
		],
		"on_update":[ 
		"erpnext.hr.doctype.employee.employee.update_user_permissions",
		"erpnext.hr.doctype.employee.employee.update_users"
		],
	}
}

scheduler_events = {
	"all": [
		"erpnext.support.doctype.support_ticket.get_support_mails.get_support_mails",
		"erpnext.hr.doctype.job_applicant.get_job_applications.get_job_applications",
		"erpnext.selling.doctype.lead.get_leads.get_leads",
		"erpnext.selling.doctype.lead.get_leads.assign_support"
	],
	"daily": [
		"erpnext.accounts.doctype.sales_invoice.sales_invoice.manage_recurring_invoices",
		"erpnext.stock.utils.reorder_item",
		"erpnext.setup.doctype.email_digest.email_digest.send",
		"erpnext.support.doctype.support_ticket.support_ticket.auto_close_tickets"
	],
	"daily_long": [
		"erpnext.setup.doctype.backup_manager.backup_manager.take_backups_daily"
	],
	"weekly_long": [
		"erpnext.setup.doctype.backup_manager.backup_manager.take_backups_weekly"
	]
}

