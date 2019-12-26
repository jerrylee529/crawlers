# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import MySQLdb.cursors
#import pymysql


class SpiderMenPipeline(object):
    def process_item(self, item, spider):
        return item


class MobilePhoneLocationPipeline(object):
    def __init__(self, host, port, user, password, db):
        params = dict(
            host=host,
            port=port,
            user=user,
            passwd=password,
            db=db,
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor
        )

        # 使用Twisted中的adbapi获取数据库连接池对象
        self.db_pool = adbapi.ConnectionPool('MySQLdb', **params)

    @classmethod
    def from_crawler(cls, crawler):
        # 获取settings文件中的配置
        host = crawler.settings.get('HOST')
        port = crawler.settings.get('PORT')
        user = crawler.settings.get('USER')
        password = crawler.settings.get('PASSWORD')
        db = crawler.settings.get('DB')
        return cls(host, port, user, password, db)

    def process_item(self, item, spider):
        query = self.db_pool.runInteraction(self.do_insert, item)
        query.addErrback(self.on_error, spider)
        return item

    def do_insert(self, cursor, item):
        sql = "insert into tc_mobile_number(`mobilenumber`, `mobilearea`, `mobilecity`, `mobiletype_name`, `mobiletype`, `AreaCode`, `PostCode`) values(%s, %s, %s, %s, %s, %s, %s)"
        sql += " ON DUPLICATE KEY UPDATE mobilenumber=%s"
        args = (item['num_prefix'], item['province'], item['city'], item['card_type_name'], item['card_type'], item['area_code'], item['post_code'], item['num_prefix'])
        cursor.execute(sql, args)

    def on_error(self, failure, spider):
        spider.logger.error(failure)


class CAPubPipeline(object):
    def __init__(self, host, port, user, password, db):
        params = dict(
            host=host,
            port=port,
            user=user,
            passwd=password,
            db=db,
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor
        )

        # 使用Twisted中的adbapi获取数据库连接池对象
        self.db_pool = adbapi.ConnectionPool('MySQLdb', **params)

    @classmethod
    def from_crawler(cls, crawler):
        # 获取settings文件中的配置
        host = crawler.settings.get('HOST')
        port = crawler.settings.get('PORT')
        user = crawler.settings.get('USER')
        password = crawler.settings.get('PASSWORD')
        db = crawler.settings.get('DB')
        return cls(host, port, user, password, db)

    def process_item(self, item, spider):
        query = self.db_pool.runInteraction(self.do_insert, item)
        query.addErrback(self.on_error, spider)
        return item

    def do_insert(self, cursor, item):
        sql = "insert into capubinfo(`cip_no`, `book_name`, `publisher`, `publish_datetime`, `author`, `owner`) values(%s, %s, %s, %s, %s, %s)"
        sql += " ON DUPLICATE KEY UPDATE cip_no=%s"
        args = (item['cip_no'], item['book_name'], item['publisher'], item['publish_datetime'], item['author'], item['owner'], item['cip_no'])
        cursor.execute(sql, args)

    def on_error(self, failure, spider):
        spider.logger.error(failure)


class WDZJPipeline(object):
    def __init__(self, host, port, user, password, db):
        params = dict(
            host=host,
            port=port,
            user=user,
            passwd=password,
            db=db,
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor
        )

        # 使用Twisted中的adbapi获取数据库连接池对象
        self.db_pool = adbapi.ConnectionPool('MySQLdb', **params)

    @classmethod
    def from_crawler(cls, crawler):
        # 获取settings文件中的配置
        host = crawler.settings.get('HOST')
        port = crawler.settings.get('PORT')
        user = crawler.settings.get('USER')
        password = crawler.settings.get('PASSWORD')
        db = crawler.settings.get('DB')
        return cls(host, port, user, password, db)

    def process_item(self, item, spider):
        query = self.db_pool.runInteraction(self.do_insert, item)
        query.addErrback(self.on_error, spider)
        return item

    def do_insert(self, cursor, item):
        sql = "insert into wdzj_info(`company_name`, `register_city`, `amount`, `income_rate`, `loan_period`, `collected_balance`) values(%s, %s, %s, %s, %s, %s)"
        args = (item['company_name'], item['register_city'], item['amount'], item['income_rate'], item['loan_period'], item['collected_balance'])
        cursor.execute(sql, args)

    def on_error(self, failure, spider):
        spider.logger.error(failure)


class XueQiuIncomeReportPipeline(object):
    def __init__(self, host, port, user, password, db):
        params = dict(
            host=host,
            port=port,
            user=user,
            passwd=password,
            db=db,
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor
        )

        # 使用Twisted中的adbapi获取数据库连接池对象
        self.db_pool = adbapi.ConnectionPool('MySQLdb', **params)

    @classmethod
    def from_crawler(cls, crawler):
        # 获取settings文件中的配置
        host = crawler.settings.get('HOST')
        port = crawler.settings.get('PORT')
        user = crawler.settings.get('USER')
        password = crawler.settings.get('PASSWORD')
        db = crawler.settings.get('DB')
        return cls(host, port, user, password, db)

    def process_item(self, item, spider):
        query = self.db_pool.runInteraction(self.do_insert, item)
        query.addErrback(self.on_error, spider)
        return item

    def do_insert(self, cursor, item):
        sql = "insert into xueqiu_report_info(`report_date`, `report_name`, `net_profit`, `net_profit_atsopc`, `total_revenue`, " \
              "`op`, `income_from_chg_in_fv`, `invest_incomes_from_rr`, `invest_income`, `exchg_gain`, `operating_taxes_and_surcharge`, " \
              "`asset_impairment_loss`, `non_operating_income`, `non_operating_payout`, `profit_total_amt`, `minority_ga`, `basic_eps`," \
              "`dlt_earnings_per_share`, `othr_compre_income_atoopc`, `othr_compre_income_atms`, `total_compre_income`, `total_compre_income_atsopc`, " \
              "`total_compre_income_atms`, `othr_compre_income`, `net_profit_after_nrgal_atsolc`, `income_tax_expenses`, " \
              "`revenue`, `operating_costs`, `operating_cost`, `sales_fee`, `manage_fee`, `financing_expenses`) " \
              "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        args = (item['report_date'], item['report_name'], item['net_profit'], item['net_profit_atsopc'], item['total_revenue'],
                item['op'], item['income_from_chg_in_fv'], item['invest_incomes_from_rr'], item['invest_income'], item['exchg_gain'],
                item['operating_taxes_and_surcharge'], item['asset_impairment_loss'], item['non_operating_income'], item['non_operating_payout'],
                item['profit_total_amt'], item['minority_ga'], item['basic_eps'], item['dlt_earnings_per_share'],
                item['othr_compre_income_atoopc'], item['othr_compre_income_atms'], item['total_compre_income'], item['total_compre_income_atsopc'],
                item['total_compre_income_atms'], item['othr_compre_income'], item['net_profit_after_nrgal_atsolc'], item['income_tax_expenses'],
                item['revenue'], item['operating_costs'], item['operating_cost'], item['sales_fee'],
                item['manage_fee'], item['financing_expenses'])
        cursor.execute(sql, args)

    def on_error(self, failure, spider):
        spider.logger.error(failure)


class XueQiuCashFlowReportPipeline(object):
    def __init__(self, host, port, user, password, db):
        params = dict(
            host=host,
            port=port,
            user=user,
            passwd=password,
            db=db,
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor
        )

        # 使用Twisted中的adbapi获取数据库连接池对象
        self.db_pool = adbapi.ConnectionPool('MySQLdb', **params)

    @classmethod
    def from_crawler(cls, crawler):
        # 获取settings文件中的配置
        host = crawler.settings.get('HOST')
        port = crawler.settings.get('PORT')
        user = crawler.settings.get('USER')
        password = crawler.settings.get('PASSWORD')
        db = crawler.settings.get('DB')
        return cls(host, port, user, password, db)

    def process_item(self, item, spider):
        query = self.db_pool.runInteraction(self.do_insert, item)
        query.addErrback(self.on_error, spider)
        return item

    def do_insert(self, cursor, item):
        sql = "insert into xueqiu_report_info(`report_date`, `report_name`, `net_profit`, `net_profit_atsopc`, `total_revenue`, " \
              "`op`, `income_from_chg_in_fv`, `invest_incomes_from_rr`, `invest_income`, `exchg_gain`, `operating_taxes_and_surcharge`, " \
              "`asset_impairment_loss`, `non_operating_income`, `non_operating_payout`, `profit_total_amt`, `minority_ga`, `basic_eps`," \
              "`dlt_earnings_per_share`, `othr_compre_income_atoopc`, `othr_compre_income_atms`, `total_compre_income`, `total_compre_income_atsopc`, " \
              "`total_compre_income_atms`, `othr_compre_income`, `net_profit_after_nrgal_atsolc`, `income_tax_expenses`, " \
              "`revenue`, `operating_costs`, `operating_cost`, `sales_fee`, `manage_fee`, `financing_expenses`) " \
              "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        args = (item['report_date'], item['report_name'], item['net_profit'], item['net_profit_atsopc'], item['total_revenue'],
                item['op'], item['income_from_chg_in_fv'], item['invest_incomes_from_rr'], item['invest_income'], item['exchg_gain'],
                item['operating_taxes_and_surcharge'], item['asset_impairment_loss'], item['non_operating_income'], item['non_operating_payout'],
                item['profit_total_amt'], item['minority_ga'], item['basic_eps'], item['dlt_earnings_per_share'],
                item['othr_compre_income_atoopc'], item['othr_compre_income_atms'], item['total_compre_income'], item['total_compre_income_atsopc'],
                item['total_compre_income_atms'], item['othr_compre_income'], item['net_profit_after_nrgal_atsolc'], item['income_tax_expenses'],
                item['revenue'], item['operating_costs'], item['operating_cost'], item['sales_fee'],
                item['manage_fee'], item['financing_expenses'])
        cursor.execute(sql, args)

    def on_error(self, failure, spider):
        spider.logger.error(failure)


class XueQiuBalanceReportPipeline(object):
    def __init__(self, host, port, user, password, db):
        params = dict(
            host=host,
            port=port,
            user=user,
            passwd=password,
            db=db,
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor
        )

        # 使用Twisted中的adbapi获取数据库连接池对象
        self.db_pool = adbapi.ConnectionPool('MySQLdb', **params)

    @classmethod
    def from_crawler(cls, crawler):
        # 获取settings文件中的配置
        host = crawler.settings.get('HOST')
        port = crawler.settings.get('PORT')
        user = crawler.settings.get('USER')
        password = crawler.settings.get('PASSWORD')
        db = crawler.settings.get('DB')
        return cls(host, port, user, password, db)

    def process_item(self, item, spider):
        query = self.db_pool.runInteraction(self.do_insert, item)
        query.addErrback(self.on_error, spider)
        return item

    def do_insert(self, cursor, item):
        sql = "insert into xueqiu_report_info(`report_date`, `report_name`, `net_profit`, `net_profit_atsopc`, `total_revenue`, " \
              "`op`, `income_from_chg_in_fv`, `invest_incomes_from_rr`, `invest_income`, `exchg_gain`, `operating_taxes_and_surcharge`, " \
              "`asset_impairment_loss`, `non_operating_income`, `non_operating_payout`, `profit_total_amt`, `minority_ga`, `basic_eps`," \
              "`dlt_earnings_per_share`, `othr_compre_income_atoopc`, `othr_compre_income_atms`, `total_compre_income`, `total_compre_income_atsopc`, " \
              "`total_compre_income_atms`, `othr_compre_income`, `net_profit_after_nrgal_atsolc`, `income_tax_expenses`, " \
              "`revenue`, `operating_costs`, `operating_cost`, `sales_fee`, `manage_fee`, `financing_expenses`) " \
              "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        args = (item['report_date'], item['report_name'], item['net_profit'], item['net_profit_atsopc'], item['total_revenue'],
                item['op'], item['income_from_chg_in_fv'], item['invest_incomes_from_rr'], item['invest_income'], item['exchg_gain'],
                item['operating_taxes_and_surcharge'], item['asset_impairment_loss'], item['non_operating_income'], item['non_operating_payout'],
                item['profit_total_amt'], item['minority_ga'], item['basic_eps'], item['dlt_earnings_per_share'],
                item['othr_compre_income_atoopc'], item['othr_compre_income_atms'], item['total_compre_income'], item['total_compre_income_atsopc'],
                item['total_compre_income_atms'], item['othr_compre_income'], item['net_profit_after_nrgal_atsolc'], item['income_tax_expenses'],
                item['revenue'], item['operating_costs'], item['operating_cost'], item['sales_fee'],
                item['manage_fee'], item['financing_expenses'])
        cursor.execute(sql, args)

    def on_error(self, failure, spider):
        spider.logger.error(failure)


class XueQiuReportPipeline(object):
    def __init__(self, host, port, user, password, db):
        params = dict(
            host=host,
            port=port,
            user=user,
            passwd=password,
            db=db,
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor
        )

        # 使用Twisted中的adbapi获取数据库连接池对象
        self.db_pool = adbapi.ConnectionPool('MySQLdb', **params)

    @classmethod
    def from_crawler(cls, crawler):
        # 获取settings文件中的配置
        host = crawler.settings.get('HOST')
        port = crawler.settings.get('PORT')
        user = crawler.settings.get('USER')
        password = crawler.settings.get('PASSWORD')
        db = crawler.settings.get('DB')
        return cls(host, port, user, password, db)

    def process_item(self, item, spider):
        query = self.db_pool.runInteraction(self.do_insert, item)
        query.addErrback(self.on_error, spider)
        return item

    def do_insert(self, cursor, item):
        sql = "insert into xueqiu_report_info(`security_code`, `security_name`, `report_type`, `report_data`) values(%s, %s, %s, %s)"
        sql += " ON DUPLICATE KEY UPDATE report_data=%s"
        args = (item['security_code'], item['security_name'], item['report_type'], item['report_data'], item['report_data'])
        cursor.execute(sql, args)

    def on_error(self, failure, spider):
        spider.logger.error(failure)
