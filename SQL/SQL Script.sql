CREATE DATABASE electronics_sales_db;
USE electronics_sales_db;

-- Total Records
SELECT COUNT(*) AS Total_Rows
FROM electronics;

ALTER TABLE electronics
CHANGE COLUMN `ï»¿Order_ID` Order_ID VARCHAR(20);

-- Duplicate Records
SELECT Order_ID,
COUNT(*) AS Duplicate_Count
FROM electronics
GROUP BY Order_ID
HAVING COUNT(*) > 1;

-- Unique Customers
SELECT COUNT(DISTINCT Customer_ID) AS Unique_Customers
FROM electronics;

-- Unique Products
SELECT COUNT(DISTINCT Product_Name) AS Unique_Products
FROM electronics;

-- Date Range
SELECT
MIN(Order_Date) AS Start_Date,
MAX(Order_Date) AS End_Date
FROM electronics;

-- Age Validation
SELECT *
FROM electronics
WHERE Age < 18 OR Age > 80;

-- Order Status Distribution
SELECT
Order_Status,
COUNT(*) AS Orders
FROM electronics
GROUP BY Order_Status;

-- Total Revenue
SELECT ROUND(SUM(Revenue),2) AS Total_Revenue
FROM electronics;

-- Revenue by Year
SELECT
YEAR(Order_Date) AS Sales_Year,
ROUND(SUM(Revenue),2) AS Revenue
FROM electronics
GROUP BY YEAR(Order_Date)
ORDER BY Sales_Year;

-- Revenue by Month
SELECT
MONTHNAME(Order_Date) AS Month_Name,
ROUND(SUM(Revenue),2) AS Revenue
FROM electronics
GROUP BY MONTH(Order_Date), MONTHNAME(Order_Date)
ORDER BY MONTH(Order_Date);

-- Revenue by Region
SELECT
Region,
ROUND(SUM(Revenue),2) AS Revenue
FROM electronics
GROUP BY Region
ORDER BY Revenue DESC;

-- Revenue by State
SELECT
State,
ROUND(SUM(Revenue),2) AS Revenue
FROM electronics
GROUP BY State
ORDER BY Revenue DESC;

-- Revenue by Brand
SELECT
Brand,
ROUND(SUM(Revenue),2) AS Revenue
FROM electronics
GROUP BY Brand
ORDER BY Revenue DESC;

-- Revenue by Product
SELECT
Product_Name,
ROUND(SUM(Revenue),2) AS Revenue
FROM electronics
GROUP BY Product_Name
ORDER BY Revenue DESC;

-- Top 10 Products
SELECT
Product_Name,
ROUND(SUM(Revenue),2) AS Revenue
FROM electronics
GROUP BY Product_Name
ORDER BY Revenue DESC
LIMIT 10;

-- Bottom 10 Products
SELECT
Product_Name,
ROUND(SUM(Revenue),2) AS Revenue
FROM electronics
GROUP BY Product_Name
ORDER BY Revenue ASC
LIMIT 10;

-- Profitablility Analysis
SELECT ROUND(SUM(Profit),2) AS Total_Profit
FROM electronics;

-- Profit by Brand
SELECT
Brand,
ROUND(SUM(Profit),2) AS Profit
FROM electronics
GROUP BY Brand
ORDER BY Profit DESC;

-- Profit by Product
SELECT
Product_Name,
ROUND(SUM(Profit),2) AS Profit
FROM electronics
GROUP BY Product_Name
ORDER BY Profit DESC;

-- Average Profit Margin
SELECT
ROUND(AVG(Profit_Margin),2) AS Avg_Profit_Margin
FROM electronics;

-- Customer Analysis
SELECT
Customer_Segment,
ROUND(SUM(Revenue),2) AS Revenue
FROM electronics
GROUP BY Customer_Segment
ORDER BY Revenue DESC;

-- Revenue by Membership
SELECT
Membership_Type,
ROUND(SUM(Revenue),2) AS Revenue
FROM electronics
GROUP BY Membership_Type
ORDER BY Revenue DESC;

