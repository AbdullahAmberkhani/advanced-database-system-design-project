<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Spacecraft</title>
</head>
<body>
    <h1>Add New Spacecraft</h1>
    <form method="post" action="/spacecraft/add">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="manufacturer">Manufacturer:</label>
        <input type="text" id="manufacturer" name="manufacturer" required>
        <br>
        <input type="submit" value="Add Spacecraft">
    </form>
    <p><a href="/spacecraft">Back to Spacecraft List</a></p>
</body>
</html>
