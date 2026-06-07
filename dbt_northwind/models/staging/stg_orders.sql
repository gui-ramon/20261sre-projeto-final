with source as (
    select * from read_csv_auto('../data/raw/northwind_orders.csv', header=True)
)

select * from source
