# :bus: Easy-Rider-Bus-Company

You've just been hired by a bus company that started actively using the Internet for business. 

Before you came, their database had been updated a few times by various employees with various levels of skill.  
Your task is to find all the mistakes they made in the database. 

Good news: you have [documentation](https://github.com/spaceowlsoul/Easy-Rider-Bus-Company/tree/main/documentation), but bad news: it's incomplete. This promises to be quite an investigation!

## Step 1. Checking the data type
Check that the types of variables match and all the required fields are filled.

### Objectives

1. The string containing the data in JSON format is passed to standard input.
2. Check that the data types match.
3. Check that the required fields are filled in.
4. Display the information about the number of found errors in total and in each field. Keep in mind that there might be no errors at all.
5. The output should have the same formatting as shown in the [example 1](#example-1).

 The documents that you have: [documentation](https://github.com/spaceowlsoul/Easy-Rider-Bus-Company/blob/main/documentation/Documentation.jpg) and [diagram of the bus lines](https://github.com/spaceowlsoul/Easy-Rider-Bus-Company/blob/main/documentation/Diagram_of_the_bus_line.jpg).

#### Example 1:

Input: [json string](https://github.com/spaceowlsoul/Easy-Rider-Bus-Company/blob/main/test_strings/stage1.json).

Output: 

    Type and required field validation: 8 errors
    bus_id: 2
    stop_id: 1
    stop_name: 1
    next_stop: 1
    stop_type: 1
    a_time: 2

## Step 2. Correct syntax
Check if the syntax is correct. 

### Objectives

1. The string containing the data in JSON format is passed to standard input.
2. Check that the data format complies with the documentation.
3. Only the fields that have such a requirement are relevant, i.e. _stop_name, stop_type, a_time_, so, please, count errors __only for them__.
4. Like in the previous stage, print the information about the number of found errors in total and in each field. Remember that there might be no errors at all.
5. The output should have the same formatting as shown in the [example 2](#example-2).

Note that the time format is military time (24 hours, _hh:mm_). That means that there are __certain restrictions__:

- the first digit cannot be _3, 4_, etc.;
- hours less than 10 should have zero in front of them, _e.g. 08:34_;
- the delimiter should be colon _":"_.

The documents that you have: [documentation](https://github.com/spaceowlsoul/Easy-Rider-Bus-Company/blob/main/documentation/Documentation.jpg) and [diagram of the bus lines](https://github.com/spaceowlsoul/Easy-Rider-Bus-Company/blob/main/documentation/Diagram_of_the_bus_line.jpg).

#### Example 2:

Input: [json string](https://github.com/spaceowlsoul/Easy-Rider-Bus-Company/blob/main/test_strings/stage2.json).

Output: 

    Format validation: 9 errors
    stop_name: 3
    stop_type: 2
    a_time: 4

## Step 3. Bus line info
Make sure that the information about the bus lines and the number of stops is correct.

### Objectives

1. The string containing the data in JSON format is passed to standard input.
2. Find the names of all the bus lines.
3. Verify the number of stops for each line.
4. The output should have the same formatting as shown in the [example 3](#example-3).

The documents that you have: [documentation](https://github.com/spaceowlsoul/Easy-Rider-Bus-Company/blob/main/documentation/Documentation.jpg) and [diagram of the bus lines](https://github.com/spaceowlsoul/Easy-Rider-Bus-Company/blob/main/documentation/Diagram_of_the_bus_line.jpg).

#### Example 3:

Input: [json string](https://github.com/spaceowlsoul/Easy-Rider-Bus-Company/blob/main/test_strings/stage3.json).

Output: 

    Line names and number of stops:
    bus_id: 128, stops: 4
    bus_id: 256, stops: 4
    bus_id: 512, stops: 2
    
## Step 4. Special stops
Find all departure stations, final stops, and transfer stops to fill in the missing specifications.

### Objectives 

1. The string containing the data in JSON format is passed to standard input.
2. Make sure each bus line has exactly one starting point (_S_) and one final stop (_F_).
3. If a bus line does not meet this condition, stop checking and print a message about it. Do not continue checking the other bus lines.
4. If all bus lines meet the condition, count how many starting points and final stops there are. Print their unique names in alphabetical order.
5. Count the transfer stops and print their unique names in alphabetical order. A transfer stop is a stop shared by at least two bus lines.
6. The output should have the same formatting as shown in the examples [4](#example-4) and [5](#example-5).

The documents that you have: [documentation](https://github.com/spaceowlsoul/Easy-Rider-Bus-Company/blob/main/documentation/Documentation.jpg) and [diagram of the bus lines](https://github.com/spaceowlsoul/Easy-Rider-Bus-Company/blob/main/documentation/Diagram_of_the_bus_line.jpg).

#### Example 4:

Input: [json string](https://github.com/spaceowlsoul/Easy-Rider-Bus-Company/blob/main/test_strings/stage4_1.json).

Output: 

    There is no start or end stop for the line: 512.

#### Example 5:

Input: [json string](https://github.com/spaceowlsoul/Easy-Rider-Bus-Company/blob/main/test_strings/stage4_2.json).

Output: 

    Start stops: 3 ['Bourbon Street', 'Pilotow Street', 'Prospekt Avenue']
    Transfer stops: 3 ['Elm Street', 'Sesame Street', 'Sunset Boulevard']
    Finish stops: 2 ['Sesame Street', 'Sunset Boulevard']
 
## Step 5. Unlost in time
Make sure that the stops follow each other and their estimated arrival times make sense.

### Objectives 

1. The string containing the data in JSON format is passed to standard input.
2. Check that the arrival time for the upcoming stops for a given bus line is increasing.
3. If the arrival time for the next stop is earlier than or equal to the time of the current stop, stop checking that bus line and remember the name of the incorrect stop.
4. Display the information for those bus lines that have time anomalies. For the correct stops, do not display anything.
5. If all the lines are correct timewise, print OK.
6. The output should have the same formatting as shown in the examples [6](#example-6) and [7](#example-7).

The documents that you have: [documentation](https://github.com/spaceowlsoul/Easy-Rider-Bus-Company/blob/main/documentation/Documentation.jpg) and [diagram of the bus lines](https://github.com/spaceowlsoul/Easy-Rider-Bus-Company/blob/main/documentation/Diagram_of_the_bus_line.jpg).

#### Example 6:

Input: [json string](https://github.com/spaceowlsoul/Easy-Rider-Bus-Company/blob/main/test_strings/stage5_1.json).

Output: 

    Arrival time test:
    bus_id line 128: wrong time on station Fifth Avenue
    bus_id line 256: wrong time on station Sunset Boulevard

#### Example 7:

Input: [json string](https://github.com/spaceowlsoul/Easy-Rider-Bus-Company/blob/main/test_strings/stage5_2.json).

Output: 

    Arrival time test:
    OK 
    
## Step 6. On-demand
Check that there are no wrongly marked on-demand stops.

### Objectives 

1. The string containing the data in JSON format is passed to standard input.
2. Check that all the departure points, final stops, and transfer stations are not "On-demand".
3. Display the unique names of the stops containing this type of issue. Sort them in ascending order.
4. If everything is fine, print OK.
5. The output should have the same formatting as shown in the examples [8](#example-8) and [9](#example-9).

The documents that you have: [documentation](https://github.com/spaceowlsoul/Easy-Rider-Bus-Company/blob/main/documentation/Documentation.jpg) and [diagram of the bus lines](https://github.com/spaceowlsoul/Easy-Rider-Bus-Company/blob/main/documentation/Diagram_of_the_bus_line.jpg).

#### Example 8:

Input: [json string](https://github.com/spaceowlsoul/Easy-Rider-Bus-Company/blob/main/test_strings/stage6_1.json).

Output: 

    On demand stops test:
    Wrong stop type: ['Elm Street', 'Sunset Boulevard']

#### Example 9:

Input: [json string](https://github.com/spaceowlsoul/Easy-Rider-Bus-Company/blob/main/test_strings/stage6_2.json).

Output: 

    On demand stops test:
    OK 
