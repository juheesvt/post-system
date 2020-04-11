from core.manage import ObjectManager

LOCAL_DB_LOCATION = "C:\\Users\\juheeSVT\\PycharmProjects\\post-system\\core\\local_db"
SERVER_DB_LOCATION = "C:\\Users\\juheeSVT\\PycharmProjects\\post-system\\core\\server_db"

DATABASES = {
    "TRANSACTION_DB": LOCAL_DB_LOCATION + '\\transaction.db',
    "PRODUCT_DB": LOCAL_DB_LOCATION + '\\product.db',
    "ORIGIN_PRODUCT_DB": SERVER_DB_LOCATION + '\\origin.db'
}
