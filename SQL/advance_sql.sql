-- Window function syntax
-- WINDOW_FUNCTION() OVER(PARTITION BY COLUMN1 ORDER BY COLUMN2) 

-- ROW_NUMBER()

-- TOP 2 EMPLOYEES from each depratment

SELECT * FROM(
    SELECT
    EMPLOYEED_ID,
    EMPLOYEE_NAME,
    DEPARTMENT,
    CITY,
    SALARY,
    ROW_NUMBER() OVER(PARTITION BY DEPARTMENT ORDER BY SALARY) AS ROW_NUM
    FROM EMPLOYEES
) WHERE ROW_NUM <= 2;


WITH EMP_CTE AS (
    SELECT
    EMPLOYEED_ID,
    EMPLOYEE_NAME,
    DEPARTMENT,
    CITY,
    SALARY,
    ROW_NUMBER() OVER(PARTITION BY DEPARTMENT ORDER BY SALARY) AS ROW_NUM
    FROM EMPLOYEES
)
SELECT * FROM EMP_CTE WHERE ROW_NUM <= 2;


-- TOP SELLING PRODUCTS

WITH PRODUCT_AGG AS (
    SELECT
    PRODUCT_CATEGORY_ID,
    PRODUCT_ID,
    PRODUCT_NAME,
    SUM(ORDER_ITEM_QUANTITY) AS TOTAL_QUANTITY,
    sum(ORDER_ITEM_SUBTOTAL) AS TOTAL_AMOUNT,
    FROM(
        SELECT
        O.ORDER_ITEM_ORDER_ID AS ORDER_ID,
        O.ORDER_ITEM_ID,
        O.ORDER_ITEM_PRODUCT_ID AS PRODUCT_ID,
        O.ORDER_ITEM_QUANTITY,
        O.ORDER_ITEM_SUBTOTAL,
        P.PRODUCT_CATEGORY_ID,
        P.PRODUCT_NAMEFROM ORDER_ITEMS O
        JOIN PRODUCT P 
        ON P.ORDER_ITEM_PRODUCT_ID = P.PRODUCT_ID
    ) GROUP BY PRODUCT_ID, PRODUCT_NAME, PRODUCT_CATEGORY_ID
 )
WINDOWED_CTE AS (
    SELECT *,
    ROW_NUMBER() OVER(PARTITION BY PRODUCT_CATEGORY_ID ORDER BY TOTAL_AMOUNT)) AS ROW_NUM FROM PRODUCT_AGG
)
SELECT* FROM WINDOWED_CTE WHERE ROW_NUM <= 1;


-- TWO PEOPLE WITH SAME SALARY

SELECT *,
ROW_NUMBER() OVER(ORDER BY SALARY) AS ROW_NUM,
RANK() OVER(ORDER BY SALARY) AS RNK,
DENSE_RANK() OVR(ORDER BY SALARY) AS DNS_RNK 
FROM EMPLOYEES;


-- DAY BT DAY SALE

SELECT
SALE_DATE,
PRODUCT_ID,
PRODUCT_NAME,
UNITS_SOLD AS CURRENT_SALE,
LEAD(UNITS_SOLD,1,0) OVER(PARTITION BY PRODUCT_ID ORDER BY SALE_DATE) AS NEXT_DAY_SALE,
LAG(UNITS_SOLD,1,0) OVER(PARTITION BY PRODUCT_ID ORDER BY SALE_DATE) AS PREV_DAY_SALE
FROM SALES;


--CALCULATE % OF TOTAL FOLLOWERS GAINS FOR EACH MONTH
WITH FIRST_PART AS
(
    SELECT USER_ID,
    USER_NAME,
    MONTH,
    (LINKEDIN_FOLLOWERS + FACEBOOK_FOLLOWERS + INSTAGRAM_FOLLOWERS + YOUTUBE_FOLLOWERS) AS TOTAL_FOLLOWERS
)
SECOND_PART AS (
    SELECT *,
    LEAD(TOTAL_FOLLOWERS) OVER(PARTITION BY USER_ID ORDER BY MONTH) AS NEXT_MONTH_FOLLOWERS,
    LAG(TOTAL_FOLLOWERS) OVER(PARTITION BY USER_ID ORDER BY MONTH) AS PREV_MONTH_FOLLOWERS
    FROM FIRST_PART
)
SELECT *,
ROUND((TOTAL_FOLLOWERS-PREV_MONTH_FOLLOWERS)*100/PREV_MONTH_FOLLOWERS, 2) A FOLLOWERS_GAIN
FROM SECOND_PART;


-- Problem Description:
-- We are given a table called UserVisits which contains logs of the dates that users visited a specific retailer. The table has two columns user_id and visit_date. We have to write an SQL query to find out the largest window of days between each visit and the one right after it (or today if we are considering the last visit) for each user_id. We return the result table ordered by user_id.

-- Example:
-- Given UserVisits table:

-- user_id	visit_date
-- 1	2020-11-28
-- 1	2020-10-20
-- 1	2020-12-3
-- 2	2020-10-5
-- 2	2020-12-9
-- 3	2020-11-11


WITH SORTED_VISITS AS (
    SELECT USER_ID, VISIT_DATE,
    LEAD(VISIT_DATE) OVER(PARTITION BY USER_ID ORDER BY VISIT_DATE) AS SORTED_VISITS_SEQ
),
DIFF_VISIT AS (
    SELECT 
        user_id,
        (COALESCE(next_visit, CURRENT_DATE) - visit_date) AS diff_days
    FROM SORTED_VISITS
)
SELECT USER_ID, MAX(DIFF) AS MAX_DIFF FROM DIFF_VISIT GROUP BY USER_ID ORDER BY USER_ID;




-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | player_id   | int  |
-- | match_day   | date |
-- | result      | enum |
-- +-------------+------+
-- (player_id, match_day) is the primary key for this table.
-- Each row of this table contains the ID of a player, the day of the match they played, and the result of that match.
-- The result column is an ENUM type of ('Win', 'Draw', 'Lose').

-- The winning streak of a player is the number of consecutive wins uninterrupted by draws or losses.

-- Write an SQL query to count the longest winning streak for each player.

-- Return the result table in any order.

-- The query result format is in the following example.

 

-- Example 1:

-- Input: 
-- Matches table:
-- +-----------+------------+--------+
-- | player_id | match_day  | result |
-- +-----------+------------+--------+
-- | 1         | 2022-01-17 | Win    |
-- | 1         | 2022-01-18 | Win    |
-- | 1         | 2022-01-25 | Win    |
-- | 1         | 2022-01-31 | Draw   |
-- | 1         | 2022-02-08 | Win    |
-- | 2         | 2022-02-06 | Lose   |
-- | 2         | 2022-02-08 | Lose   |
-- | 3         | 2022-03-30 | Win    |
-- +-----------+------------+--------+
-- Output: 
-- +-----------+----------------+
-- | player_id | longest_streak |
-- +-----------+----------------+
-- | 1         | 3              |
-- | 2         | 0              |
-- | 3         | 1              |
-- +-----------+----------------+
-- Explanation: 
-- Player 1:
-- From 2022-01-17 to 2022-01-25, player 1 won 3 consecutive matches.
-- On 2022-01-31, player 1 had a draw.
-- On 2022-02-08, player 1 won a match.
-- The longest winning streak was 3 matches.

-- Player 2:
-- From 2022-02-06 to 2022-02-08, player 2 lost 2 consecutive matches.
-- The longest winning streak was 0 matches.

-- Player 3:
-- On 2022-03-30, player 3 won a match.
-- The longest winning streak was 1 match.

-- 1 > top 3 products by sales, top 3 employees by salaries, within cat/dept

select * from (
    SELECT *,
    ROW_NUMBER() OVER(PARTITION by dept order by salary) as rn,
    DENSE_RANK() Over(PARTITION by dept order by salary) as DNS_RNK
    from  employees
) a
where rn <= 2 ---> will not get duplicate salary, if we do DNS_RNK <= 2 then we will get duplicate salaries also


with cte as (
    select catagory, product_id, sum(sales) as sales
    from orders group by catagory, product_id
),
cte1 as (select *,
ROW_NUMBER() over(PARTITION by catagory order by sales desc) as rn
from cte order by sales desc
) select * from cte1 where rn<=5;

--- yoy growth/products with current month sales more than previous month
with cte as (
    select category, year(order_date) as year_order,
    sum(sales) as sales
    from orders
    group by catagory, year(order_date)
),
cte2 as (
    select *,
    lag(sales, 1, sales) over(PARTITION by catagory order by year_order) as previous_year_sales
    from cte
)
select catagory, year_order,
sales,
previous_year_sales,
(sales - previous_year_sales)*100/previous_year_sales as growth_percentage
from cte2;
-- prev year -> use lag or lead desc
-- next year -> use lead or lag desc

-- running/cumulative sales/ rolling n months sales

with cte as (
    select catagory, year(order_date) as year_order,
    sum(sales) as sales
    from orders
    group by catagory, year(order_date)
),
select *,
sum(sales) over(PARTITION by category order by year_order) as cumulative_sales
from cte;

-- rolling 3 months sales

with cte as (
    select year(order_date) as year_order,
    month(order_date) as month_order,
    sum(sales) as sales
    from orders
    group by year(order_date), month(order_date)
),
select *,
sum(sales) over(Porder by year_order, month_order
rows between 2 preceding and current row
) as cumulative_sales
from cte;


-- pivoting -> convert rows into column--year wise each category

select year(order_date),
sum(case when category = 'Furniture' then sales else 0 end) as furniture_sales,
sum(case when category = 'Office Supplies' then sales else 0 end) as office_supplies_sales,
sum(case when category = 'Technology' then sales else 0 end) as technology_sales
from orders
group by year(order_date);