<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Mission</title>
</head>
<body>
    <h1>Add Mission</h1>
    <form method="post" action="/mission/add">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="destination">Destination:</label>
        <input type="text" id="destination" name="destination" required>
        <br>
        <label for="spacecraft_id">Spacecraft:</label>
        <select id="spacecraft_id" name="spacecraft_id" required>
            % for spacecraft in spacecraft_list:
                <option value="{{ spacecraft.id }}">{{ spacecraft.name }}</option>
            % end
        </select>
        <br>
        <input type="submit" value="Add Mission">
    </form>
    <p><a href="/mission">Back to Mission List</a></p>
</body>
</html>

