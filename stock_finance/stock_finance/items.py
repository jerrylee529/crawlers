# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderMenItem(scrapy.Item):
    num_prefix = scrapy.Field()  # 号段
    province = scrapy.Field()  # 省
    city = scrapy.Field()  # 市
    area_code = scrapy.Field()  # 区号
    post_code = scrapy.Field()  # 邮编
    card_type = scrapy.Field()  # 卡类型， CMCC：中国移动， CUCC：中国联通，CTCC：中国电信
    card_type_name = scrapy.Field()  # 卡类型名称，移动、联通或者电信


class CAPubItem(scrapy.Item):
    cip_no = scrapy.Field()  # cip核字号
    book_name = scrapy.Field()  # 书名
    publisher = scrapy.Field()  # 出版商
    publish_datetime = scrapy.Field()  # 出版时间
    author = scrapy.Field()  # 作者和编者
    owner = scrapy.Field()  # 原著


class WDZJItem(scrapy.Item):
    company_name = scrapy.Field()  # 公司名称
    register_city = scrapy.Field()  # 注册地
    amount = scrapy.Field()  # 成交量(万元)
    income_rate = scrapy.Field()  # 平均预期收益率(%)
    loan_period = scrapy.Field()  # 平均借款期限(月)
    collected_balance = scrapy.Field()  # 待还余额(万元)


class IncomeReportItem(scrapy.Item):
    '''
    利润表
    '''
    security_code = scrapy.Field()
    security_name = scrapy.Field()
    report_date = scrapy.Field()
    report_name = scrapy.Field()
    net_profit = scrapy.Field()  # 净利润
    net_profit_atsopc = scrapy.Field()  # 归属于母公司所有者的净利润
    total_revenue = scrapy.Field()  # 营业总收入
    op = scrapy.Field()  # 营业利润
    #income_from_chg_in_fv = scrapy.Field()
    #invest_incomes_from_rr = scrapy.Field()
    invest_income = scrapy.Field()  # 投资收益
    exchg_gain = scrapy.Field() # 汇兑收益
    #operating_taxes_and_surcharge = scrapy.Field()
    #asset_impairment_loss = scrapy.Field()
    #non_operating_income = scrapy.Field()
    #non_operating_payout = scrapy.Field()
    profit_total_amt = scrapy.Field()
    minority_ga = scrapy.Field()
    basic_eps = scrapy.Field()
    dlt_earnings_per_share = scrapy.Field()
    othr_compre_income_atoopc = scrapy.Field()
    othr_compre_income_atms = scrapy.Field()
    total_compre_income = scrapy.Field()
    total_compre_income_atsopc = scrapy.Field()
    total_compre_income_atms = scrapy.Field()
    othr_compre_income = scrapy.Field()
    net_profit_after_nrgal_atsolc = scrapy.Field()
    income_tax_expenses = scrapy.Field()
    revenue = scrapy.Field()
    operating_costs = scrapy.Field()
    operating_cost = scrapy.Field()
    sales_fee = scrapy.Field()
    manage_fee = scrapy.Field()
    financing_expenses = scrapy.Field()


class BalanceReportItem(scrapy.Item):
    '''
    资产负债表
    '''
    security_code = scrapy.Field()
    security_name = scrapy.Field()
    report_date = scrapy.Field()
    report_name = scrapy.Field()
    total_assets = scrapy.Field()
    total_liab = scrapy.Field()
    asset_liab_ratio = scrapy.Field()
    total_quity_atsopc = scrapy.Field()
    tradable_fnncl_assets = scrapy.Field()
    interest_receivable = scrapy.Field()
    saleable_finacial_assets = scrapy.Field()
    held_to_maturity_invest = scrapy.Field()
    fixed_asset = scrapy.Field()
    intangible_assets = scrapy.Field()
    construction_in_process = scrapy.Field()
    dt_assets = scrapy.Field()
    tradable_fnncl_liab = scrapy.Field()
    payroll_payable = scrapy.Field()
    tax_payable = scrapy.Field()
    estimated_liab = scrapy.Field()
    dt_liab = scrapy.Field()
    bond_payable = scrapy.Field()
    shares = scrapy.Field()
    capital_reserve = scrapy.Field()
    earned_surplus = scrapy.Field()
    undstrbtd_profit = scrapy.Field()
    minority_equity = scrapy.Field()
    total_holders_equity = scrapy.Field()
    total_liab_and_holders_equity = scrapy.Field()
    lt_equity_invest = scrapy.Field()
    currency_funds = scrapy.Field()
    bills_receivable = scrapy.Field()
    account_receivable = scrapy.Field()
    pre_payment = scrapy.Field()
    dividend_receivable = scrapy.Field()
    othr_receivables = scrapy.Field()
    inventory = scrapy.Field()
    nca_due_within_one_year = scrapy.Field()
    othr_current_assets = scrapy.Field()
    current_assets_si = scrapy.Field()
    total_current_assets = scrapy.Field()
    lt_receivable = scrapy.Field()
    invest_property = scrapy.Field()
    dev_expenditure = scrapy.Field()
    goodwill = scrapy.Field()
    lt_deferred_expense = scrapy.Field()
    othr_noncurrent_assets = scrapy.Field()
    noncurrent_assets_si = scrapy.Field()
    total_noncurrent_assets = scrapy.Field()
    st_loan = scrapy.Field()
    bill_payable = scrapy.Field()
    accounts_payable = scrapy.Field()
    pre_receivable = scrapy.Field()
    interest_payable = scrapy.Field()
    dividend_payable = scrapy.Field()
    othr_payables = scrapy.Field()
    noncurrent_liab_due_in1y = scrapy.Field()
    othrcurrent_liab = scrapy.Field()
    current_liab_si = scrapy.Field()
    total_current_liab = scrapy.Field()
    lt_loan = scrapy.Field()
    lt_payable = scrapy.Field()
    special_payable = scrapy.Field()
    othr_non_current_liab = scrapy.Field()
    noncurrent_liab_si = scrapy.Field()
    total_noncurrent_liab = scrapy.Field()
    treasury_stock = scrapy.Field()
    salable_financial_assets = scrapy.Field()
    othr_current_liab = scrapy.Field()


class CashFlowReportItem(scrapy.Item):
    '''
    现金流量表
    '''
    security_code = scrapy.Field()
    security_name = scrapy.Field()
    report_date = scrapy.Field()
    report_name = scrapy.Field()
    ncf_from_oa = scrapy.Field()
    ncf_from_ia = scrapy.Field()
    ncf_from_fa = scrapy.Field()
    cash_received_of_othr_oa = scrapy.Field()
    sub_total_of_ci_from_oa = scrapy.Field()
    cash_paid_to_employee_etc = scrapy.Field()
    payments_of_all_taxes = scrapy.Field()
    othrcash_paid_relating_to_oa = scrapy.Field()
    sub_total_of_cos_from_oa = scrapy.Field()
    cash_received_of_dspsl_invest = scrapy.Field()
    invest_income_cash_received = scrapy.Field()
    net_cash_of_disposal_assets = scrapy.Field()
    net_cash_of_disposal_branch = scrapy.Field()
    cash_received_of_othr_ia = scrapy.Field()
    sub_total_of_ci_from_ia = scrapy.Field()
    invest_paid_cash = scrapy.Field()
    cash_paid_for_assets = scrapy.Field()
    othrcash_paid_relating_to_ia = scrapy.Field()
    sub_total_of_cos_from_ia = scrapy.Field()
    cash_received_of_absorb_invest = scrapy.Field()
    cash_received_from_investor = scrapy.Field()
    cash_received_from_bond_issue = scrapy.Field()
    cash_received_of_borrowing = scrapy.Field()
    cash_received_of_othr_fa = scrapy.Field()
    sub_total_of_ci_from_fa = scrapy.Field()
    cash_pay_for_debt = scrapy.Field()
    cash_paid_of_distribution = scrapy.Field()
    branch_paid_to_minority_holder = scrapy.Field()
    othrcash_paid_relating_to_fa = scrapy.Field()
    sub_total_of_cos_from_fa = scrapy.Field()
    effect_of_exchange_chg_on_cce = scrapy.Field()
    net_increase_in_cce = scrapy.Field()
    initial_balance_of_cce = scrapy.Field()
    final_balance_of_cce = scrapy.Field()
    cash_received_of_sales_service = scrapy.Field()
    refund_of_tax_and_levies = scrapy.Field()
    goods_buy_and_service_cash_pay = scrapy.Field()
    net_cash_amt_from_branch = scrapy.Field()


class XueQiuReportItem(scrapy.Item):
    """
    雪球报告，保存json格式
    """
    security_code = scrapy.Field()  # 代码
    security_name = scrapy.Field()  # 名称
    report_type = scrapy.Field()  # 报表类型 0: 资产负债表 1: 利润分配表 2: 现金流量表
    report_data = scrapy.Field()  # 报表内容, json格式
