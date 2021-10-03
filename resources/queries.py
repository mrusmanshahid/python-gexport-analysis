
class SQLQuery:

    def get_stmt_for_order_location_analytics(self,fullvisitorId):
        query = f"""
            WITH CustomerChangedPositions
            AS (
                SELECT 
                    e.fullvisitorid,
                    e.visitNumber,
                    e.visitId,
                    e.transaction_id,
                    ST_GeogPoint(CAST(entry_longitude AS FLOAT64),CAST(entry_latitude AS FLOAT64)) entry_point,
                    ST_GeogPoint(CAST(checkout_longitude AS FLOAT64),CAST(checkout_latitude AS FLOAT64)) checkout_point,
                    ST_DISTANCE(ST_GeogPoint(CAST(entry_longitude AS FLOAT64),CAST(entry_latitude AS FLOAT64)), 
                    ST_GeogPoint(CAST(checkout_longitude AS FLOAT64),CAST(checkout_latitude AS FLOAT64))) distance_meters
                FROM (
                        SELECT  
                                    e.fullvisitorid, 
                                    e.visitNumber,
                                    e.visitId,
                                    MAX(h.transactionId) transaction_id,
                                    MAX(CASE WHEN sc.index = 18 AND h.eventCategory LIKE '%shop_list' THEN sc.value END) as entry_longitude, 
                                    MAX(CASE WHEN sc.index = 19 AND h.eventCategory LIKE '%shop_list' THEN sc.value END) as entry_latitude,
                                    MAX(CASE WHEN sc.index = 18 AND h.eventCategory LIKE '%checkout' THEN sc.value END) as checkout_longitude, 
                                    MAX(CASE WHEN sc.index = 19 AND h.eventCategory LIKE '%checkout' THEN sc.value END) as checkout_latitude
                        FROM `dhh-analytics-hiringspace.GoogleAnalyticsSample.ga_sessions_export` as e,
                        
                        UNNEST(hit) AS h,
                        UNNEST(h.customDimensions) AS sc
                        
                        WHERE (h.eventCategory like '%shop_list' OR h.eventCategory like '%checkout' OR h.eventCategory like '%order_confirmation')
                        AND  e.fullvisitorid = '{fullvisitorId}'
                        
                        GROUP BY
                                    e.fullvisitorid, 
                                    e.visitNumber,
                                    e.visitId
                ) AS E
                WHERE   SAFE_CAST(checkout_latitude AS FLOAT64) IS NOT NULL 
                AND     SAFE_CAST(entry_latitude AS FLOAT64) IS NOT NULL
                AND     ST_DISTANCE(ST_GeogPoint(CAST(entry_longitude AS FLOAT64),CAST(entry_latitude AS FLOAT64)), 
                ST_GeogPoint(CAST(checkout_longitude AS FLOAT64),CAST(checkout_latitude AS FLOAT64))) > 0
            ) 
            
            SELECT
                c.fullvisitorid,  c.visitId, c.transaction_id, c.entry_point,c.checkout_point, c.distance_meters, e.backendOrderId,
                e.frontendOrderId, e.status_id,  e.declinereason_code, e.declinereason_type, e.deliveryType, e.geopointDropoff,
                CASE WHEN c.distance_meters > 0 THEN TRUE ELSE FALSE END address_changed,
                CASE WHEN e.frontendOrderId IS NULL THEN FALSE ELSE TRUE END is_order_placed,
                CASE WHEN e.status_id = 24 THEN TRUE ELSE FALSE END Is_order_delivered
            FROM  CustomerChangedPositions c
            LEFT JOIN  `dhh-analytics-hiringspace.BackendDataSample.transactionalData` e 
            ON e.frontendOrderId = c.transaction_id
        """
        return query
