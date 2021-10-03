
class SQLQuery:

    def get_stmt_for_order_location_analytics(self,fullvisitorId):
        query = """
            select * from `dynamic-bongo-327518.BackendDataSample.transactionalData` limit 100;
        """
        return query
