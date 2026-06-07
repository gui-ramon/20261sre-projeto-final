with daily_revenue as (
    select * from {{ ref('fct_net_revenue') }}
),

product_ranking as (
    select
        product_id,
        sum(net_revenue) as total_net_revenue
    from daily_revenue
    group by 1
    order by 2 desc
    limit 10
),

monthly_evolution as (
    select
        product_id,
        month_year,
        sum(net_revenue) as monthly_net_revenue
    from daily_revenue
    where product_id in (select product_id from product_ranking)
    group by 1, 2
)

select
    r.product_id,
    r.total_net_revenue,
    m.month_year,
    m.monthly_net_revenue
from product_ranking r
join monthly_evolution m on r.product_id = m.product_id
order by r.total_net_revenue desc, m.month_year asc
