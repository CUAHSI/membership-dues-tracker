# define dates of exports from memberclicks (YYMMDD)
transaction_export_date = '241009'
institutions_export_date = '240923'
representatives_export_date = '240923'

# information on rep status export
# active: paid dues this current year
# lapsed: did not pay dues for this year
# note -- can modify this to include graced for next year
member_statuses = ['active','lapsed']


# the final target of the pipeline is a list of reps grouped by their member status
rule all:
	input:
		expand(f'07_munge_representatives/out/{transaction_export_date}_{{member_status}}_representatives_list.csv',member_status = member_statuses)

################################# FETCHING #########################################

# this folder is a placeholder for the moment (could ingest member dues crosswalk or 
# other relevant infomation on SharePoint here)

# input files are raw exports from memberclicks, this is all done manually and stored in
# ./02_clean/src/in location

################################# CLEANING #########################################

# mostly changing/dropping column names from raw memberclicks export

# in the clean_transaction_report step I add a column for payment line as the transaction export 
# only reports invoice number. This is useful as many multi year payments are included in the same 
# invoice but different payment lines. 

rule clean_institutions_export:
	input:
		in_filename = f'02_clean/src/in/{institutions_export_date}_institutions_export.csv'
	output:
		out_filename = '02_clean/src/tmp/cleaned_institutions_list.csv'
	script:
		'02_clean/src/clean_institutions_export.py'

rule clean_representatives_export:
	input:
		in_filename = f'02_clean/src/in/{representatives_export_date}_representatives_export.csv'
	output:
		out_filename = '02_clean/src/tmp/cleaned_representatives_list.csv'
	script:
		'02_clean/src/clean_representatives_export.py'

rule clean_transaction_report:
	input:
		in_filename = f'02_clean/src/in/{transaction_export_date}_transaction_report.csv'
	output:
		out_filename = '02_clean/src/tmp/cleaned_transaction_report.csv'
	script:
		'02_clean/src/clean_transaction_report.py'

################################# MUNGING #########################################

# include payments/waivers done outside of MemberClicks; can also modify date for transactions
# done retroactively

# joining member type information from institution profile list to transaction report

# converting values (e.g., date format) and aggregating yearly payments for each insitution

# also flagging where and when initation payments occured

rule modify_payments:
	input:
		in_filename = '02_clean/src/tmp/cleaned_transaction_report.csv'
	output:
		out_filename = '03_munge_transactions/src/tmp/modified_transaction_report.csv'
	script:
		'03_munge_transactions/src/modify_payments.py'

rule join_member_type:
	input:
		in_institutions_filename = '02_clean/src/tmp/cleaned_institutions_list.csv', 
		in_transactions_filename = '03_munge_transactions/src/tmp/modified_transaction_report.csv'
	output:
		out_filename = '03_munge_transactions/src/tmp/joined_transaction_report.csv'
	script:
		'03_munge_transactions/src/join_member_type.py'

rule convert_values:
	input:
		in_filename = '03_munge_transactions/src/tmp/joined_transaction_report.csv' 
	output:
		out_filename = '03_munge_transactions/src/tmp/converted_transaction_report.csv'
	script:
		'03_munge_transactions/src/convert_values.py'

rule combine_payments:
	input:
		in_filename = '03_munge_transactions/src/tmp/converted_transaction_report.csv' 
	output:
		out_filename = '03_munge_transactions/src/tmp/combined_transaction_report.csv'
	script:
		'03_munge_transactions/src/combine_payments.py'

rule track_initiation_payments:
	input:
		in_filename = '03_munge_transactions/src/tmp/combined_transaction_report.csv' 
	output:
		out_filename = '03_munge_transactions/src/tmp/tracked_transaction_report.csv'
	script:
		'03_munge_transactions/src/track_initiation_payments.py'

################################# PROCESSING #########################################

# adjusting payments for 5-year prepay (10% discount) and initiation fees (includes one 
# year of membership)

# creating pivot table of raw payment data that spreads the annual due prepayments out 
# to 2028, a few institutions have membership payments that extend past 2028 and can be 
# flagged in figure

# membership payment structure for reference (could be included in crosswalk outside of code):
# university member: $200/yr ($900 for 5 year prepay)
# primarily undergrad instituion: 70/yr ($315 for 5 year prepay)
# non profit and int'l affiliate: 100/yr ($450 for 5 year prepay) -- note I have actually not 
# seen this one in official CUAHSI literature but this is assumed. nonprofits and int'l
# affiliates just started paying member dues in 2024 so things are a little behind here


rule adjust_payments:
	input:
		in_filename = '03_munge_transactions/src/tmp/tracked_transaction_report.csv' 
	output:
		out_filename = '04_process_transactions/src/tmp/adjusted_transaction_report.csv'
	script:
		'04_process_transactions/src/adjust_payments.py'

rule transform_payments:
	input:
		in_filename = '04_process_transactions/src/tmp/adjusted_transaction_report.csv' 
	output:
		out_filename = '04_process_transactions/src/tmp/transformed_transaction_report.csv'
	script:
		'04_process_transactions/src/transform_payments.py'

rule spread_payments:
	input:
		in_filename = '04_process_transactions/src/tmp/transformed_transaction_report.csv' 
	output:
		out_filename = f'04_process_transactions/out/{transaction_export_date}_membership_payments.csv'
	script:
		'04_process_transactions/src/spread_payments.py'


############################ VISUALIZE TRANSACTIONS #######################################

# this folder is a placeholder for the moment for generating heatmap of transaction data
# across institutions over time



########################### INSTITIUTION MUNGING #########################################

# get membership status (active/lapsed/long-lapsed), filter and report accordingly

# will also create summary table here of member institutions grouped by status over time

rule get_membership_status:
	input:
		in_filename = f'04_process_transactions/out/{transaction_export_date}_membership_payments.csv'
	params:
		statuses = member_statuses
	output:
		out_filename = f'06_munge_institutions/out/{transaction_export_date}_membership_status.csv'
	script:
		'06_munge_institutions/src/get_membership_status.py'

rule filter_institutions:
	input:
		in_filename = f'06_munge_institutions/out/{transaction_export_date}_membership_status.csv'
	params:
		member_status = f'{{member_status}}'
	output:
		out_filename = f'06_munge_institutions/src/tmp/{transaction_export_date}_{{member_status}}_institutions_list.csv'
	script:
		'06_munge_institutions/src/filter_institutions.py'

########################### REPRESENTATIVE MUNGING #######################################

# group representatives based on membership status
rule get_representatives_lists:
	input:
		in_institutions_filename = f'06_munge_institutions/src/tmp/{transaction_export_date}_{{member_status}}_institutions_list.csv',
		in_representatives_filename = '02_clean/src/tmp/cleaned_representatives_list.csv'
	output:
		out_representatives_filename = f'07_munge_representatives/out/{transaction_export_date}_{{member_status}}_representatives_list.csv'
	script:
		'07_munge_representatives/src/get_representatives_lists.py'