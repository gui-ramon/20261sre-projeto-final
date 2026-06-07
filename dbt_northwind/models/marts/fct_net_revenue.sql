with orders as (
    select * from {{ ref('stg_orders') }}
),

order_details as (
    select * from {{ ref('stg_order_details') }}
),

joined as (
    select
        od.product_id,
        cast(o.order_date as date) as order_date,
        od.unit_price,
        od.quantity,
        od.discount,
        (od.unit_price * od.quantity * (1 - od.discount)) as net_revenue
    from order_details od
    join orders o on od.order_id = o.order_id
)

select
    product_id,
    order_date,
    strftime('%Y-%m', order_date) as month_year,
    net_revenue
from joined
