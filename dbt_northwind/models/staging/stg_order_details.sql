with source as (
    select * from read_csv_auto('../data/raw/northwind_order_details.csv', header=True)
)

select * from source
