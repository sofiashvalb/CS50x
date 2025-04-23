-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Starting at this table becuase it contains the hints I got for the crime
-- Get the description of the crime
.schema crime_scene_reports
SELECT description FROM crime_scene_reports
WHERE year = 2021 AND month = 7 AND day = 28 AND street = 'Humphrey Street';

-- Got back the time (10:15am) Humphrey Street Bakery place, 3 witnesses (interviews) with transcripts
-- Littering 16:36 no withnesses
-- look at the tables to see what matches new information
.tables
-- Becuase the witnesses mention Bakery
.schema bakery_security_logs
-- Lets see what happens at 10:15am and 16:36
SELECT activity, license_plate, minute FROM bakery_security_logs
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute = 15;
--NO match
SELECT activity, license_plate, minute FROM bakery_security_logs
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 16 AND minute = 36;
--NO match
-- lets see the whole table and see if I can chorten the conditions differently
SELECT * FROM bakery_security_logs;
--lets make it more specific because there is no 10:15 and 16:36 specificly
SELECT activity, license_plate, minute FROM bakery_security_logs
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10;
SELECT activity, license_plate, minute FROM bakery_security_logs
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 16;
-- I'm looking for the log that entered and exited around that time
--the only log that matches enter at 10:44 exit at 16:06 is WD5M8I6
-- Lets see what person matches this license_plate
SELECT * FROM people
WHERE license_plate = 'WD5M8I6';
--  id   |  name  |  phone_number  | passport_number | license_plate |
--+--------+--------+----------------+-----------------+---------------+
--| 660982 | Thomas | (286) 555-0131 | 6034823042      | WD5M8I6
-- now lets look at the witnesses
.schema interviews
SELECT name, transcript FROM interviews
WHERE year = 2021 AND month = 7 AND day = 28;
--We have 6 (or 7 if it's different Eugene) interviews. Lets focus on the relevant ones (mention bakery)

-- Ruth - Sometime within ten minutes of the theft, thief get into a car in the bakery

-- Eugene -someone I recognized. Earlier ,before I arrived at bakery,
--         I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.

--Raymond - thief was leaving the bakery, they (!!)called someone who talked to them for less than a minute.
 --         planning to take the earliest flight out of Fiftyville (!!)tomorrow.
 --         asked the person on phone to purchase the flight ticket.

-- I need to look again at mentrances and exits to see what car has 2 activities (Ruth)
 SELECT license_plate, hour, minute, COUNT(activity)
 FROM bakery_security_logs
 WHERE day = 28 AND hour IN (9, 10) GROUP BY license_plate ORDER BY hour;
--  4328GD8
--| 5P2BI95
--| 6P58WS2
--| G412CB7

-- ATM on Leggett Street before Eugene arrived to the bakery
-- lets see Eugenes log to see the time before bakery
SELECT id, name, license_plate FROM people
WHERE name = 'Eugene';
--   id   |  name  | license_plate |
--+--------+--------+---------------+
--| 280744 | Eugene | 47592FJ

--Check the bakery
SELECT hour, minute FROM bakery_security_logs WHERE activity = 'entrance' AND license_plate = '47592FJ' AND day = 28;
SELECT hour, minute FROM bakery_security_logs WHERE license_plate = '47592FJ' AND day = 28;
--No match - weird!

--Lets check the ATM before the robery time 10:15
.schema atm_transactions
SELECT account_number, transaction_type, amount FROM atm_transactions
WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street';
--+----------------+------------------+--------+
--| account_number | transaction_type | amount |
--+----------------+------------------+--------+
--| 28500762       | withdraw         | 48     |
--| 28296815       | withdraw         | 20     |
--| 76054385       | withdraw         | 60     |
--| 49610011       | withdraw         | 50     |
--| 16153065       | withdraw         | 80     |
--| 86363979       | deposit          | 10     |-- not relevant
--| 25506511       | withdraw         | 20     |
--| 81061156       | withdraw         | 30     |
--| 26013199       | withdraw         | 35     |

--lets look at the bank account to see if something is weird
.schema bank_accounts
SELECT creation_year FROM bank_accounts
WHERE account_number IN (28500762, 28296815, 76054385, 49610011, 16153065, 25506511, 81061156, 26013199);
--nothing special for now
--check the calls
.schema phone_call
SELECT caller, receiver, duration FROM phone_calls
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;
--+----------------+----------------+----------+
--|     caller     |    receiver    | duration |
--+----------------+----------------+----------+
--| (130) 555-0289 | (996) 555-8899 | 51       |
--| (499) 555-9472 | (892) 555-8872 | 36       |
--| (367) 555-5533 | (375) 555-8161 | 45       |
--| (499) 555-9472 | (717) 555-1342 | 50       |
--| (286) 555-6063 | (676) 555-6554 | 43       |
--| (770) 555-1861 | (725) 555-3243 | 49       |
--| (031) 555-6622 | (910) 555-3251 | 38       |
--| (826) 555-1652 | (066) 555-9701 | 55       |
--| (338) 555-6650 | (704) 555-2131 | 54       |

-- lets look at the flights
.schema airports
SELECT id, abbreviation, full_name FROM airports
WHERE city = 'Fiftyville';
--| id | abbreviation |          full_name          |
--+----+--------------+-----------------------------+
--| 8  | CSF          | Fiftyville Regional Airport |
.schema flights
--earliest tommorow flight (July 29, 2021)
SELECT destination_airport_id, hour, minute FROM flights
JOIN airports ON flights.origin_airport_id = airports. id
WHERE flights.year = 2021 AND flights.month = 7 AND flights.day = 29
AND airports.id = 8;
--the earliest one
--| destination_airport_id | hour | minute
--  4                      | 8    | 20
SELECT city FROM airports JOIN flights ON airports.id = flights.destination_airport_id
WHERE flights.destination_airport_id = 4;
-- result: New York City

--to try and find the passenger
SELECT id FROM flights WHERE destination_airport_id = 4 AND year = 2021 AND month = 7 AND day = 29;
-- id = 36
.schema passengers
SELECT passport_number, seat FROM passengers WHERE flight_id = 36;
-------------------+------+
--| passport_number | seat |
--+-----------------+------+
--| 7214083635      | 2A   |
--| 1695452385      | 3B   |
--| 5773159633      | 4A   |
--| 1540955065      | 5C   |
--| 8294398571      | 6C   |
--| 1988161715      | 6D   |
--| 9878712108      | 7A   |
--| 8496433585      | 7B   |!!!!

--with license_plates from the bakery:
SELECT id, phone_number, passport_number FROM people WHERE license_plate IN ('4328GD8', '5P2BI95', '6P58WS2', 'G412CB7');
------------+----------------+-----------------+
--|   id   |  phone_number  | passport_number |
--+--------+----------------+-----------------+
--| 221103 | (725) 555-4692 | 2963008352      |
--| 243696 | (301) 555-4174 | 7526138472      |
--| 398010 | (130) 555-0289 | 1695452385      |
--| 467400 | (389) 555-5198 | 8496433585      |!!!!

-- you can see now that the person on the flight to new york on earliest day of 29 matches one of the people from the above table
SELECT name FROM people WHERE passport_number = 8496433585;
--result - Luca
--lets check luca with phone_calls

--something whent wrong. Going other way
--I have the passports on that flight, lets match them to people to look for phone number
SELECT name, phone_number FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36);
--+--------+----------------+
--|  name  |  phone_number  |
--+--------+----------------+
--| Kenny  | (826) 555-1652 |
--| Sofia  | (130) 555-0289 |
--| Taylor | (286) 555-6063 |
--| Luca   | (389) 555-5198 |
--| Kelsey | (499) 555-9472 |
--| Edward | (328) 555-1152 |
--| Bruce  | (367) 555-5533 |
--| Doris  | (066) 555-9701 |
SELECT receiver, caller, duration FROM phone_calls
WHERE year = 2021 AND month = 7 AND day = 28 AND caller IN (
    SELECT  phone_number FROM people WHERE passport_number IN (
        SELECT passport_number
        FROM passengers WHERE flight_id = 36));
--+----------------+----------------+----------+
--|    receiver    |     caller     | duration |
--+----------------+----------------+----------+
--| (996) 555-8899 | (130) 555-0289 | 51       |
--| (892) 555-8872 | (499) 555-9472 | 36       |
--| (375) 555-8161 | (367) 555-5533 | 45       |
--| (344) 555-9601 | (367) 555-5533 | 120      |
--| (022) 555-4052 | (367) 555-5533 | 241      |
--| (717) 555-1342 | (499) 555-9472 | 50       |
--| (676) 555-6554 | (286) 555-6063 | 43       |
--| (066) 555-9701 | (826) 555-1652 | 55       |
--| (310) 555-8568 | (286) 555-6063 | 235      |
--| (704) 555-5790 | (367) 555-5533 | 75       |
SELECT person_id FROM bank_accounts
WHERE account_number IN (28500762, 28296815, 76054385, 49610011, 16153065, 25506511, 81061156, 26013199);

SELECT name FROM people JOIN bank_accounts ON people.id = bank_accounts.person_id
WHERE bank_accounts.account_number IN (28500762, 28296815, 76054385, 49610011, 16153065, 25506511, 81061156, 26013199);
--I have a match for Bruce Kenny and Luca
--they withdrew from atm, they are on a flight to New York City now lets see who called:
SELECT phone_number, name FROM people WHERE name IN ('Bruce', 'Luca', 'Kenny');
--+----------------+-------+
--|  phone_number  | name  |
--+----------------+-------+
--| (826) 555-1652 | Kenny |
--| (389) 555-5198 | Luca  |
--| (367) 555-5533 | Bruce |
--+----------------+-------+
SELECT receiver, caller, duration FROM phone_calls
WHERE year = 2021 AND month = 7 AND day = 28
AND caller IN ('(826) 555-1652 ', '(389) 555-5198', '(367) 555-5533');
--result: Only (367) 555-5533 nuumber called. Meaning Bruce is the thief
-- to find his accomplice i chose the duration of 45 seconds
SELECT name FROM people WHERE phone_number = '(375) 555-8161';
--result: Robin



