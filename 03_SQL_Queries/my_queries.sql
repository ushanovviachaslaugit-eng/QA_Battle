-- =============================================
-- Мои SQL-запросы к базе авиакомпаний
-- Дата: 2026-08-29
-- =============================================

-- Задача №1: Вывести имена всех пассажиров
SELECT name FROM Passenger;
-- Задача №2: Вывести названия всеx авиакомпаний
SELECT Company.name FROM Company
-- Задача №3: Вывести все рейсы, совершенные из Москвы
SELECT * FROM Trip WHERE town_from = "Moscow"
-- Задача №4: Вывести имена людей, которые заканчиваются на "man"
SELECT name
FROM Passenger
WHERE name LIKE '%man'--% означает "любое количество любых символов" (в данном случае — до этих букв).
-- Задача №5: Количество рейсов на TU-134
SELECT COUNT(*) AS count
FROM Trip
WHERE plane = 'TU-134';
-- Задача №6: Какие компании совершали перелеты на Boeing
SELECT DISTINCT Company.name
FROM Company
JOIN Trip ON Company.id = Trip.company
WHERE Trip.plane = 'Boeing';
-- Задача №7: Вывести все названия самолётов, на которых можно улететь в Москву (Moscow)
SELECT DISTINCT Trip.plane
FROM Trip
WHERE Trip.town_to = 'Moscow'
-- Задача №8: В какие города можно улететь из Парижа (Paris) и сколько времени это займёт?
SELECT
    town_to,
    TIMEDIFF(time_in, time_out) AS flight_time
FROM Trip
WHERE town_from = 'Paris';
-- Задача №9: Компании с рейсами из Владивостока?
SELECT Company.name
FROM Company
JOIN Trip ON Company.id =Trip.company
WHERE Trip.town_from = 'Vladivostok'
-- Задача №10: Вылеты в определенное время
SELECT *
FROM Trip
WHERE DATE(time_out) = '1900-01-01'
  AND TIME(time_out) BETWEEN '10:00:00' AND '14:00:00';