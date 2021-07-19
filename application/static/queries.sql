SELECT   Row_number() OVER (ORDER BY popularity DESC) n,
         title,
         popularity,
FROM     commons.movies m
WHERE    Split(m.release_date, '-')[1] = :year
ORDER BY m.popularity DESC 
limit 10

################################################################################

WITH total_revenue AS
(
         SELECT   Sum(revenue)                  AS tot_revenue,
                  Split(m.release_date, '-')[1] as year
         FROM     commons.movies m
         WHERE    split(m.release_date, '-')[1] = :year
         GROUP BY split(m.release_date, '-')[1])
SELECT    row_number() OVER (ORDER BY revenue DESC) n,
          title,
          revenue,
          ROUND(cast(revenue AS DOUBLE) / cast(total_revenue.tot_revenue AS DOUBLE) * 100, 0) percentRevenue
FROM      commons.movies m
LEFT JOIN total_revenue
ON        total_revenue.year = split(m.release_date, '-')[1]
WHERE     split(m.release_date, '-')[1] = :year
ORDER BY  revenue DESC
limit 10

################################################################################

SELECT   Row_number() OVER (ORDER BY Count(generas.genera.name) DESC) n,
         generas.genera.name,
         Count(generas.genera.name) num_movies
FROM     commons.movies m,
         unnest (m.genres as genera) AS generas
WHERE    split(m.release_date, '-')[1] = :year
GROUP BY generas.genera.name
ORDER BY count(generas.genera.name) DESC limit 10

################################################################################

WITH max_genera AS
(
         SELECT   generas.genera.name name
         FROM     commons.movies m,
                  unnest (m.genres as genera) AS generas
         WHERE    split(m.release_date, '-')[1] = :year
         GROUP BY generas.genera.name
         ORDER BY count(generas.genera.name) DESC limit 1),
all_movies AS
(
       SELECT m.title ,
              generas.genera.name,
              m.production_companies
       FROM   commons.movies m,
              unnest (m.genres AS genera) AS generas
       WHERE  split(m.release_date, '-')[1] = :year)
SELECT     Row_number() OVER (order by count(companies.company.name) DESC, companies.company.name ASC) n,
		       all_movies.name,
           companies.company.name production_company,
           count(companies.company.name) num_movies
FROM       max_genera
INNER JOIN all_movies
ON         all_movies.name = max_genera.name,
           unnest(all_movies.production_companies AS company) AS companies
WHERE      all_movies.name = max_genera.name
GROUP BY   companies.company.name,
           all_movies.name
ORDER BY   count(companies.company.name) DESC, companies.company.name ASC
limit 10
